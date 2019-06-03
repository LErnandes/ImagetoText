import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
frase = pytesseract.image_to_string(Image.open('a.jpg'), lang='por')
print(frase)
