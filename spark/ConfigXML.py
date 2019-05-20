import xml.etree.ElementTree as ET
from book import Book, SheetGroup, Sheet

class ConfigXML:
    tree = ET.parse('book.XML')
    root = tree.getroot()
    books ={}
    sheetgroups={}

    def __init__(self):
        self.parseBooks()
        self.parseSheets()

    def parseBooks(self):
        for child in self.root.findall("book"):
            book = Book(child.get("datatable"),
                        child.get("groupname"),
                        child.get("prefix"),
                        child.get("title"),
                        child.get("unit"),
                        child.get("block"),
                        child.get('rmcols'),
                        child.get('sheetgroup'))
            self.books[book.prefix] = book


    def parseSheets(self):
        for sg in self.root.findall('sheetgroup'):
            sheetgroup = []
            for node in sg.findall('sheet'):
                sheet = Sheet(
                    node.get('suffix'),
                    node.get('subtitle'),
                    node.text,
                    node.get('matchlen')
                )
                sheetgroup.append(sheet)
            self.sheetgroups[sg.get('name')] = sheetgroup
