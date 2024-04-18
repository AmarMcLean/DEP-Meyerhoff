import openpyxl

if __name__ == '__main__':
    file_path = "2021Kuali-MegaFile-M33-35.xlsx"
    sheet_old = openpyxl.load_workbook(file_path)
    sheet_old = sheet_old.active

    tuples = tuple(sheet_old.rows)
    for t1 in range(len(tuples)):
        found = False
        if tuples[t1][0].value is not None:
            for t2 in range(len(tuples)):
                if tuples[t1][0].value == tuples[t2][1].value:
                    found = True
                     # print(tuples[t1][0].value + " " + tuples[t2][1].value)
                    print(tuples[t2][3].value + " " + tuples[t2][2].value)
            if not found:
                print("-")
