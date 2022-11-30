from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


def calculate(food, drink, dessert, tip):
    tax = 0.1
    total_tax = (food + drink + dessert) * tax
    if tip[0] == 'percent':
        total_tip = (food + drink + dessert + total_tax) * tip[1]
    else:
        total_tip = food + drink + dessert + total_tax + tip[1]
    grand_total = food + drink + dessert + total_tax + total_tip
    return total_tax, total_tip, grand_total


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Submit_Button.clicked.connect(lambda: self.submit())
        self.Clear_Button.clicked.connect(lambda: self.clear())
        self.Radio_Custom.clicked.connect(lambda: self.custom())
        self.Radio_10.clicked.connect(lambda: self.radio())
        self.Radio_15.clicked.connect(lambda: self.radio())
        self.Radio_20.clicked.connect(lambda: self.radio())

    def radio(self):
        self.Custom_Entry.setReadOnly(True)
        self.Custom_Entry.setText('')

    def custom(self):
        self.Custom_Entry.setReadOnly(False)

    def clear(self):
        self.Food_Entry.setText('')
        self.Drink_Entry.setText('')
        self.Dessert_Entry.setText('')
        self.Radio_10.click()
        self.Summary_Label.setText('')
        self.Custom_Entry.setText('')
        self.Custom_Entry.setReadOnly(True)

    def submit(self):
        try:
            food = float(self.Food_Entry.text())
            drink = float(self.Drink_Entry.text())
            dessert = float(self.Dessert_Entry.text())
            if self.Radio_10.isChecked():
                tip = ['percent', .1]
            elif self.Radio_15.isChecked():
                tip = ['percent', .15]
            elif self.Radio_20.isChecked():
                tip = ['percent', .2]
            elif self.Radio_Custom.isChecked():
                tip = ['amount', float(self.Custom_Entry.text())]
            else:
                tip = 0
            total_tax, total_tip, grand_total = calculate(food, drink, dessert, tip)
            self.Summary_Label.setText(f'{" " * 25}SUMMARY\n\nFood:{" " * 34}${food:.2f}\nDrink:{" " * 33}${drink:.2f}\nDessert:{" " * 29}${dessert:.2f}\nTax:{" " * 36}${total_tax:.2f}\nTip:{" " * 37}${total_tip:.2f}\n\nTOTAL:{" " * 31}${grand_total:.2f}')
        except ValueError:
            self.Summary_Label.setText(f'\n\n\n{" " * 15}Food drink, and dessert\n{" " * 15}need to be numeric\n{" " * 15}e.g. 10.25 not $10.25')
