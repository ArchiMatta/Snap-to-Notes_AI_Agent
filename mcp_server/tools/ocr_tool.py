from PIL import Image
import pytesseract
import os

# If tesseract is not on PATH, set path here (Windows default install)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRTool:
    """
    OCR tool to extract text from a screenshot/image.
    """

    def __init__(self, tesseract_cmd: str = None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def run(self, image_path: str) -> str:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"OCRTool Error: File not found: {image_path}")

        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
