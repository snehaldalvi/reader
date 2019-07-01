
"""import PyPDF2
f=open('Bank Balance Statement.pdf','rb')
"""
from PyPDF2 import PdfFileReader
def get_info(path):

    with open('Bank Balance Statement.pdf', 'rb') as f:

        pdf = PdfFileReader(f)

        info = pdf.getDocumentInfo()

        number_of_pages = pdf.getNumPages()

    print(info)

    #author = info.author

    #creator = info.creator

    #producer = info.producer

    #ubject = info.subject

    title = info.title

if __name__ == '__main__':

    path = 'Bank Balance Statement.pdf'

    get_info(path)

"""
reader=PyPDF2.PdfFileReader(f)
print(reader.getNumPages())
#reader.getNumPages(0)
print(reader.getPage(1))
print(reader.getOutlines())
page=reader.getPage(2)
print(page.extractText())
#page=reader.getPage(1)

"""