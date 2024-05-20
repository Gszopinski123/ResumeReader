from pypdf import PdfReader;

reader = PdfReader('C:/Users/gabes/Projects/ResumeReader/test.pdf')
print(reader.pages[0].extract_text())