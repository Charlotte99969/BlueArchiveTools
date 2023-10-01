import cv2
import os

from ImageManager import ImageManager
from DataManager import DataManager

class VideoManager:
    def __init__(self):
        self.video_file_path = None
        self.output_directory = "characters"  # 保存影格的目錄
        self.total_progress = 0
        self.current_progress = 0
        self.processing_completed = False

    def set_video_file(self, file_path):
        self.video_file_path = file_path

    def process_video_frames(self):
        if self.video_file_path:
            # 初始化影格保存目錄
            DataManager.initialize_output_directory(self.output_directory)

            cap = cv2.VideoCapture(self.video_file_path)
            self.total_progress = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 影片的總幀數

            characters = []

            while cap.isOpened():
                ret, frame = cap.read()

                if not ret:
                    break

                character_name = ImageManager.extract_character_name(frame)  # 提取腳色名稱的方法需自行實現
                # print(character_name)
                if (character_name not in characters):
                    characters.append(character_name)
                    frame_filename = os.path.join(self.output_directory, f"{character_name}.jpg")
                    cv2.imwrite(frame_filename, frame)

                self.current_progress += 1

            cap.release()
            self.processing_completed = True
