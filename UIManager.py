import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from time import sleep

from VideoManager import VideoManager
from ImageManager import ImageManager

class UIManager:
    def __init__(self, root):
        self.root = root
        self.video_manager = VideoManager()
        self.image_manager = ImageManager()
        self.root.title("蔚藍檔案腳色練度")

        # 創建UI元件
        self.select_button = tk.Button(root, text="選擇影片文件", command=self.choose_video_file)
        self.select_button.pack(pady=10)

        self.process_button = tk.Button(root, text="處理影片", command=self.start_processing)
        self.process_button.pack(pady=10)

        # 初始化進度條
        self.progress = ttk.Progressbar(root, orient="horizontal", mode="determinate")
        self.progress.pack(fill="x")

    def choose_video_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if file_path:
            self.video_manager.set_video_file(file_path)

    def start_processing(self):
        if self.video_manager.video_file_path:
            # 使用多執行緒處理影格切分和圖片過濾
            processing_thread = threading.Thread(target=self.video_manager.process_video_frames)
            processing_thread.start()
            
            # 使用多執行緒更新共用進度條
            update_progress_thread = threading.Thread(target=self.update_progress, args=(self.video_manager,))
            update_progress_thread.start()

    def update_progress(self, manager):
        while True:
            if manager.processing_completed:
                # print("Processing completed")
                break

            if manager.total_progress > 0:
                progress_value = (manager.current_progress / manager.total_progress) * 100
                self.progress["value"] = progress_value
                # print(f"Progress: {progress_value:.2f}%")
            
            sleep(0.1)

    def run(self):
        self.root.mainloop()


           
