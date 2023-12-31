# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:/gui/Join.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_joindialog(object):
    def setupUi(self, joindialog):
        joindialog.setObjectName("joindialog")
        joindialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/c/ff.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        joindialog.setWindowIcon(icon)
        joindialog.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Consolas\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(joindialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.status = QtWidgets.QTextBrowser(joindialog)
        self.status.setGeometry(QtCore.QRect(0, 280, 128, 16))
        self.status.setStyleSheet("color: rgb(255, 0, 0);")
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setObjectName("status")
        self.label = QtWidgets.QLabel(joindialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 41, 16))
        self.label.setObjectName("label")
        self.chatroom = QtWidgets.QLineEdit(joindialog)
        self.chatroom.setGeometry(QtCore.QRect(70, 130, 256, 32))
        self.chatroom.setClearButtonEnabled(True)
        self.chatroom.setObjectName("chatroom")

        self.retranslateUi(joindialog)
        self.buttonBox.accepted.connect(joindialog.accept) # type: ignore
        self.buttonBox.rejected.connect(joindialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(joindialog)

    def retranslateUi(self, joindialog):
        _translate = QtCore.QCoreApplication.translate
        joindialog.setWindowTitle(_translate("joindialog", "Join"))
        self.status.setHtml(_translate("joindialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connecting...</p></body></html>"))
        self.label.setText(_translate("joindialog", "[Join]"))
        self.chatroom.setPlaceholderText(_translate("joindialog", " Enter Chatroom name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    joindialog = QtWidgets.QDialog()
    ui = Ui_joindialog()
    ui.setupUi(joindialog)
    joindialog.show()
    sys.exit(app.exec_())
