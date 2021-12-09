import pandas as pd 

def fetchAllStudentDetails():
    file = ('./Files/Result.xlsx')
    sData = pd.read_excel(file, sheet_name=['StudentDetails'])
    return sData


def fetchStudentDetails(roll):
    file = ('./Files/Result.xlsx')
    resultData = pd.read_excel(file,
                               sheet_name=['StudentDetails'])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    return sRecord