#This code generates a QR code for any text or link and also auto saves it in your desktop. 
import os
import pyqrcode
from PIL import Image

class QrGenerator(object):
	def __init__(self, text):
		self.qr_image = self.qr_gen(text)

	@staticmethod
	def qr_gen(text):
		qr_code = pyqrcode.create(text)
		file_name = "QR Code"
		save_path = os.path.join(os.path.expanduser('~'), 'Desktop')

		img_name = f"{save_path}{file_name}.png"
		qr_code.png(img_name, scale=20)
		img = Image.open(img_name)
		img = img.resize((500, 500), Image.ANTIALIAS)
		img.show()

if __name__ == "__main__" :
	QrGenerator(input("Enter text or link:"))
