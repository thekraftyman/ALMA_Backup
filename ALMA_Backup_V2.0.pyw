import os
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    os.system('pip install pyqt5')
    from PyQt5 import QtCore, QtGui, QtWidgets
from Core.ALMA_log import ALMA_log

class Ui_ALMA_BACKUP(object):
    def setupUi(self, ALMA_BACKUP):
        ALMA_BACKUP.setObjectName("ALMA_BACKUP")
        ALMA_BACKUP.resize(794, 600)
        self.centralwidget = QtWidgets.QWidget(ALMA_BACKUP)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 821, 554))
        self.tabWidget.setMinimumSize(QtCore.QSize(791, 554))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.CI_item_input = QtWidgets.QLineEdit(self.tab)
        self.CI_item_input.setGeometry(QtCore.QRect(340, 140, 361, 31))
        self.CI_item_input.setObjectName("CI_item_input")
        self.CI_text = QtWidgets.QLabel(self.tab)
        self.CI_text.setGeometry(QtCore.QRect(280, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.CI_text.setFont(font)
        self.CI_text.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.CI_text.setObjectName("CI_text")
        self.CI_item_text = QtWidgets.QLabel(self.tab)
        self.CI_item_text.setGeometry(QtCore.QRect(130, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.CI_item_text.setFont(font)
        self.CI_item_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CI_item_text.setObjectName("CI_item_text")
        self.CI_add_btn = QtWidgets.QPushButton(self.tab)
        self.CI_add_btn.setGeometry(QtCore.QRect(40, 180, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.CI_add_btn.setFont(font)
        self.CI_add_btn.setObjectName("CI_add_btn")
        self.CI_item_list = QtWidgets.QListWidget(self.tab)
        self.CI_item_list.setGeometry(QtCore.QRect(370, 230, 381, 271))
        self.CI_item_list.setObjectName("CI_item_list")
        self.CI_done_btn = QtWidgets.QPushButton(self.tab)
        self.CI_done_btn.setGeometry(QtCore.QRect(40, 230, 311, 271))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.CI_done_btn.setFont(font)
        self.CI_done_btn.setObjectName("CI_done_btn")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.CO_text = QtWidgets.QLabel(self.tab_2)
        self.CO_text.setGeometry(QtCore.QRect(280, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.CO_text.setFont(font)
        self.CO_text.setAlignment(QtCore.Qt.AlignCenter)
        self.CO_text.setObjectName("CO_text")
        self.CO_done_btn = QtWidgets.QPushButton(self.tab_2)
        self.CO_done_btn.setGeometry(QtCore.QRect(40, 230, 311, 271))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CO_done_btn.setFont(font)
        self.CO_done_btn.setObjectName("CO_done_btn")
        self.CO_item_list = QtWidgets.QListWidget(self.tab_2)
        self.CO_item_list.setGeometry(QtCore.QRect(370, 230, 381, 271))
        self.CO_item_list.setObjectName("CO_item_list")
        self.CO_item_text = QtWidgets.QLabel(self.tab_2)
        self.CO_item_text.setGeometry(QtCore.QRect(130, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.CO_item_text.setFont(font)
        self.CO_item_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CO_item_text.setObjectName("CO_item_text")
        self.CO_ID_text = QtWidgets.QLabel(self.tab_2)
        self.CO_ID_text.setGeometry(QtCore.QRect(56, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.CO_ID_text.setFont(font)
        self.CO_ID_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CO_ID_text.setObjectName("CO_ID_text")
        self.CO_item_input = QtWidgets.QLineEdit(self.tab_2)
        self.CO_item_input.setGeometry(QtCore.QRect(340, 140, 361, 31))
        self.CO_item_input.setObjectName("CO_item_input")
        self.CO_ID_input = QtWidgets.QLineEdit(self.tab_2)
        self.CO_ID_input.setGeometry(QtCore.QRect(340, 99, 361, 31))
        self.CO_ID_input.setObjectName("CO_ID_input")
        self.CO_add_btn = QtWidgets.QPushButton(self.tab_2)
        self.CO_add_btn.setGeometry(QtCore.QRect(40, 182, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.CO_add_btn.setFont(font)
        self.CO_add_btn.setObjectName("CO_add_btn")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.SU_text = QtWidgets.QLabel(self.tab_3)
        self.SU_text.setGeometry(QtCore.QRect(270, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setUnderline(True)
        self.SU_text.setFont(font)
        self.SU_text.setAlignment(QtCore.Qt.AlignCenter)
        self.SU_text.setObjectName("SU_text")
        self.SU_item_text = QtWidgets.QLabel(self.tab_3)
        self.SU_item_text.setGeometry(QtCore.QRect(130, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.SU_item_text.setFont(font)
        self.SU_item_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SU_item_text.setObjectName("SU_item_text")
        self.SU_item_input = QtWidgets.QLineEdit(self.tab_3)
        self.SU_item_input.setGeometry(QtCore.QRect(340, 140, 361, 31))
        self.SU_item_input.setObjectName("SU_item_input")
        self.SU_add_btn = QtWidgets.QPushButton(self.tab_3)
        self.SU_add_btn.setGeometry(QtCore.QRect(40, 180, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.SU_add_btn.setFont(font)
        self.SU_add_btn.setObjectName("SU_add_btn")
        self.SU_done_btn = QtWidgets.QPushButton(self.tab_3)
        self.SU_done_btn.setGeometry(QtCore.QRect(40, 230, 311, 271))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.SU_done_btn.setFont(font)
        self.SU_done_btn.setObjectName("SU_done_btn")
        self.SU_item_list = QtWidgets.QListWidget(self.tab_3)
        self.SU_item_list.setGeometry(QtCore.QRect(370, 230, 381, 271))
        self.SU_item_list.setObjectName("SU_item_list")
        self.tabWidget.addTab(self.tab_3, "")
        ALMA_BACKUP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ALMA_BACKUP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        ALMA_BACKUP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ALMA_BACKUP)
        self.statusbar.setObjectName("statusbar")
        ALMA_BACKUP.setStatusBar(self.statusbar)

        self.retranslateUi(ALMA_BACKUP)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ALMA_BACKUP)

        # ---------------------------------------------------------------------
        # CREATE THE LOG FOR USE WITH THE PROGRAM
        self.ALMA_log = ALMA_log()
        # CREATE LISTS FOR USE
        self.CI_lst = []
        self.CO_lst = []
        self.SU_lst = []
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # CONNECT BUTTONS AND STUFF
        # ---------------------
        # Check In
        self.CI_add_btn.clicked.connect(self.CI_add)
        # self.CI_item_list
        self.CI_done_btn.clicked.connect(self.CI_done)
        self.CI_item_input.returnPressed.connect(self.CI_add_btn.click)

        # Check Out
        self.CO_add_btn.clicked.connect(self.CO_add)
        # self.CO_item_list
        self.CO_item_input.returnPressed.connect(self.CO_add_btn.click)
        self.CO_done_btn.clicked.connect(self.CO_done)
        self.CO_ID_input.returnPressed.connect(self.CO_item_input.setFocus)

        # Scan for Use
        self.SU_add_btn.clicked.connect(self.SU_add)
        self.SU_item_input.returnPressed.connect(self.SU_add_btn.click)
        # self.SU_item_list
        self.SU_done_btn.clicked.connect(self.SU_done)

        # ---------------------------------------------------------------------

    def retranslateUi(self, ALMA_BACKUP):
        _translate = QtCore.QCoreApplication.translate
        ALMA_BACKUP.setWindowTitle(_translate("ALMA_BACKUP", "ALMA BACKUP"))
        self.CI_text.setText(_translate("ALMA_BACKUP", "Check In"))
        self.CI_item_text.setText(_translate("ALMA_BACKUP", "Item Barcode:"))
        self.CI_add_btn.setText(_translate("ALMA_BACKUP", "Add Item"))
        self.CI_done_btn.setText(_translate("ALMA_BACKUP", "DONE!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ALMA_BACKUP", "Check In"))
        self.CO_text.setText(_translate("ALMA_BACKUP", "Check Out"))
        self.CO_done_btn.setText(_translate("ALMA_BACKUP", "DONE!"))
        self.CO_item_text.setText(_translate("ALMA_BACKUP", "Item Barcode:"))
        self.CO_ID_text.setText(_translate("ALMA_BACKUP", "Student ID Number:"))
        self.CO_add_btn.setText(_translate("ALMA_BACKUP", "Add Item"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ALMA_BACKUP", "Check Out"))
        self.SU_text.setText(_translate("ALMA_BACKUP", "Scan For Use"))
        self.SU_item_text.setText(_translate("ALMA_BACKUP", "Item Barcode:"))
        self.SU_add_btn.setText(_translate("ALMA_BACKUP", "Add Item"))
        self.SU_done_btn.setText(_translate("ALMA_BACKUP", "DONE!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ALMA_BACKUP", "Scan For Use"))

    def CI_add(self):
        item = self.CI_item_input.text()
        self.CI_item_input.clear()
        self.CI_item_list.addItem(item)
        self.CI_lst.append(item)

    def CI_done(self):
        if self.CI_item_input.text() != '':
            self.CI_add()
        self.ALMA_log.check_in(self.CI_lst)
        self.CI_item_list.clear()
        self.CI_item_input.clear()
        self.CI_lst = []

    def CO_add(self):
        item = self.CO_item_input.text()
        self.CO_item_input.clear()
        self.CO_item_list.addItem(item)
        self.CO_lst.append(item)

    def CO_done(self):
        ID = self.CO_ID_input.text()
        if self.CO_item_input.text() != '':
            self.CO_add()
        self.ALMA_log.check_out(ID,self.CO_lst)
        self.CO_item_list.clear()
        self.CO_item_input.clear()
        self.CO_ID_input.clear()
        self.CO_lst = []

    def SU_add(self):
        item = self.SU_item_input.text()
        self.SU_item_input.clear()
        self.SU_item_list.addItem(item)
        self.SU_lst.append(item)

    def SU_done(self):
        if self.SU_item_input.text() != '':
            self.SU_add()
        self.ALMA_log.check_in(self.SU_lst,task='Scan for use')
        self.SU_item_list.clear()
        self.SU_item_input.clear()
        self.SU_lst = []



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ALMA_BACKUP = QtWidgets.QMainWindow()
    ui = Ui_ALMA_BACKUP()
    ui.setupUi(ALMA_BACKUP)
    ALMA_BACKUP.show()
    sys.exit(app.exec_())
