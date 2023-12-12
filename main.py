import PyPDF2

merger = PyPDF2.PdfMerger()
pdfFiles = ["A.pdf", "B.pdf"]

for filename in pdfFiles:
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merge.pdf")

