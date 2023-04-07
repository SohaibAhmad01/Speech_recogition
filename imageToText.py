import pytesseract
from PIL import Image

# Set Tesseract path (Windows example)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR"

# Open image using PIL
image = Image.open('12.png')

# Extract text from image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
