import sys
from PyQt5 import QtGui

#app = QtGui.QApplication(sys.argv)
#
#window = QtGui.QWidget()
#window.setGeometry(0, 0, 500, 300)
#window.setWindowTitle("PyQT Tuts!")
#
#window.show()

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
