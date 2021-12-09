# from reportlab.lib.pagesizes import letter, A4
# PAGE_WIDTH, PAGE_HEIGHT = A4
from reportlab.lib.units import inch, mm

PAGE_WIDTH, PAGE_HEIGHT = 140*mm, 215*mm
page_size = (PAGE_WIDTH, PAGE_HEIGHT)
TOP_MARGIN, BOTTOM_MARGIN = 0.5*inch, 0.5*inch
LEFT_MARGIN, RIGHT_MARGIN = 0.5*inch, 0.5*inch

export_name_url = 'directory_final.pdf'

PAGE_FRAME_WIDTH = PAGE_WIDTH - (LEFT_MARGIN + RIGHT_MARGIN)
PAGE_FRAME_HEIGHT = PAGE_HEIGHT - (TOP_MARGIN + BOTTOM_MARGIN)

db_url = 'sqlite.db'

frame_boundary = 0