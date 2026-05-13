import csv, sys
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
    def load(self):
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                self.students = list(csv.DictReader(f))
        except Exception as e:
            print(f"Error: {e}"); sys.exit()