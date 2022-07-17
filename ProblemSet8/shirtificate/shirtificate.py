from PIL import Image, ImageOps
from fpdf import FPDF

with Image.open("shirtificate.png") as shirt:
    pdf = FPDF(orientation = 'portrait', format = 'A4')
    pdf.set_font("Times", size = 30)
    pdf.set_text_color(255,255,255)
    pdf.set_draw_color
    pdf.add_page()
    pdf.image(shirt, x = 0, y = 50)
    pdf.text(100,100,txt = input("What is your name"))
    pdf.output("myshirt.pdf")

print("Hello world")