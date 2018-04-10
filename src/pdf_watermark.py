import sys
import random
import string
from fpdf import FPDF
from PIL import Image
from pyPdf import PdfFileWriter, PdfFileReader

class PDF(object):
	""" PDF Class """
	filename = ""
	outputname = ""
	imagename = ""
	
	def __image_to_pdf(self):
		""" Image to PDF converter """
		#pdf instance
		pdf = FPDF()
		pdf.add_page()
		#image info
		im = Image.open(self.imagename)
		width, height = im.size
		pdf.image(self.imagename,0,0,width,height)
		pdf.output("tpl/_tpl_image_.pdf", "F")

	def __init__(self, filename="", outputname="", imagename=""):
		""" Constructor """
		if filename == "":
			sys.exit("Filename not given")
		if outputname == "":
			sys.exit("Outputname not given")
		if imagename == "":
			sys.exit("Imagename not given")
		self.filename = filename
		self.outputname = outputname
		self.imagename = imagename
		
	def watermark_all_pages(self):
		""" Watermark in all pages """
		self.__image_to_pdf()
		reader_pdf = PdfFileReader(file(self.filename, "rb"))
		writer_pdf = PdfFileWriter()
		watermark_pdf = PdfFileReader(file("tpl/_tpl_image_.pdf", "rb"))
		overlay = watermark_pdf.getPage(0) #get first page image
		for page_num in range(0, reader_pdf.getNumPages()):
			page = reader_pdf.getPage(page_num)
			page.mergePage(overlay)
			writer_pdf.addPage(page)
		pdf_stream = file(self.outputname, "wb")
		writer_pdf.write(pdf_stream)
		pdf_stream.close()
		print "[+] Done"

	def watermark_page(self, index):
		""" Watermark in all pages """
		self.__image_to_pdf()
		can_overlay = False
		reader_pdf = PdfFileReader(file(self.filename, "rb"))
		writer_pdf = PdfFileWriter()
		watermark_pdf = PdfFileReader(file("tpl/_tpl_image_.pdf", "rb"))
		overlay = watermark_pdf.getPage(0) #get first page image
		for page_num in range(0, reader_pdf.getNumPages()):
			if page_num == index:
				can_overlay = True
			page = reader_pdf.getPage(page_num)
			if can_overlay:
				page.mergePage(overlay)
				can_overlay = False
			writer_pdf.addPage(page)
		pdf_stream = file(self.outputname, "wb")
		writer_pdf.write(pdf_stream)
		pdf_stream.close()
		print "[+] Done"
