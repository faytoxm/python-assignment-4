import os
class FileManager:
    def __init__(self, filename): self.filename = filename
    def check_file(self): return os.path.exists(self.filename)
    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder): os.makedirs(folder)