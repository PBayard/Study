import xlwings as xw
import datetime as dt

# wb = xw.Book()  # this will create a new workbook (this will open Excel)
# wb = xw.Book('Book2.xlsx')  # connect to an existing file in the current working directory
wb = xw.Book(r'C:\Temp\myproject\PythonTest.xlsm')  # on Windows: use raw strings to escape backslashes (this will open Excel)
sht = wb.sheets['Sheet1']  # Instantiate a sheet object

# Active objects
app = xw.apps.active
print('Active App ', app)
# wb = xw.books.active  # in active app
wb = app.books.active  # in specific app
print('Active Book ', wb)
# sht = xw.sheets.active  # in active book
sht = wb.sheets.active  # in specific book
print('Active Sheet ', sht)

# A Range can be instantiated with A1 notation, a tuple of Excel’s 1-based indices, a named range or two Range objects
xw.Range('E1').value = 'E1'
xw.Range('G1:G3').value = 'G1:G3'
tst = xw.Range('E2:F3')
for x in tst:
    x.value = 'E2:F3'
xw.Range((1,8)).value = "'1:8"
xw.Range((1,9), (3,9)).value = "'1:9 to 3:9"
xw.Range('Namedrange').value = 'Namedrange'
xw.Range(xw.Range('H1'), xw.Range('H2')).value = 'H1:H2'

# Round brackets follow Excel’s behavior (i.e. 1-based indexing), while square brackets use Python’s
# 0-based indexing/slicing. As an example, the following expressions all reference the same range
xw.apps[0].books[0].sheets[0].range('J1').value = 1
xw.apps(1).books(1).sheets(1).range('J2').value = 1
xw.apps[0].books['PythonTest.xlsm'].sheets['Sheet1'].range('J3').value = 1
xw.apps(1).books('PythonTest.xlsm').sheets('Sheet1').range('J4').value = 1

# Range indexing & slicing
print('********* Index / Slice *************')
rng = wb.sheets[0].range('A1:D5')
print(rng[0, 0])
print(rng[0, 1])
print(rng[1])
print(rng[:, :]) # returns A1:D5 (all rows , all col)
print(rng[1:3, 1:3]) # returns B2:C3 (rows 2 to 3 - 1, col B to D - 1)
print(rng[1:4, :2]) # returns A2:B4 (rows 2 to 5 - 1, col A to C - 1)
print(rng[:4, :2])
print (sht['A1'])
print (sht['A1:B5'])
print (sht[0,1])
print (sht[:10, :10]) # returns A1:J10 (rows 1 to 11 -1, col A to K -1)

# Reading / Writing values
print(sht.range('A3').value is None)
sht.range('A5').value = dt.datetime(2017, 10, 2)

# Lists
print('********* List *************')
# 1st list: Ranges that represent rows or columns in Excel are returned as simple lists, which means that once they are in
# Python, you’ve lost the information about the orientation. Point B) shows you how to preserve this info
sht.range('M1').value = [[1],[2],[3],[4],[5]]   # Column orientation (nested list)
print(sht.range('M1:M5').value, ' N.B.: lost nested list')
sht.range('N1').value = [1, 2, 3, 4, 5]         # Row orientation
print(sht.range('N1:R1').value, ' N.B.: lost nested list')
sht.range('S1').options(transpose=True).value = [1,2,3,4] # write a list in column orientation
# force single cell to arrive as list
print(sht.range('A1').options(ndim=1).value)

# 2nd list: If the row or column orientation has to be preserved, set ndim in the Range options. This will return
# the Ranges as nested lists (ndmin 2 = 2d lists; 1 = 1st list)
print(sht.range('M1:M5').options(ndim=2).value, ' N.B.: preserved nested list')
print(sht.range('N1:R1').options(ndim=2).value, ' N.B.: preserved nested list')

# Reading/writing values to/from ranges
sht.range('A1').value = 'Foo 1'
print(sht.range('A1').value)
# Range expanding
sht.range('A2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
print(sht.range((1,1),(3,3)).value, ' Read value back')
# Call active sheet directly. xw.Range only when interacting otherwise always define book and sheet
print('Active Sheet Range A1 value', xw.Range('A1').value)

# Expand
print('********* Expand *************')
sht.range('A9:B9').value = None # Otherwise example does not work
print(sht.range('A1').expand().value, ' Expand value')  # Expand till empty cell : row and col
sht.range('A7').value = [[1,2], [3,4]]
rng1 = sht.range('A7').expand('table')  # or just .expand()
rng2 = sht.range('A7').options(expand='table') # table' expands to 'down' (col) and 'right' (row)
print(rng1.value)
print(rng2.value)
sht.range('A9').value = [5, 6]
print(rng1.value)
print(rng2.value, ' with options(expand=table)')