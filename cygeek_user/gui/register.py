# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:/gui/register.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerdialog(object):
    def setupUi(self, registerdialog):
        registerdialog.setObjectName("registerdialog")
        registerdialog.resize(400, 300)
        registerdialog.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(200, 200, 200);\n"
"font: 75 10pt \"Consolas\";")
        registerdialog.setSizeGripEnabled(False)
        registerdialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(registerdialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.username = QtWidgets.QLineEdit(registerdialog)
        self.username.setGeometry(QtCore.QRect(70, 60, 256, 32))
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(registerdialog)
        self.password.setGeometry(QtCore.QRect(70, 110, 256, 32))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.password_2 = QtWidgets.QLineEdit(registerdialog)
        self.password_2.setGeometry(QtCore.QRect(70, 170, 256, 32))
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setClearButtonEnabled(True)
        self.password_2.setObjectName("password_2")
        self.label = QtWidgets.QLabel(registerdialog)
        self.label.setGeometry(QtCore.QRect(160, 10, 81, 16))
        self.label.setObjectName("label")
        self.status = QtWidgets.QTextBrowser(registerdialog)
        self.status.setGeometry(QtCore.QRect(0, 280, 128, 16))
        self.status.setStyleSheet("color: rgb(255, 0, 0);")
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setObjectName("status")

        self.retranslateUi(registerdialog)
        self.buttonBox.accepted.connect(registerdialog.accept) # type: ignore
        self.buttonBox.rejected.connect(registerdialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(registerdialog)

    def retranslateUi(self, registerdialog):
        _translate = QtCore.QCoreApplication.translate
        registerdialog.setWindowTitle(_translate("registerdialog", "Register"))
        self.username.setPlaceholderText(_translate("registerdialog", " Enter Username"))
        self.password.setPlaceholderText(_translate("registerdialog", " Enter Password"))
        self.password_2.setPlaceholderText(_translate("registerdialog", " re-Enter Password"))
        self.label.setText(_translate("registerdialog", "[Registesr]"))
        self.status.setHtml(_translate("registerdialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connecting...</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerdialog = QtWidgets.QDialog()
    ui = Ui_registerdialog()
    ui.setupUi(registerdialog)
    registerdialog.show()
    sys.exit(app.exec_())
