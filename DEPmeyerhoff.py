# Meyerhoff Scholars Program Data Entry Portal
# Authored by Amar McLean; SC04296
import openpyxl


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Excel:
    def __init__(self, file_path):
        self.path = file_path
        self.variables = []
        self.cohorts = []
        self.first_name = []
        self.last_name = []

        # Opens the Excel Sheet
        sheet = openpyxl.load_workbook(file_path)
        self.sheet = sheet.active

        # Puts all the variables (Everything in first row) into an array
        for x in range(self.sheet.max_column):
            self.variables.append((self.sheet.cell(row=1, column=x+1)).value)

        # Puts all the cohorts into an array
        for x in range(len(self.variables)):
            if self.variables[x].lower() == 'cohort':
                for y in range(self.sheet.max_row):
                    self.cohorts.append((self.sheet.cell(row=y+2, column=x+1)).value)

        # Puts all the last names into an array
        for x in range(len(self.variables)):
            if self.variables[x].lower() == 'last name':
                for y in range(self.sheet.max_row):
                    self.last_name.append((self.sheet.cell(row=y+2, column=x+1)).value)

        # Puts all the first names into an array
        for x in range(len(self.variables)):
            if self.variables[x].lower() == 'first name':
                for y in range(self.sheet.max_row):
                    self.first_name.append((self.sheet.cell(row=y+2, column=x+1)).value)

    def add_cohort(self):
        user_input = input("Would you like to add to an existing cohort(y/n)? ")
        if user_input.lower() == 'y':
            first_name = input("What is their first name? ").lower()
            last_name = input("What is their last name? ").lower()
            cohort = input("What is their cohort? ").lower()
            for x in range(len(self.cohorts)):
                if (first_name == self.first_name[x].lower()) & (last_name == self.last_name[x].lower()) & (
                        cohort == self.cohorts[x]):
                    print("Yippee")

    def edit_cohort(self):
        print(f'{self.path}')

    def search_cohort(self):
        print(f'{self.path}')

    def __del__(self):
        # self.sheet.close()
        print('DONE')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    excel_sheet = Excel('big_cheese.xlsx')
    excel_sheet.add_cohort()
