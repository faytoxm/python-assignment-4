from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser

def main():
    filename = "students.csv"
    fm = FileManager(filename)
    if not fm.check_file(): return
    fm.create_output_folder()

    dl = DataLoader(filename)
    dl.load()

    # Polymorphism demo
    analysers = [GpaAnalyser(dl.students), GpaAnalyser(dl.students[:5])]
    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()

    # Association
    gpa_an = GpaAnalyser(dl.students)
    report = Report(gpa_an, ResultSaver(gpa_an.result, "output/result.json"))
    report.generate()

if __name__ == "__main__":
    main()