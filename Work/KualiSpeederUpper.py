import openpyxl

if __name__ == '__main__':
    file_path = "2020Kuali-M33.xlsx"
    sheet_old = openpyxl.load_workbook(file_path)
    inactive_sheet = sheet_old
    sheet_old = sheet_old.active

    sheet_new = []

    tuples = tuple(sheet_old.rows)
    for t1 in range(len(tuples)):
        found = False
        for t2 in range(len(tuples)):
            if tuples[t1][0].value == tuples[t2][1].value:
                found = True
                # print(tuples[t1][0].value + " " + tuples[t2][1].value)
                print(tuples[t2][3].value + " " + tuples[t2][2].value)
        if not found:
            print("-")
