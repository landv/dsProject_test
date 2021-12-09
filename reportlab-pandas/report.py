import requests
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Paragraph
from reportlab.platypus import TableStyle, Image, Flowable, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet

## Separator line
class MCLine(Flowable):

    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def __repr__(self):
        return "Line(w=%s)" % self.width

    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)


def createPdf(products):

    # File configure
    pdf_file = "report.pdf"
    pdf = SimpleDocTemplate(pdf_file, pagesize=A4)

    # Elements list
    elements = []

    # Title text style
    title_style = getSampleStyleSheet()["Title"]
    title_style.fontSize = 28
    title_style.spaceAfter = 50
    elements.append(Paragraph('ORDER #157', style=title_style))

    # Categories text style
    category_style = getSampleStyleSheet()["Normal"]
    category_style.fontSize = 12
    category_style.spaceBefore = 50
    category_style.spaceAfter = 10
    category_style.alignment = 0

    # Product text style
    producto_style = getSampleStyleSheet()["Normal"]
    producto_style.fontSize = 10
    producto_style.spaceBefore = 20
    producto_style.spaceAfter = 10
    producto_style.alignment = 1

    # Iterate categories
    categories = products['category'].unique()

    count = 1

    for category in categories:

        # Add category
        elements.append(Paragraph(category.upper(), style=category_style))
        count += 0.5

        # Add horizontal line
        elements.append(MCLine(440))

        # Products of current category
        prods = products[products['category'] == category]

        # Iterate products
        for id, prod in prods.iterrows():

            # Add product name
            elements.append(Paragraph(prod['name'], style=producto_style))

            # Add product detail
            table = createProductTable(image=prod['image'], code=prod['id'], price=prod['price'], quantity=prod['quantity'])
            elements.append(table)

            count += 1

            if count >= 4:
                elements.append(PageBreak())
                count = 0

    # Add space
    space = Spacer(width=0, height=2 * cm)
    elements.append(space)

    # Subtotal cost
    subtotal = (products['price'] * products['quantity']).sum()

    # Add total table
    table = createTotalTable(subtotal)
    elements.append(table)

    # Generate pdf
    pdf.build(elements)


def createTotalTable( subtotal):

    # calcule subtotal with tax
    tax = 12
    t_val = subtotal * (tax/100)
    subtotal2 = subtotal + t_val

    # calcule final prince with discount
    dis = 10
    d_val = subtotal2 * (dis/100)
    final = subtotal2 - d_val

    # Order data in table
    data = [['Subtotal1', '{:.2f}'.format(float(subtotal))],
            ['TAX', '{:.2f}'.format(float(t_val))],
            ['Subtotal2', '{:.2f}'.format(float(subtotal2))],
            ['Disc', '{:.2f}'.format(float(d_val))],
            ['FINAL PRICE', '${:.2f}'.format(float(final))]]

    # Add data to table
    table = Table(data, colWidths=[300, 100], rowHeights=15)

    # Table style
    style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), "CENTER"),
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 4), (-1, -1), colors.black),
        ('TEXTCOLOR', (0, 4), (-1, -1), colors.white)
    ])
    table.setStyle(style)

    # Return table
    return table


def createProductTable(image, code, price, quantity):

    # Read image from url
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    response = requests.get(image, headers=headers)

    # Resize image dimentions
    a = Image(BytesIO(response.content))
    w_aux = a.imageWidth
    h_aux = a.imageHeight

    if w_aux >= h_aux:
        w_1 = 4 * cm
        h_1 = w_1 * (h_aux /w_aux )
    else:
        h_1 = 4 * cm
        w_1 = h_1 * (w_aux /h_aux )

    imageDim = 4 * cm
    rowDim = imageDim / 4

    a.drawHeight = h_1
    a.drawWidth = w_1

    # Total product price
    total = int(quantity) * float(price)

    # Order data in table
    data = [['', 'CODE', code],
            ['', 'QUANTITY', quantity],
            ['', 'UNIT PRECE', '${:.2f}'.format(float(price))],
            [a, 'TOTAL PRICE', '${:.2f}'.format(float(total))]]

    # Add data to table
    table = Table(data, colWidths=[imageDim, 100, 100], rowHeights=rowDim)

    # Table style
    style = TableStyle([
        ('GRID', (1, 0), (-1, -1), 0.5, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('ALIGN', (0, 0), (-1, -1), "CENTER"),
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('VALIGN', (1, 0), (-1, -1), 'MIDDLE')
    ])
    table.setStyle(style)


    # Return table
    return table