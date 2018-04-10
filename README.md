# pdf_password
	Using PyPdf to overlay image on pdf
	Requirements:
	 pip install fpdf Pillow pypdf
	
	Examples
	* Specific page, the pages begin at zero
	p = PDF("C://tmp/a.pdf", "C://tmp/w.pdf", "C://tmp/img.jpg")
	p.watermark_page(3)

	* All pages
	p = PDF("C://tmp/a.pdf", "C://tmp/w.pdf", "C://tmp/img.jpg")
	pdf.watermark_all_pages()


