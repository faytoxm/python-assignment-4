import json
class ResultSaver:
    def __init__(self, data, outfile):
        self.data, self.outfile = data, outfile
    def save_json(self):
        with open(self.outfile, 'w') as f: json.dump(self.data, f, indent=4)