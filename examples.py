""" Examples """

from src.pdf_watermark import PDF

p = PDF('C://tmp/a.pdf', 'C://tmp/o.pdf', 'C://tmp/img.jpg')
p.watermark_all_pages()

p = PDF("C://tmp/a.pdf", "C://tmp/w.pdf", "C://tmp/img.jpg")
pdf.watermark_all_pages()
