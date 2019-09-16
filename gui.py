import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "UI Designs/homepage.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class EZStat(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.submitButton.clicked.connect(##choose a functions)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    homepage = EZStat()
    homepage.show()
    sys.exit(app.exec_())
