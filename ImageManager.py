import cv2
import pytesseract

from skimage.metrics import structural_similarity as ssim

class ImageManager:
    def __init__(self):
        self.total_progress = 0
        self.current_progress = 0
        self.processing_completed = False

    def extract_character_name(image):
        # 裁切圖片，這裡使用相對位置
        height, width, _ = image.shape
        left = int(0.0573 * width)
        top = int(0.764 * height)
        right = int(0.2005 * width)
        bottom = int(0.810 * height)
        cropped_image = image[top:bottom, left:right]

        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ() --psm 6'
        character_name = pytesseract.image_to_string(gray_image, config=config).strip()  # '--psm 6' 表示單行文本
        if character_name.count("(") == 1 and character_name.count(")") == 0:
            character_name += ')'

        return character_name  # 去除前後空格