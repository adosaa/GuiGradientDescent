from PyQt4.QtGui  import *
from PyQt4.QtCore import *
import sys
from interfaz import Ui_MainWindow
class Principal(QMainWindow, Ui_MainWindow):
    # Se define el constructor de la clase __init__
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Principal()
    mainwindow.show()
    sys.exit(app.exec_())

