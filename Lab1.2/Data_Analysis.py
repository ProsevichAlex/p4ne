from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


def getvalue(x):
    return x.value

colonka_a = sheet['A'][1:]
colonka_c = sheet['C'][1:]
colonka_d = sheet['D'][1:]

val_a = list(map(getvalue, colonka_a))
val_c = list(map(getvalue, colonka_c))
val_d = list(map(getvalue, colonka_d))

pyplot.plot(val_a, val_c, label="Метка1")
pyplot.plot(val_a, val_d, label="Метка2")
pyplot.show()