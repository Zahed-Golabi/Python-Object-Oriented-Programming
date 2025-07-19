class PDFDocument():
    def open(self):
        return "The PDF file is open!"
    
class WordDocument():
    def open(self):
        return "The Word file is open!"
    

def display_document(doc):
    return doc.open()


pdf1 = PDFDocument()
word1 = WordDocument()

print(display_document(pdf1))
print(display_document(word1))