import pandas as pd 

def fetchSchoolDetails():
    file = ('./Files/Result.xlsx')
    sData = pd.read_excel(file, sheet_name=['SchoolDetails'])
    for sd in sData:
        sdata = sData[sd]
    return sdata