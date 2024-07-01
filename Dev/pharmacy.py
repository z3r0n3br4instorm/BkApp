# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pharmacy_interface_demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
import subprocess
import sys
import threading
from bson.objectid import ObjectId
import pymongo
import re
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import notifications as notif

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 436)
        MainWindow.setStyleSheet("font: 8pt \"Space Grotesk\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("../resources/Images/clothing.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 80, 1241, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 0, 411, 91))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(384, 380, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 491, 271))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load prescriptions when the application starts
        self.loadPrescriptions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pharmacy Interface - v0.0.1 [ALPHA]"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Received Prescriptions</span></p><p><span style=\" font-size:10pt;\">Princeton Plainsboro Pharmacy</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "View Request"))

    def loadPrescriptions(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client.Hospital
        requests_collection = db.Patient_Requests
        patients_collection = db.Patients

        self.listWidget.clear()

        for request in requests_collection.find():
            patient_id = request["patientOriginalID"]
            patient = patients_collection.find_one({"_id": ObjectId(patient_id)})
            if patient:
                username = patient["UserName"]
                request_id = request["_id"]
                symptoms = ", ".join(request["symptoms"]) if "symptoms" in request else "N/A"
                self.listWidget.addItem(f"{username} - {request_id} - Symptoms: {symptoms}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())