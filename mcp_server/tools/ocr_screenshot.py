import pytesseract
from PIL import Image

class OcrScreenshot:
    def run(self, image_path):
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return {"extracted_text": text}
