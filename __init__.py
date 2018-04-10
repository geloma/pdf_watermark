from src.pdf_watermark import PDF

""" Example """	
p = PDF('C://tmp/a.pdf', 'C://tmp/o.pdf', 'C://tmp/img.jpg')
p.watermark_all_pages()

