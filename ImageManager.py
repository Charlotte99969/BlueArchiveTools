import cv2
import pytesseract
import numpy as np

import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

class ImageManager:
    def __init__(self):
        self.total_progress = 0
        self.current_progress = 0
        self.processing_completed = False

    def extract_character_name(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 110
        top = 830
        right = 400
        bottom = 875
        cropped_image = image[top:bottom, left:right]
        # ImageManager.show_img(cropped_image)

        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        # '--psm 6' 表示單行文本
        config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ() --psm 6'
        character_name = pytesseract.image_to_string(gray_image, config=config).strip().replace('(', '_').replace(')', '')

        return character_name

    def extract_character_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 85
        top = 885
        right = 115
        bottom = 910
        cropped_image = image[top:bottom, left:right]

        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        # '--psm 6' 表示單行文本
        config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
        character_level = pytesseract.image_to_string(gray_image, config=config).strip()

        # print('character_level ' + str(character_level))
        # if(character_level != '85'):
        #     ImageManager.show_img(cropped_image, gray_image)

        return character_level

    def extract_character_unique_equipment_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1210
        top = 685
        right = 1245
        bottom = 710
        cropped_image = image[top:bottom, left:right]

        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        # '--psm 6' 表示單行文本
        config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
        character_unique_equipment_level = pytesseract.image_to_string(gray_image, config=config).strip()

        return character_unique_equipment_level

    def extract_character_bond_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 70
        top = 840
        right = 100
        bottom = 860
        cropped_image = image[top:bottom, left:right]

        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        # '--psm 6' 表示單行文本
        config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
        character_bond_level = pytesseract.image_to_string(gray_image, config=config).strip()

        return character_bond_level

    def extract_character_ex_skill_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1055
        top = 605
        right = 1120
        bottom = 630
        cropped_image = image[top:bottom, left:right]
        ex_skill_level = ImageManager.extract_character_skill_level(cropped_image)

        # EX 技能等級上限為 5
        if ex_skill_level == 10:
            ex_skill_level = 5

        return ex_skill_level

    def extract_character_normal_skill_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1220
        top = 605
        right = 1285
        bottom = 630
        cropped_image = image[top:bottom, left:right]

        return ImageManager.extract_character_skill_level(cropped_image)

    def extract_character_passive_skill_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1375
        top = 605
        right = 1440
        bottom = 630
        cropped_image = image[top:bottom, left:right]

        return ImageManager.extract_character_skill_level(cropped_image)

    def extract_character_sub_skill_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1535
        top = 605
        right = 1600
        bottom = 630
        cropped_image = image[top:bottom, left:right]

        return ImageManager.extract_character_skill_level(cropped_image)

    def extract_character_skill_level(cropped_image):
        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        # '--psm 6' 表示單行文本
        config = r'-c tessedit_char_whitelist=Lv.MmAXx1234567890 --psm 6'
        character_skill_level = pytesseract.image_to_string(gray_image, config=config).strip()
        # print(character_skill_level)
        # 移除Lv.
        character_skill_level = character_skill_level.replace('L', '').replace('v', '').replace('.', '').upper()

        # M 判斷常常出問題
        if 'M' in character_skill_level or 'A' in character_skill_level or 'X' in character_skill_level:
            return 10

        if character_skill_level == '':
            return 0

        return int(character_skill_level)

    def extract_character_attack_item_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1030
        top = 925
        right = 1055
        bottom = 945
        cropped_image = image[top:bottom, left:right]

        return ImageManager.extract_character_item_level(cropped_image)

    def extract_character_defense_item_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1170
        top = 925
        right = 1195
        bottom = 945
        cropped_image = image[top:bottom, left:right]

        return ImageManager.extract_character_item_level(cropped_image)

    def extract_character_support_item_level(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1310
        top = 925
        right = 1335
        bottom = 945
        cropped_image = image[top:bottom, left:right]

        return ImageManager.extract_character_item_level(cropped_image)

    def extract_character_item_level(cropped_image):
        # 將裁切後的圖片轉為灰度
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 使用Tesseract進行文字辨識
        # '--psm 6' 表示單行文本
        config = r'-c tessedit_char_whitelist=TSe12345678 --psm 6'
        character_item_level = pytesseract.image_to_string(gray_image, config=config).strip()

        #調整常見誤判
        #將S轉換為5 將e轉換為6 並將T移除
        character_item_level = character_item_level.replace('S', '5').replace('e', '6').replace('T', '')
        character_item_level = int(character_item_level) if character_item_level else 0
        if character_item_level > 70:
            character_item_level -= 70

        return character_item_level

    def extract_character_quantity(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 390
        top = 840
        right = 505
        bottom = 880
        cropped_image = image[top:bottom, left:right]

        #轉換為黑白
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        _, black_white_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

        # 查找白色区域
        contours, _ = cv2.findContours(black_white_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 绘制并标记星星
        star_count = 0
        for contour in contours:
            # 如果轮廓面积大于某个阈值，则认为这是一颗星星
            if cv2.contourArea(contour) > 150:
                # 绘制轮廓线
                # cv2.drawContours(cropped_image, [contour], -1, (0, 255, 0), 2)
                star_count += 1

        # cv2.imwrite('output_image.jpg', cropped_image)
        return star_count

    def extract_character_unique_equipment(image):
        # 裁切圖片 以下數值為 1920*1080
        left = 1545
        top = 760
        right = 1635
        bottom = 795
        cropped_image = image[top:bottom, left:right]

        #轉換為黑白
        gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # 定义要替换的颜色范围，这里以白色为例
        lower_white = np.array([230])
        upper_white = np.array([255])

        # 找到符合颜色范围的像素，并将它们标记为白色
        mask = cv2.inRange(gray_image, lower_white, upper_white)

        # 替换颜色，将掩码中的白色像素替换为黑色
        gray_image[mask > 0] = 0

        _, black_white_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
        # 查找白色区域
        contours, _ = cv2.findContours(black_white_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 绘制并标记星星
        star_count = 0
        for contour in contours:
            # 如果轮廓面积大于某个阈值，则认为这是一颗星星
            # print(cv2.contourArea(contour))
            if cv2.contourArea(contour) > 120:
                # 绘制轮廓线
                cv2.drawContours(cropped_image, [contour], -1, (0, 255, 0), 2)
                star_count += 1

        # cv2.imwrite('output_image.jpg', black_white_image)
        return star_count

    def show_img(original_image, converted_image = None):
        # 显示原始图像
        plt.subplot(121), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
        # 显示转换后的图像
        if (converted_image is None):
            converted_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        plt.subplot(122), plt.imshow(converted_image, cmap='gray'), plt.title('Converted Image')
        plt.show()
