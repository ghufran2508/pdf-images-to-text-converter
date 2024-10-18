# # importing all the required modules
# import PyPDF2

# # creating a pdf reader object
# reader = PyPDF2.PdfReader('./Automation Example Docs/Broker Example 1.pdf')

# # print the number of pages in pdf file
# print(len(reader.pages))

# # print the text of the first page
# print(reader.pages[0].extract_text())

from pdf2image import convert_from_path
import os

from PyPDF2 import PdfReader

def convert_pdf_to_images(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        return

    reader = PdfReader(pdf_path)

    page = reader.pages[0]
    count = 0

    print(reader, page)
    for pages_index in range(len(reader.pages)):
        for image_file_object in reader.pages[pages_index].images:
            with open('page_' + str(count) + ".jpg", "wb") as fp:
                fp.write(image_file_object.data)
                count += 1

    print("Conversion complete. Images saved in the current directory.")

    return count

            
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\muhammadghufran.ali\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

from PIL import Image

def perform_ocr_on_images(num_pages):

    combined_text = ""

    for i in range(num_pages):

        image_path = f'''page_{i}.jpg'''

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        combined_text += text + "\n"

        print(f'''Page {i + 1}:\n{text}\n''')
    
    with open("extracted_text.txt", "w") as f:

        f.write(combined_text)

    print("Extraction complete. Text saved to ‘extracted_text.txt’")


path = os.path.join(os.getcwd(), 'Automation Example Docs', "Broker Example 1.pdf")
count = convert_pdf_to_images(path)
perform_ocr_on_images(count)

# path = os.path.join(os.getcwd(), 'Automation Example Docs', "Broker Example 1.pdf")

# convert_pdf_to_images(path)