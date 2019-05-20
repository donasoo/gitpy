class Book:

    def __init__(self, datatable, groupname, prefix, title, unit, block, rmcols, sheetgroup):
        self.datatable = datatable
        self.groupname = groupname
        self.prefix = prefix
        self.title = title
        self.unit = unit
        self.block = block
        self.rmcols = rmcols
        self.sheetgroup = sheetgroup



class Sheet:

    def __init__(self, suffix, subtitle, colstr, matchlen=4):
        self.suffix = suffix
        self.subtitle = subtitle
        self.colstr = colstr
        self.matchlen = matchlen


class SheetGroup:

    def __init__(self, name):
        self.name = name
        self.sheets = []

    def addSheet(self, sheet):
        self.sheets.append(sheet)


