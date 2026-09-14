#!/usr/bin/env python3
"""
A spreadsheet writer, in the standard library.

An .xlsx file is a zip of XML parts, and writing the handful this library needs
is a smaller thing than taking a dependency. The book's tools already ask for
pyyaml and, for the build, playwright; a reader who wants the trial snapshot
should not have to install a third.

Only what is actually used is implemented: inline strings, numbers, a bold
header row that stays put when you scroll, a filter on that row, wrapped text
for the long prose columns, and set column widths.

    sheets = [Sheet("Trials", ["Trial", "N"], [["CLEOPATRA", 808]])]
    write("out.xlsx", sheets)

Every cell is written as an explicit inline string or an explicit number, so a
spreadsheet never reinterprets the contents. This matters for a registry: a
result beginning with a minus sign, or a trial named after a formula, is text
here and stays text, which is the failure that makes a CSV of clinical data
untrustworthy.
"""
import io
import re
import zipfile

# Zip entries carry a modification time, and the default is "now", which would
# make two exports of identical data differ byte for byte. The date is fixed so
# that a snapshot changes only when the registry does.
EPOCH = (1980, 1, 1, 0, 0, 0)

# XML 1.0 forbids most control characters outright; no escape exists for them.
# Tab, newline and carriage return are legal and are kept, because the prose
# columns contain newlines.
ILLEGAL = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x84\x86-\x9f]")


class Sheet(object):
    """One tab. `widths` is in characters, per column; `wrap` names the columns
    that hold prose and should wrap rather than run off to the right."""

    def __init__(self, name, headers, rows, widths=None, wrap=(), freeze=True,
                 autofilter=True):
        self.name = sheetname(name)
        self.headers = list(headers)
        self.rows = rows
        self.widths = widths or []
        # A column may be named or numbered. A sheet whose headers repeat, or
        # are blank because it reads as a document rather than a table, cannot
        # be addressed by name.
        self.wrap = {w if isinstance(w, int) else self.headers.index(w)
                     for w in wrap
                     if isinstance(w, int) or w in self.headers}
        self.freeze = freeze
        self.autofilter = autofilter


# A spreadsheet forbids these in a tab name, and caps it at 31 characters.
BAD_NAME = re.compile(r"[\\/?*\[\]:]")
# A cell holds at most this many characters. Nothing here comes close, but a
# registry grows and a silently corrupt file is worse than a visibly cut one.
CELL_MAX = 32767


def sheetname(name):
    n = BAD_NAME.sub("-", str(name)).strip("'")[:31]
    if not n:
        raise ValueError("a sheet needs a name")
    return n


def esc(s):
    s = ILLEGAL.sub("", s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def colname(i):
    """0 -> A, 25 -> Z, 26 -> AA."""
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def cell(ref, value, style):
    if value is None or value == "":
        return '<c r="%s" s="%d"/>' % (ref, style)
    if isinstance(value, bool):
        value = "yes" if value else "no"
    elif isinstance(value, (int, float)):
        return '<c r="%s" s="%d"><v>%s</v></c>' % (ref, style, value)
    text = str(value)
    if len(text) > CELL_MAX:
        text = text[:CELL_MAX - 1] + "\u2026"
    return ('<c r="%s" s="%d" t="inlineStr"><is><t xml:space="preserve">%s'
            '</t></is></c>' % (ref, style, esc(text)))


def sheet_xml(sh):
    n = len(sh.headers)
    out = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
    ]
    if sh.freeze:
        out.append('<sheetViews><sheetView workbookViewId="0">'
                   '<pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" '
                   'state="frozen"/></sheetView></sheetViews>')
    if sh.widths:
        cols = "".join(
            '<col min="%d" max="%d" width="%s" customWidth="1"/>' % (i + 1, i + 1, w)
            for i, w in enumerate(sh.widths) if w)
        out.append("<cols>%s</cols>" % cols)

    out.append("<sheetData>")
    out.append("<row r=\"1\">%s</row>" % "".join(
        cell("%s1" % colname(i), h, 1) for i, h in enumerate(sh.headers)))
    r = 1
    for row in sh.rows:
        r += 1
        cells = []
        for i in range(n):
            v = row[i] if i < len(row) else None
            cells.append(cell("%s%d" % (colname(i), r), v, 2 if i in sh.wrap else 0))
        out.append('<row r="%d">%s</row>' % (r, "".join(cells)))
    out.append("</sheetData>")

    # autoFilter has to follow sheetData; the schema fixes the order.
    if sh.autofilter and n:
        out.append('<autoFilter ref="A1:%s%d"/>' % (colname(n - 1), max(r, 1)))
    out.append("</worksheet>")
    return "".join(out)


STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="2">
  <font><sz val="11"/><name val="Calibri"/></font>
  <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font>
</fonts>
<fills count="3">
  <fill><patternFill patternType="none"/></fill>
  <fill><patternFill patternType="gray125"/></fill>
  <fill><patternFill patternType="solid"><fgColor rgb="FF6B2C4F"/>
    <bgColor indexed="64"/></patternFill></fill>
</fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="3">
  <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1">
    <alignment vertical="top"/></xf>
  <xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1"
      applyFill="1" applyAlignment="1"><alignment vertical="center"/></xf>
  <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1">
    <alignment vertical="top" wrapText="1"/></xf>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Target="xl/workbook.xml" Type="http://schemas.openxmlformats.org/\
officeDocument/2006/relationships/officeDocument"/>
</Relationships>"""


def write(path, sheets):
    """Write the workbook. Returns the bytes as well, so a caller can compare
    them with what is already on disk without reading the file back."""
    types = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.'
             'relationships+xml"/>',
             '<Default Extension="xml" ContentType="application/xml"/>',
             '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-'
             'officedocument.spreadsheetml.sheet.main+xml"/>',
             '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-'
             'officedocument.spreadsheetml.styles+xml"/>']
    wb = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
          '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
          "<sheets>"]
    wr = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
          '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
          '<Relationship Id="rIdS" Target="styles.xml" Type="http://schemas.openxmlformats.org/'
          'officeDocument/2006/relationships/styles"/>']

    for i, sh in enumerate(sheets, 1):
        types.append('<Override PartName="/xl/worksheets/sheet%d.xml" ContentType="application/'
                     'vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' % i)
        wb.append('<sheet name="%s" sheetId="%d" r:id="rId%d"/>' % (esc(sh.name), i, i))
        wr.append('<Relationship Id="rId%d" Target="worksheets/sheet%d.xml" Type="http://'
                  'schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"/>'
                  % (i, i))
    types.append("</Types>")
    wb.append("</sheets></workbook>")
    wr.append("</Relationships>")

    parts = [("[Content_Types].xml", "".join(types)),
             ("_rels/.rels", RELS),
             ("xl/workbook.xml", "".join(wb)),
             ("xl/_rels/workbook.xml.rels", "".join(wr)),
             ("xl/styles.xml", STYLES)]
    for i, sh in enumerate(sheets, 1):
        parts.append(("xl/worksheets/sheet%d.xml" % i, sheet_xml(sh)))

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, text in parts:
            info = zipfile.ZipInfo(name, EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, text.encode("utf-8"))
    data = buf.getvalue()
    if path:
        with io.open(path, "wb") as fh:
            fh.write(data)
    return data
