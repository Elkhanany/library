"""Gather candidate trial papers for the registry completeness sweep.

Sources: PubMed phase 3 breast cancer papers, the reference lists of ESMO and ASCO breast cancer
guidelines (PubMed's cited-reference links), and the NCCN v6.2026 reference list in the repository.
Every paper is fetched from PubMed once and stored as JSON lines in ../data/papers.jsonl.

    python3 gather.py
"""
import csv, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
LIB = "/home/user/library/books/breast-cancer"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
TOOL = "&tool=library-registry-sweep"


def get(url, data=None, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # network hiccup: back off and retry
            if i == tries - 1:
                raise
            time.sleep(2 ** i)
        finally:
            time.sleep(0.4)


def esearch(term):
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": 10000, "retmode": "json"})
    return json.loads(get(EU + "esearch.fcgi?" + q + TOOL))["esearchresult"]["idlist"]


def refs_of(pmids):
    out = {}
    for p in pmids:
        q = urllib.parse.urlencode({"dbfrom": "pubmed", "db": "pubmed", "id": p,
                                    "linkname": "pubmed_pubmed_refs", "retmode": "json"})
        js = json.loads(get(EU + "elink.fcgi?" + q + TOOL))
        ids = []
        for ls in js.get("linksets", []):
            for db in ls.get("linksetdbs", []):
                ids += db.get("links", [])
        out[p] = ids
    return out


NCT = re.compile(r"\bNCT\d{8}\b")
ISRCTN = re.compile(r"\bISRCTN\d{8}\b")
EUDRA = re.compile(r"\b\d{4}-\d{6}-\d{2}\b")


def text(el):
    return "".join(el.itertext()).strip() if el is not None else ""


def efetch(pmids):
    rows = []
    for i in range(0, len(pmids), 200):
        chunk = pmids[i:i + 200]
        body = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"}).encode()
        root = ET.fromstring(get(EU + "efetch.fcgi?" + TOOL[1:], data=body))
        for art in root.findall(".//PubmedArticle"):
            mc = art.find("MedlineCitation")
            pmid = text(mc.find("PMID"))
            a = mc.find("Article")
            title = text(a.find("ArticleTitle"))
            abstract = " ".join(text(x) for x in a.findall(".//AbstractText"))
            year = text(a.find(".//JournalIssue/PubDate/Year")) or text(a.find(".//JournalIssue/PubDate/MedlineDate"))[:4]
            journal = text(a.find(".//ISOAbbreviation"))
            ptypes = [text(x) for x in a.findall(".//PublicationType")]
            mesh = [text(x) for x in mc.findall(".//MeshHeading/DescriptorName")]
            banks = []
            for db in a.findall(".//DataBank"):
                banks += [text(x) for x in db.findall(".//AccessionNumber")]
            blob = " ".join([title, abstract] + banks)
            doi = ""
            for aid in art.findall(".//ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = text(aid)
            rows.append({"pmid": pmid, "title": title, "abstract": abstract, "year": year, "journal": journal,
                         "doi": doi, "ptypes": ptypes, "mesh": mesh,
                         "nct": sorted(set(NCT.findall(blob))), "isrctn": sorted(set(ISRCTN.findall(blob))),
                         "eudract": sorted(set(EUDRA.findall(blob)))})
        print("  fetched %d/%d" % (min(i + 200, len(pmids)), len(pmids)), file=sys.stderr)
    return rows


def main():
    os.makedirs(DATA, exist_ok=True)
    src = {}
    q1 = esearch('"Clinical Trial, Phase III"[pt] AND "Breast Neoplasms"[mh]')
    q2 = esearch('"Randomized Controlled Trial"[pt] AND "Breast Neoplasms"[mh] AND ("phase 3"[tiab] OR "phase III"[tiab])')
    for p in q1 + q2:
        src.setdefault(p, set()).add("pubmed-phase3")
    gl = sorted(set(esearch('"Practice Guideline"[pt] AND "Breast Neoplasms"[mh] AND (ESMO[tiab] OR '
                            '"European Society for Medical Oncology"[ad] OR "American Society of Clinical Oncology"[tiab] '
                            'OR ASCO[tiab]) AND 2015:2026[dp]')
                    + esearch('"Practice Guideline"[pt] AND "Breast Neoplasms"[majr] AND ("Annals of oncology"[ta] '
                              'OR "J Clin Oncol"[ta] OR "ESMO Open"[ta]) AND 2015:2026[dp]')))
    print("guidelines:", len(gl), file=sys.stderr)
    refs = refs_of(gl)
    json.dump(refs, open(os.path.join(DATA, "guideline-refs.json"), "w"))
    for g, ids in refs.items():
        for p in ids:
            src.setdefault(p, set()).add("guideline:" + g)
    for row in csv.DictReader(open(os.path.join(LIB, "gaps", "nccn-breast-v6.2026-references.csv"), encoding="utf-8-sig")):
        if row.get("pmid"):
            src.setdefault(row["pmid"].strip(), set()).add("nccn")
    pmids = sorted(src)
    print("papers to fetch:", len(pmids), file=sys.stderr)
    rows = efetch(pmids)
    with open(os.path.join(DATA, "papers.jsonl"), "w") as fh:
        for r in rows:
            r["sources"] = sorted(src.get(r["pmid"], []))
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    json.dump(gl, open(os.path.join(DATA, "guidelines.json"), "w"))
    print("wrote", len(rows), "papers", file=sys.stderr)


if __name__ == "__main__":
    main()
