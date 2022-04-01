# read.py
# The scripts reads an excel file content

import xlrd

FILE_REFERENCE =".\projectplan.xlsx"

# File location
loc = (FILE_REFERENCE)

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0,0))

