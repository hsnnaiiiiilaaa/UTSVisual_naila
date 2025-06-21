# -- coding: utf-8 --

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 828)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # LineEdits
        self.lineEdit_npm = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_npm.setGeometry(QtCore.QRect(210, 50, 171, 22))
        self.lineEdit_npm.setObjectName("lineEdit_npm")

        self.lineEdit_nama = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nama.setGeometry(QtCore.QRect(210, 90, 171, 22))
        self.lineEdit_nama.setObjectName("lineEdit_nama")

        self.lineEdit_panggilan = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_panggilan.setGeometry(QtCore.QRect(210, 140, 171, 22))
        self.lineEdit_panggilan.setObjectName("lineEdit_panggilan")

        self.lineEdit_telepon = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_telepon.setGeometry(QtCore.QRect(210, 180, 171, 22))
        self.lineEdit_telepon.setObjectName("lineEdit_telepon")

        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(210, 230, 171, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.lineEdit_kelas = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kelas.setGeometry(QtCore.QRect(210, 270, 171, 22))
        self.lineEdit_kelas.setObjectName("lineEdit_kelas")

        self.lineEdit_matkul = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_matkul.setGeometry(QtCore.QRect(210, 310, 171, 22))
        self.lineEdit_matkul.setObjectName("lineEdit_matkul")

        self.lineEdit_lokasi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lokasi.setGeometry(QtCore.QRect(210, 360, 171, 22))
        self.lineEdit_lokasi.setObjectName("lineEdit_lokasi")

        # Buttons
        self.btn_tambah = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tambah.setGeometry(QtCore.QRect(240, 430, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tambah.setIcon(icon)
        self.btn_tambah.setObjectName("btn_tambah")

        self.btn_ubah = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ubah.setGeometry(QtCore.QRect(350, 430, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("exchange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ubah.setIcon(icon1)
        self.btn_ubah.setObjectName("btn_ubah")

        self.btn_hapus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hapus.setGeometry(QtCore.QRect(470, 430, 93, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("out-of-stock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hapus.setIcon(icon2)
        self.btn_hapus.setObjectName("btn_hapus")

        self.btn_batal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_batal.setGeometry(QtCore.QRect(800, 430, 93, 28))
        self.btn_batal.setObjectName("btn_batal")

        # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 55, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 131, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 131, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 131, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 131, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 270, 131, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 310, 131, 16))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 360, 131, 16))
        self.label_8.setObjectName("label_8")

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 480, 901, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        headers = [
            "NPM",
            "NAMA LENGKAP",
            "NAMA PANGGILAN",
            "TELEPON",
            "EMAIL",
            "KELAS",
            "LOKASI KAMPUS",
        ]

        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(header)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar & Status Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form Data Mahasiswa"))

        self.lineEdit_npm.setText(_translate("MainWindow", "2310020062"))
        self.lineEdit_nama.setText(_translate("MainWindow", "Hasna Naila"))
        self.lineEdit_panggilan.setText(_translate("MainWindow", "nay"))
        self.lineEdit_telepon.setText(_translate("MainWindow", "0853635282"))
        self.lineEdit_email.setText(_translate("MainWindow", "naila87@gmail.com"))
        self.lineEdit_kelas.setText(_translate("MainWindow", "4A NON REG"))
        self.lineEdit_matkul.setText(_translate("MainWindow", "VISUAL STUDIO 2"))
        self.lineEdit_lokasi.setText(_translate("MainWindow", "BANJARMASIN"))

        self.btn_tambah.setText(_translate("MainWindow", "TAMBAH"))
        self.btn_ubah.setText(_translate("MainWindow", "UBAH"))
        self.btn_hapus.setText(_translate("MainWindow", "HAPUS"))
        self.btn_batal.setText(_translate("MainWindow", "BATAL"))

        self.label.setText(_translate("MainWindow", "NPM"))
        self.label_2.setText(_translate("MainWindow", "NAMA LENGKAP"))
        self.label_3.setText(_translate("MainWindow", "NAMA PANGGILAN"))
        self.label_4.setText(_translate("MainWindow", "TELEPON"))
        self.label_5.setText(_translate("MainWindow", "EMAIL"))
        self.label_6.setText(_translate("MainWindow", "KELAS"))
        self.label_7.setText(_translate("MainWindow", "MATA KULIAH"))
        self.label_8.setText(_translate("MainWindow", "LOKASI KAMPUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())