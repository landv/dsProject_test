from SchoolDetailsGen import fetchSchoolDetails
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import utils

def fetchResultSubject(roll,schoolDetails,sDetails,result,overAll,
                       ScholasticAreasGrade,DisciplneGrade):
    elements = []
    styleSheet = getSampleStyleSheet()

    data1 = []

    data2 = []

    data3 = [
        ['SCHOLASTIC AREA', 'Term-1\n(100 Marks)', '', '', '', '',
         'Term-2\n(100 Marks)', '', '', '', '', 'OVERALL', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '',
            'Term-1(50 Marks)\n+\nTerm-2(50 Marks)', '', ''],
        ['Subjects', 'UT1', 'UT2', 'UT3', 'Half\nYearly', 'Total',
         'UT4', 'UT5', 'UT6', 'Annual\nExam', 'Total', 'Grand\nTotal',
         'Grade', 'Rank']]

    data41 = [['Overall Mark']]
    data42 = [['Percentage']]
    data43 = [['Grade']]
    data44 = [['Rank']]
    

    data51 = [['Co-Scholastic Areas\n(3 Points grading scale A,B,C)'],
              ['Activity', 'T1', 'T2']]

    data52 = [['Discipline\n(3 Points grading scale A,B,C)'],
              ['Activity', 'T1', 'T2']]
    
    data6=[['Attendance : 256/365','','Remarks : Qualified'],
           ['Class Teacher','Principal','Exam Incharge'],
           ['**Congratulation Promoted To Class XII','','Date : 10/07/2005'],
           ]

    getSchoolDetails(roll,schoolDetails,data1)
    getStudentDetails(sDetails,data2)
    resultExamWise(result, data3)
    getOverAll(overAll,data41,data42,data43,data44)
    CoScholasticGrade(ScholasticAreasGrade, data51)
    DiscplineGrade(DisciplneGrade, data52)

    t1 = Table(data1, colWidths=[80, 410, 80], 
               rowHeights=[40, None, None, None, None, None, None],
               style=[
        #('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('SPAN', (0, 0), (0, 3)),
        ('SPAN', (2, 0), (2, 3)),
        ('SPAN', (0, 4), (2, 4)),
        ('SPAN', (0, 5), (2, 5)),
        ('SPAN', (0, 6), (2, 6)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (2, 0), 16),
    ])

    t2 = Table(data2,
               colWidths=[100, 280, 95, 95],
               style=[
                   ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                   ('SPAN', (1, 4), (3, 4)),
               ])

    t3 = Table(data3, colWidths=[110, 30, 30, 30, 40, 40,
                                 30, 30, 30, 40, 40, 40, 40, 40],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (0, 0), (0, 1)),
        ('SPAN', (1, 0), (5, 1)),
        ('SPAN', (6, 0), (10, 1)),
        ('SPAN', (11, 0), (13, 0)),
        ('SPAN', (11, 1), (13, 1))
    ])

    t41 = Table(data41,colWidths=[70,60],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ],)
    t42 = Table(data42,colWidths=[70,60],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ],)
    t43 = Table(data43,colWidths=[70,33],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ],)
    t44 = Table(data44,colWidths=[70,32],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ],)
               
    
    data4=[[t41,t42,t43,t44]]
    
    t4 = Table(data4,colWidths=[165,165,120,120],
               style=[
        #('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (2, 0), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (3, 0), (3, 0), 18),
        ],)

    t51 = Table(data51, colWidths=[185, 50, 50],
                style=[
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('SPAN', (0, 0), (2, 0)),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
    ])

    t52 = Table(data52, colWidths=[185, 50, 50],
                style=[
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('SPAN', (0, 0), (2, 0)),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
    ])

    data5 = [[t51, t52]]

    t5 = Table(data5,colWidths=[285,285],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ],)
    
    t6=Table(data6,colWidths=[190,190,190],
        style=[
        ('GRID', (0, 0), (0, 0), 0.5, colors.grey),
        ('GRID', (2, 0), (2, 0), 0.5, colors.grey),
        ('SPAN', (0, 2), (1, 2)),
        ('LINEABOVE', (1, 0), (1, 0), 0.5, colors.grey),
        ('GRID', (0, 1), (0, 1), 0.5, colors.grey),
        ('LINEBELOW', (1, 1), (1, 1), 0.5, colors.grey),
        ('GRID', (2, 1), (2, 1), 0.5, colors.grey),
        ('TOPPADDING', (0, 1), (0, 2), 55),
        ('TOPPADDING', (1, 1), (1, 2), 55),
        ('TOPPADDING', (2, 1), (2, 2), 55),
        ('TOPPADDING', (0, 2), (2, 2), 16),
        ('VALIGN', (0, 1), (2, 1), 'MIDDLE'),
        ('ALIGN', (0, 1), (2, 1), 'CENTER'),
        ('VALIGN', (1, 2), (1, 2), 'MIDDLE'),
        ('ALIGN', (2, 2), (2, 2), 'CENTER'),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2,0), 'BOTTOM')
        ])

    data = [
        [t1],
        [t2],
        [t3],
        [t4],
        [t5],
        [t6]
    ]

    t = Table(data,
              style=[
                  #('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                  ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
              ])

    elements.append(t)
    fname = roll
    print(str(fname)+".pdf")
    doc = SimpleDocTemplate('./Files/ResultPdf/'+str(fname)+".pdf",
                            bottomMargin=5, topMargin=5,
                            rightMargin=10, leftMargin=10,)
    doc.build(elements)

def getSchoolDetails(roll,schooldetails,data1):
    
    img = utils.ImageReader('./Files/StudentPics/'
                            +str(roll)+'.jpg')
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    width=2.5*cm
    #height=width * aspect
    height=3*cm

    StudentPic = Image('./Files/StudentPics/'+str(roll)+'.jpg'
                       ,width,height)
    
    
    logo = Image('./Files/logo.png')
    logo.drawHeight = .75*inch*logo.drawHeight / logo.drawWidth
    logo.drawWidth = .90*inch

    org = schooldetails.loc[0].to_string(index=False)
    affliation = schooldetails.loc[1].to_string(index=False)
    address = schooldetails.loc[2].to_string(index=False)
    ph_email = schooldetails.loc[3].to_string(index=False)
    report_card = schooldetails.loc[4].to_string(index=False)
    cls= schooldetails.loc[5].to_string(index=False)
    acad_session= schooldetails.loc[6].to_string(index=False)

    data1.append([logo,org,StudentPic])
    data1.append(['',affliation,''])
    data1.append(['',address,''])
    data1.append(['',ph_email,''])
    data1.append([report_card])
    data1.append([cls])
    data1.append([acad_session])

def getStudentDetails(sdetails,data2):
    
    colroll = sdetails.columns[0]
    colano = sdetails.columns[1]
    colname = sdetails.columns[2]
    coldob = sdetails.columns[3]
    colcls = sdetails.columns[4]
    colsection = sdetails.columns[5]
    colmname= sdetails.columns[6]
    colfname= sdetails.columns[7]
    coladdress= sdetails.columns[8]

    roll = sdetails[sdetails.columns[0]].to_string(index=False)
    ano = sdetails[sdetails.columns[1]].to_string(index=False)
    name = sdetails[sdetails.columns[2]].to_string(index=False)
    dob = sdetails[sdetails.columns[3]].to_string(index=False)
    cls = sdetails[sdetails.columns[4]].to_string(index=False)
    section = sdetails[sdetails.columns[5]].to_string(index=False)
    mname= sdetails[sdetails.columns[6]].to_string(index=False)
    fname= sdetails[sdetails.columns[7]].to_string(index=False)
    address= sdetails[sdetails.columns[8]].to_string(index=False)

    data2.append([colname,name,colroll,roll])
    data2.append([colfname,fname,colano,ano])
    data2.append([colmname,mname])
    data2.append([coldob,dob])
    data2.append([coladdress,address])


def resultExamWise(result, data3):
    
    s1 = result.columns[1]
    s2 = result.columns[2]
    s3 = result.columns[3]
    s4 = result.columns[4]
    s5 = result.columns[5]
    s6 = result.columns[6]

    sub1 = []
    sub2 = []
    sub3 = []
    sub4 = []
    sub5 = []
    sub6 = []

    sub1 = result[s1].tolist().copy()
    sub1.insert(0, result.columns[1])
    sub2 = result[s2].tolist().copy()
    sub2.insert(0, result.columns[2])
    sub3 = result[s3].tolist().copy()
    sub3.insert(0, result.columns[3])
    sub4 = result[s4].tolist().copy()
    sub4.insert(0, result.columns[4])
    sub5 = result[s5].tolist().copy()
    sub5.insert(0, result.columns[5])
    sub6 = result[s6].tolist().copy()
    sub6.insert(0, result.columns[6])
    

    data3.append(round(num,2) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub1)
    data3.append(round(num,2) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub2)
    data3.append(round(num,2) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub3)
    data3.append(round(num,2) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub4)
    data3.append(round(num,2) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub5)
    data3.append(round(num,2) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub6)
   
   


def getOverAll(overAll,data41,data42,data43,data44):
    overall_col=overAll.columns[7]
    over_All=overAll[overall_col].tolist().copy()
    percentage=round(over_All[0]*100/600,2)
    data41[0].append(str(round(over_All[0],2))+"/600")
    data42[0].append(percentage)
    data43[0].append(over_All[1])
    data44[0].append(over_All[2])
    
    

def CoScholasticGrade(ScholasticAreasGrade, data51):
    c1 = ScholasticAreasGrade.columns[1]
    c2 = ScholasticAreasGrade.columns[2]
    c3 = ScholasticAreasGrade.columns[3]
    c4 = ScholasticAreasGrade.columns[4]
    c5 = ScholasticAreasGrade.columns[5]
    c6 = ScholasticAreasGrade.columns[6]
    c7 = ScholasticAreasGrade.columns[7]
    c8 = ScholasticAreasGrade.columns[8]

    cosc1 = []
    cosc2 = []
    cosc3 = []
    cosc4 = []
    cosc5 = []
    cosc6 = []
    cosc7 = []
    cosc8 = []

    cosc1 = ScholasticAreasGrade[c1].tolist().copy()
    cosc1.insert(0, ScholasticAreasGrade.columns[1])
    cosc2 = ScholasticAreasGrade[c2].tolist().copy()
    cosc2.insert(0, ScholasticAreasGrade.columns[2])
    cosc3 = ScholasticAreasGrade[c3].tolist().copy()
    cosc3.insert(0, ScholasticAreasGrade.columns[3])
    cosc4 = ScholasticAreasGrade[c4].tolist().copy()
    cosc4.insert(0, ScholasticAreasGrade.columns[4])
    cosc5 = ScholasticAreasGrade[c5].tolist().copy()
    cosc5.insert(0, ScholasticAreasGrade.columns[5])
    cosc6 = ScholasticAreasGrade[c6].tolist().copy()
    cosc6.insert(0, ScholasticAreasGrade.columns[6])
    cosc7 = ScholasticAreasGrade[c7].tolist().copy()
    cosc7.insert(0, ScholasticAreasGrade.columns[7])
    cosc8 = ScholasticAreasGrade[c8].tolist().copy()
    cosc8.insert(0, ScholasticAreasGrade.columns[8])

    data51.append(cosc1)
    data51.append(cosc2)
    data51.append(cosc3)
    data51.append(cosc4)
    data51.append(cosc5)
    data51.append(cosc6)
    data51.append(cosc7)
    data51.append(cosc8)


def DiscplineGrade(DisciplneGrade, data52):

    d1 = DisciplneGrade.columns[1]
    d2 = DisciplneGrade.columns[2]
    d3 = DisciplneGrade.columns[3]
    d4 = DisciplneGrade.columns[4]
    d5 = DisciplneGrade.columns[5]
    d6 = DisciplneGrade.columns[6]
    d7 = DisciplneGrade.columns[7]
    d7 = DisciplneGrade.columns[8]

    disc1 = []
    disc2 = []
    disc3 = []
    disc4 = []
    disc5 = []
    disc6 = []
    disc7 = []
    disc8 = []

    disc1 = DisciplneGrade[d1].tolist().copy()
    disc1.insert(0, DisciplneGrade.columns[1])
    disc2 = DisciplneGrade[d2].tolist().copy()
    disc2.insert(0, DisciplneGrade.columns[2])
    disc3 = DisciplneGrade[d3].tolist().copy()
    disc3.insert(0, DisciplneGrade.columns[3])
    disc4 = DisciplneGrade[d4].tolist().copy()
    disc4.insert(0, DisciplneGrade.columns[4])
    disc5 = DisciplneGrade[d5].tolist().copy()
    disc5.insert(0, DisciplneGrade.columns[5])
    disc6 = DisciplneGrade[d6].tolist().copy()
    disc6.insert(0, DisciplneGrade.columns[6])
    disc7 = DisciplneGrade[d7].tolist().copy()
    disc7.insert(0, DisciplneGrade.columns[7])
    disc8 = DisciplneGrade[d7].tolist().copy()
    disc8.insert(0, DisciplneGrade.columns[8])

    data52.append(disc1)
    data52.append(disc2)
    data52.append(disc3)
    data52.append(disc4)
    data52.append(disc5)
    data52.append(disc6)
    data52.append(disc7)
    data52.append(disc8)
