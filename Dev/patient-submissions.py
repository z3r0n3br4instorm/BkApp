# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient-submissions.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

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
global userCode, username, haltcode
haltcode = 0
userCode = sys.argv[1]

def fetchDataFromDatabase():
        global username, userCode, haltcode
        try:
                #notif("UserID "+userCode+" is being processed...")
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                db = client["Hospital"]
                collection = db["Patients"]
                object_id = ObjectId(userCode)
                result = collection.find_one({"_id": object_id})
                if result:
                        username = result['UserName']
                        print(username)
                else:
                        notif.error("User not found in the database!")
                        haltcode = 1
                        sys.exit(1)
        except Exception as e:
                notif.error("Database Communication Error occurred!<br>More Info:"+str(e))
                haltcode = 1
                sys.exit(1)

dataFetchThread = threading.Thread(target=fetchDataFromDatabase)
dataFetchThread.start()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setStyleSheet("font: 8pt \"Space Grotesk\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 361, 81))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 740, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #f0f0f0;
                alternate-background-color: #e6f7ff;
                gridline-color: #cccccc;
                border: 2px solid #8f8f91;
                border-radius: 5px;
                font-family: 'Arial';
                font-size: 14px;
            }

            QTableWidget::item {
                border: 1px solid #dcdcdc;
                padding: 10px;  /* Increased padding for more space inside cells */
                margin: 5px;    /* Added margin for more spacing between cells */
            }

            QTableWidget::item:selected {
                background-color: #3399ff;
                color: white;
            }

            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 8px;  /* Increased padding for header cells */
                border: 1px solid #8f8f91;
                font-weight: bold;
            }

            QTableCornerButton::section {
                background-color: #4CAF50;
                border: 1px solid #8f8f91;
            }
        """)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 530, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Space Grotesk")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("/* QPushButton Style */\n"
                "QPushButton {\n"
                "    background-color: #000; /* Black */\n"
                "    border: none;\n"
                "    color: #FFF; /* White */\n"
                "    padding: 12px 24px;\n"
                "    text-align: center;\n"
                "    text-decoration: none;\n"
                "    display: inline-block;\n"
                "    font-size: 16px;\n"
                "    margin: 4px 2px;\n"
                "    transition-duration: 0.4s;\n"
                "    cursor: pointer;\n"
                "    border-radius: 8px;\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color: #333; /* Darker Gray */\n"
                "}\n"
                "\n"
                "QPushButton:pressed {\n"
                "    background-color: #666; /* Even Darker Gray */\n"
                "    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);\n"
                "}\n"
        "")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton_2.clicked.connect(self.submitRequest)
        MainWindow.setStatusBar(self.statusbar)
        try:
                _translate = QtCore.QCoreApplication.translate
                self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Submission Data</span></p><p><span style=\" font-size:10pt;\">User : "+userCode+"</span></p></body></html>"))
        except Exception as e:
               notif.error(e)
        self.displayUserRequests()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def displayUserRequests(self):
        global username, userCode, haltcode
        if haltcode != 1:
                try:
                        client = pymongo.MongoClient("mongodb://localhost:27017/")
                        db = client["Hospital"]
                        collection = db["Patient_Requests"]
                        print(userCode)
                        results = collection.find({"patientOriginalID": userCode})
                        results = list(results)  # convert the cursor to a list
                        req = len(results)
                        print(int(req))
                        self.tableWidget.setRowCount(int(req))
                        for i in range(int(req)):
                                item = QtWidgets.QTableWidgetItem()
                                self.tableWidget.setVerticalHeaderItem(i, item)
                                symptoms = results[i]['symptoms']
                                status = results[i]['status']
                                appointmentTime = results[i]['appointmentTime']
                                if isinstance(symptoms, list):
                                        symptoms = ', '.join(symptoms)  # Convert list to a comma-separated string
                                item = QtWidgets.QTableWidgetItem(symptoms)  # Create QTableWidgetItem with the string
                                self.tableWidget.setItem(i, 0, item)
                                item = QtWidgets.QTableWidgetItem(status)  # Empty QTableWidgetItem
                                self.tableWidget.setItem(i, 1, item)
                                item = QtWidgets.QTableWidgetItem()
                                item.setCheckState(QtCore.Qt.Unchecked)
                                self.tableWidget.setItem(i, 2, item)
                                item = QtWidgets.QTableWidgetItem(appointmentTime)
                                self.tableWidget.setItem(i, 3, item)
                        self.tableWidget.resizeColumnsToContents()
                        self.tableWidget.resizeRowsToContents()
                except Exception as e:
                        notif.error("Database Communication Error occurred!<br>More Info:" + str(e))
                        sys.exit(1)
        else:
                print("Error occurred! Exiting...")
    def submitRequest(self):
        # Delete the Checked Queries from database
        global userCode
        try:
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                db = client["Hospital"]
                collection = db["Patient_Requests"]
                for i in range(self.tableWidget.rowCount()):
                        if self.tableWidget.item(i, 2).checkState() == QtCore.Qt.Checked:
                                results = collection.find_one({"UserCode": userCode})
                                collection.delete_one(results)
                                # refresh the table
                                self.displayUserRequests()
                notif.success("Requests submitted successfully!")
        except Exception as e:
                notif.error("Database Communication Error occurred!<br>More Info:" + str(e))
                sys.exit(1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Submissions Management"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 3)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Request"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Appointment Time"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
