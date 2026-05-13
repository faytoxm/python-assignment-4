from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser

def main():
    filename = "students.csv"
    fm = FileManager(filename)
    if not fm.check_file():
        print(f"Error: {filename} not found!")
        return
    fm.create_output_folder()

    dl = DataLoader(filename)
    dl.load()

    # --- DEMONSTRATION OF POLYMORPHISM ---
    print("--- Polymorphism Demo ---")
    analysers = [GpaAnalyser(dl.students), GpaAnalyser(dl.students[:5])]
    for a in analysers:
        a.analyse()
        a.print_results()
    print("--------------------------\n")

    # --- DEMONSTRATION OF ASSOCIATION ---
    gpa_an = GpaAnalyser(dl.students)
    gpa_an.analyse()
    saver = ResultSaver(gpa_an.result, "output/result.json")
    report = Report(gpa_an, saver)
    report.generate()

if __name__ == "__main__":
    main()
