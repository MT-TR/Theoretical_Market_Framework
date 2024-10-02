from PIL import Image
import pytesseract

# Load the image from the file
image_path = '/mnt/data/image.png'
image = Image.open(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

extracted_text
