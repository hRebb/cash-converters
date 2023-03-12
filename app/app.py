from PySide2 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Cash Converters")
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_amount = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_amountConverted = QtWidgets.QSpinBox()
        self.btn_invert = QtWidgets.QPushButton("Invert Devise")

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_amount)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_amountConverted)
        self.layout.addWidget(self.btn_invert)
    
    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")

        self.spn_amount.setRange(1, 1000000)
        self.spn_amountConverted.setRange(1, 1000000)

        self.spn_amount.setValue(100)
        self.spn_amountConverted.setValue(100)

    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_amount.valueChanged.connect(self.compute)
        self.btn_invert.clicked.connect(self.invert_devise)

    def compute(self):
        print("compute")

    def invert_devise(self):
        print("Inverser devise")

app = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()