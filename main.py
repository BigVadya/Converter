import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from ui import Ui_MainWindow
from forex_python.converter import CurrencyRates

class CurrencyConv(QtWidgets.QMainWindow):
	def __init__(self):
		super(CurrencyConv, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.init_UI()
		

	def init_UI(self):
		self.setWindowTitle('Converter')
		self.setWindowIcon(QIcon('logo.png'))

		self.ui.pushButton.clicked.connect(self.converter)

	def converter(self):
		c = CurrencyRates()
		first_currency = self.ui.first_currency.currentText()
		second_currency = self.ui.second_currency.currentText()
		input_currency = int(self.ui.input_currency.text())     
		output_currency = round(c.convert('%s' % (first_currency), '%s' % (second_currency), input_currency), 2)
		self.ui.output_currency.setText(str(output_currency))
	

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	application = CurrencyConv()
	application.show()
	 
	sys.exit(app.exec())