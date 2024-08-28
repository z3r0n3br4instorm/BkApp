# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
from PyQt5.QtWidgets import QDialog, QMessageBox

import sys
userCode = sys.argv[1]

def error(error):
        subprocess.Popen(["python", "notifications/error.py", error])

def notif(data):
        subprocess.Popen(["python", "notifications/notific.py", data])

def fetchDataFromDatabase():
        global username, userCode, haltcode
        try:
                #notif("UserID "+userCode+" is being processed...")
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                db = client["Hospital"]
                collection = db["admin"]
                object_id = ObjectId(userCode)
                result = collection.find_one({"_id": object_id})
                if result:
                        username = result['UserName']
                else:
                        error("User not found in the database!")
                        haltcode = 1
                        sys.exit(1)
        except Exception as e:
                error("Database Communication Error occurred!<br>More Info:"+str(e))
                haltcode = 1
                sys.exit(1)

class UpdateAdminDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UpdateAdminDialog, self).__init__(parent)
        self.setWindowTitle("Update Admin Credentials")
        self.setGeometry(100, 100, 300, 150)

        # Email input
        self.emailLabel = QtWidgets.QLabel("New Email:", self)
        self.emailLabel.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.emailInput = QtWidgets.QLineEdit(self)
        self.emailInput.setGeometry(QtCore.QRect(100, 20, 180, 30))

        # Password input
        self.passwordLabel = QtWidgets.QLabel("New Password:", self)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 60, 100, 30))
        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(100, 60, 180, 30))

        # Save button
        self.saveButton = QtWidgets.QPushButton("Save", self)
        self.saveButton.setGeometry(QtCore.QRect(100, 100, 80, 30))
        self.saveButton.clicked.connect(self.saveAdminCredentials)

    def saveAdminCredentials(self):
        new_email = self.emailInput.text()
        new_password = self.passwordInput.text()
        
        # Validate the input
        if not new_email or not new_password:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter both email and password.")
            return

        try:
            # Connect to MongoDB and update the admin credentials
            client = MongoClient("mongodb://localhost:27017/")
            db = client["Hospital"]
            collection = db["admin"]

            # Update the admin's email and password
            collection.update_one(
                {"name": "admin"},
                {"$set": {"email": new_email, "password": new_password}}
            )

            QtWidgets.QMessageBox.information(self, "Success", "Admin credentials updated successfully!")
            self.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", str(e))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 717)
        MainWindow.setStyleSheet("font: 10pt \"Space Grotesk Light\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 1271, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../resources/Images/clothing.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 1161, 71))
        self.label_2.setStyleSheet("font: 16pt \"Space Grotesk Light\";")
        self.label_2.setObjectName("label_2")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 1241, 581))
        self.tabWidget.setObjectName("tabWidget")
        
        # First Tab - Patients
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1211, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 494, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 494, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        
        # Second Tab - Prescriptions
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 1211, 471))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.setStyleSheet("""
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
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 494, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 494, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_2, "")
        
        # Third Tab - Patient Requests
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 10, 1211, 471))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(10)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setStyleSheet("""
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 494, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 494, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton.clicked.connect(self.save_changes)
        self.pushButton_2.clicked.connect(self.delete_patient)
        self.pushButton_5.clicked.connect(self.save_changes)
        self.pushButton_6.clicked.connect(self.delete_prescription)
        self.pushButton_7.clicked.connect(self.save_changes)
        self.pushButton_8.clicked.connect(self.delete_request)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Fourth Tab - Doctors
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 10, 1211, 471))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.tableWidget_4.setStyleSheet("""
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
                padding: 10px;
                margin: 5px;
            }

            QTableWidget::item:selected {
                background-color: #3399ff;
                color: white;
            }

            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 8px;
                border: 1px solid #8f8f91;
                font-weight: bold;
            }

            QTableCornerButton::section {
                background-color: #4CAF50;
                border: 1px solid #8f8f91;
            }
        """)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 494, 131, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 494, 131, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton_9.clicked.connect(self.save_doctor_changes)
        self.pushButton_10.clicked.connect(self.delete_doctor)
        self.updateAdminButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateAdminButton.setGeometry(QtCore.QRect(1060, 10, 171, 41))
        self.updateAdminButton.setObjectName("updateAdminButton")
        self.updateAdminButton.setText("Update Admin Credentials")
        self.updateAdminButton.clicked.connect(self.openUpdateAdminDialog)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Connect to MongoDB
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Hospital'] 
        self.doctors_collection = self.client['Hospital']['doctors']
        # try:
        self.load_data()
        # except:
        #     error("An Error Occured while loading Data !...")

    def openUpdateAdminDialog(self):
        self.updateDialog = UpdateAdminDialog()
        self.updateDialog.exec_()


    def load_data(self):
        # Load data from Patients collection into the first table
        patients_collection = self.db['Patients']
        prescriptions_collection = self.db['Patient_Prescriptions']
        requests_collection = self.db['Patient_Requests']

        # Loading Patients
        patients = list(patients_collection.find())
        self.tableWidget.setRowCount(len(patients))
        for row, patient in enumerate(patients):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(patient['UserName']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(patient['Password']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(patient['Email']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(patient['Disorders']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(patient['MaritalStatus']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(patient['Gender']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(patient['_id'])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(patient['Age']))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(patient['BloodGroup']))
            self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(patient['Address']))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

        # Loading Prescriptions
        prescriptions = list(prescriptions_collection.find())
        self.tableWidget_2.setRowCount(len(prescriptions))
        for row, prescription in enumerate(prescriptions):
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(prescription['originalPatientID']))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(prescription['prescription']))
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(prescription['PrescriptionTime']))
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(prescription['doctor']))
            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(prescription['requestID']))
            self.tableWidget_2.resizeColumnsToContents()
            self.tableWidget_2.resizeRowsToContents()
            #self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(prescription['Status']))

        requests = list(requests_collection.find())
        self.tableWidget_3.setRowCount(len(requests))
        try:
            for row, request in enumerate(requests):
                self.tableWidget_3.setItem(row, 0, QtWidgets.QTableWidgetItem(request['UserName']))
                self.tableWidget_3.setItem(row, 1, QtWidgets.QTableWidgetItem(request['doctor']))
                self.tableWidget_3.setItem(row, 2, QtWidgets.QTableWidgetItem(request['appointmentTime']))
                self.tableWidget_3.setItem(row, 3, QtWidgets.QTableWidgetItem(str(request['symptoms'])))
                self.tableWidget_3.setItem(row, 4, QtWidgets.QTableWidgetItem(request['status']))
                self.tableWidget_3.setItem(row, 5, QtWidgets.QTableWidgetItem(str(request['_id'])))
                self.tableWidget_3.setItem(row, 6, QtWidgets.QTableWidgetItem(request['patientOriginalID']))
                self.tableWidget_3.setItem(row, 7, QtWidgets.QTableWidgetItem(request['time']))
                self.tableWidget_3.setItem(row, 8, QtWidgets.QTableWidgetItem(request['appointmentTime']))

                self.tableWidget_3.resizeColumnsToContents()
                self.tableWidget_3.resizeRowsToContents()
        except Exception as e:
            error("An Error Occured while retrieving Data !..., "+str(e))
        self.load_doctors_data()


    def load_doctors_data(self):
        doctors = list(self.doctors_collection.find())
        self.tableWidget_4.setRowCount(len(doctors))
        for row, doctor in enumerate(doctors):
            self.tableWidget_4.setItem(row, 0, QtWidgets.QTableWidgetItem(doctor['name']))
            self.tableWidget_4.setItem(row, 1, QtWidgets.QTableWidgetItem(doctor['email']))
            self.tableWidget_4.setItem(row, 2, QtWidgets.QTableWidgetItem(doctor['occupation']))
            self.tableWidget_4.setItem(row, 3, QtWidgets.QTableWidgetItem(doctor['password']))
            self.tableWidget_4.setItem(row, 4, QtWidgets.QTableWidgetItem(str(doctor['_id'])))
        self.tableWidget_4.resizeColumnsToContents()
        self.tableWidget_4.resizeRowsToContents()


    def save_changes(self):
        # Determine which tab is currently selected
        current_index = self.tabWidget.currentIndex()

        if current_index == 0:  # Patients tab
            self.save_patients_changes()
        elif current_index == 1:  # Prescriptions tab
            self.save_prescriptions_changes()
        elif current_index == 2:  # Patient Requests tab
            self.save_requests_changes()
            self.delete_request()

    def save_doctor_changes(self):
        # Save changes to the doctors collection
        for row in range(self.tableWidget_4.rowCount()):
            doctor_id = self.tableWidget_4.item(row, 4).text()
            if ObjectId.is_valid(doctor_id):
                doctor = {
                    'name': self.tableWidget_4.item(row, 0).text(),
                    'email': self.tableWidget_4.item(row, 1).text(),
                    'occupation': self.tableWidget_4.item(row, 2).text(),
                    'password': self.tableWidget_4.item(row, 3).text()
                }
                self.doctors_collection.update_one({'_id': ObjectId(doctor_id)}, {'$set': doctor}, upsert=True)

    def delete_doctor(self):
        # Delete selected doctor from the doctors collection
        row = self.tableWidget_4.currentRow()
        doctor_id = self.tableWidget_4.item(row, 4).text()
        if ObjectId.is_valid(doctor_id):
            self.doctors_collection.delete_one({'_id': ObjectId(doctor_id)})
            self.tableWidget_4.removeRow(row)


    def save_patients_changes(self):
        row_count = self.tableWidget.rowCount()
        patients_collection = self.db['Patients']

        for row in range(row_count):
            username = self.tableWidget.item(row, 0).text()
            password = self.tableWidget.item(row, 1).text()
            email = self.tableWidget.item(row, 2).text()
            disorders = self.tableWidget.item(row, 3).text()
            marital_status = self.tableWidget.item(row, 4).text()
            gender = self.tableWidget.item(row, 5).text()
            _id = self.tableWidget.item(row, 6).text()
            Age = self.tableWidget.item(row, 7).text()
            bloodgroup = self.tableWidget.item(row, 8).text()
            Address = self.tableWidget.item(row, 9).text()

            patients_collection.update_one(
                {'UserName': username},
                {
                    '$set': {
                        'Password': password,
                        'Email': email,
                        'Disorders': disorders,
                        'MaritalStatus': marital_status,
                        'Gender': gender,
                        '_id': ObjectId(_id),
                        'Age': Age,
                        'BloodGroup': bloodgroup,
                        'Address': Address
                    }
                },
                upsert=True
            )

    def save_prescriptions_changes(self):
        row_count = self.tableWidget_2.rowCount()
        prescriptions_collection = self.db['Patient_Prescriptions']

        for row in range(row_count):
            patient_id = self.tableWidget_2.item(row, 0).text()
            prescription = self.tableWidget_2.item(row, 1).text()
            prescription_time = self.tableWidget_2.item(row, 2).text()
            doctor = self.tableWidget_2.item(row, 3).text()
            request_id = self.tableWidget_2.item(row, 4).text()

            prescriptions_collection.update_one(
                {'originalPatientID': patient_id, 'prescriptionID': patient_id},
                {
                    '$set': {
                        'prescription': prescription,
                        'PrescriptionTime': prescription_time,
                        'doctor': doctor,
                        'request_id': request_id
                    }
                },
                upsert=True
            )

    def save_requests_changes(self):
        row_count = self.tableWidget_3.rowCount()
        requests_collection = self.db['Patient_Requests']

        for row in range(row_count):
            username = self.tableWidget_3.item(row, 0).text()
            doctor = self.tableWidget_3.item(row, 1).text()
            appointment_time = self.tableWidget_3.item(row, 2).text()
            symptoms = self.tableWidget_3.item(row, 3).text()
            status = self.tableWidget_3.item(row, 4).text()
            request_id = self.tableWidget_3.item(row, 5).text()

            requests_collection.update_one(
                {'UserName': username, 'RequestID': request_id},
                {
                    '$set': {
                        'doctor': doctor,
                        'appointmentTime': appointment_time,
                        'symptoms': symptoms,
                        'status': status,
                        'patientOriginalID': self.tableWidget_3.item(row, 6).text(),
                        'time': self.tableWidget_3.item(row, 7).text(),
                        'appointmentTime': self.tableWidget_3.item(row, 8).text()
                    }
                },
                upsert=True
            )

        
    def delete_patient(self):
        # Example function to delete a selected patient
        current_row = self.tableWidget.currentRow()
        if current_row >= 0:
            username = self.tableWidget.item(current_row, 0).text()
            patients_collection = self.db['Patients']
            patients_collection.delete_one({'UserName': username})
            self.tableWidget.removeRow(current_row)
        else:
            QtWidgets.QMessageBox.warning(None, 'Delete Patient', 'Please select a patient to delete.')

    
    def delete_prescription(self):
        # Example function to delete a selected prescription
        current_row = self.tableWidget_2.currentRow()
        if current_row >= 0:
            patient_id = self.tableWidget_2.item(current_row, 0).text()
            prescriptions_collection = self.db['Patient_Prescriptions']
            prescriptions_collection.delete_one({'originalPatientID': patient_id})
            self.tableWidget_2.removeRow(current_row)
        else:
            QtWidgets.QMessageBox.warning(None, 'Delete Prescription', 'Please select a prescription to delete.')
    
    def delete_request(self):
        # Example function to delete a selected request
        current_row = self.tableWidget_3.currentRow()
        if current_row >= 0:
            id = self.tableWidget_3.item(current_row, 5).text()
            requests_collection = self.db['Patient_Requests']
            requests_collection.delete_one({'_id': ObjectId(id)})
            self.tableWidget_3.removeRow(current_row)
            # refresh
            self.load_data()
        else:
            QtWidgets.QMessageBox.warning(None, 'Delete Request', 'Please select a request to delete.')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hospital Management System | Admin Interface"))
        self.label_2.setText(_translate("MainWindow", "Welcome to the Hospital Management System | Admin Interface"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Disorders"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Marital Status"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "_id"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Blood Group"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Address"))
        self.pushButton.setText(_translate("MainWindow", "Save Changes"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove Selection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Patients"))

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patient ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Prescription"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prescription Time"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Doctor ID"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Prescription ID"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        #item.setText(_translate("MainWindow", "Status"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Changes"))
        self.pushButton_6.setText(_translate("MainWindow", "Remove Selection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Prescriptions"))

        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patient Name"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Doctor ID"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Request Time"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Request Type"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Request ID"))
        item=self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Patient Original ID"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Time of Request"))
        item=self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Appointment Time"))
        
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Occupation"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID"))

        self.pushButton_7.setText(_translate("MainWindow", "Save Changes"))
        self.pushButton_8.setText(_translate("MainWindow", "Remove Selection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "Doctors")
        self.pushButton_9.setText("Save Changes")
        self.pushButton_10.setText("Delete Doctor")

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Patient Requests"))

# Main Application Runner
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
