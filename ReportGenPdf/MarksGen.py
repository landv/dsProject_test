import pandas as pd
from CoScholasticAreasGradeGen import fetchCoScholasticAreasGrade
from DisciplineGradeGen import fetchDisciplneGrade
from BuildResult import fetchResultSubject
from StudentsDeatailsGen import fetchAllStudentDetails,fetchStudentDetails
from SchoolDetailsGen import fetchSchoolDetails

def fetchResult(roll):
    file = ('./Files/Result.xlsx')
    resultData = pd.read_excel(file, sheet_name=['UT1', 'UT2', 'UT3',
                                                 'HY', 'T1',
                                                 'UT4', 'UT5', 'UT6',
                                                 'Y', 'T2',
                                                 'GT', 'Grade',
                                                 'Rank'])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    return sRecord

def fetchOverAll(roll):
    file = ('./Files/Result.xlsx')
    resultData = pd.read_excel(file, sheet_name=['GT', 'Grade',
                                                 'Rank'])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    return sRecord

def MarksGenAll():
    sData = fetchAllStudentDetails()
    rolColumnName = sData['StudentDetails'].columns[0]
    rollColData = sData['StudentDetails'][rolColumnName]
    for roll in rollColData:
        schoolDetails=fetchSchoolDetails()
        sDetails=fetchStudentDetails(roll)
        result = fetchResult(roll)
        overAll=fetchOverAll(roll)
        Cograde= fetchCoScholasticAreasGrade(roll)
        DiscGrade= fetchDisciplneGrade(roll)
        fetchResultSubject(roll, schoolDetails, sDetails, 
                           result, overAll, Cograde, DiscGrade)
