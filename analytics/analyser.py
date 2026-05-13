class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self): print("Not implemented use a child class")
    def print_results(self):
        for k, v in self.result.items(): print(f"{k}: {v}")
    def __str__(self): return f"DataAnalyser: {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def analyse(self):
        gpas = [float(s['GPA']) for s in self.students if s.get('GPA')]
        high_perf = list(filter(lambda x: x >= 3.5, gpas))
        if gpas:
            self.result = {
                "total_students": len(gpas),
                "average_gpa": round(sum(gpas)/len(gpas), 2),
                "max_gpa": max(gpas), "min_gpa": min(gpas),
                "high_performers": len(high_perf)
            }
    def print_results(self):
        print("\nGPA ANALYSIS REPORT\n====== =======")
        super().print_results()
        print("===============")