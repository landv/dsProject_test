import pandas as pd

def fetchCoScholasticAreasGrade(roll):

    file = ('./Files/Result.xlsx')
    resultData = pd.read_excel(file, sheet_name=[
        'T1CoScholasticAreas',
        'T2CoScholasticAreas', ])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    return sRecord
