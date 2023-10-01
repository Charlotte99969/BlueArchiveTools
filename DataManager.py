import os
import shutil

class DataManager:
    def initialize_output_directory(directory):
        # 刪除整個資料夾並重新創建它
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)