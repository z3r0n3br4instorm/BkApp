# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from bson.objectid import ObjectId
import subprocess

global patientID
patientID = 0

def error(error):
        subprocess.Popen(["pythonw", "notifications/error.py", error])

def notif(data):
        subprocess.Popen(["pythonw", "notifications/notific.py", data])


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
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.loadPrescriptions)
        self.timer.start(15000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load prescriptions when the application starts
        self.loadPrescriptions()

        # Connect the button click to the method
        self.pushButton.clicked.connect(self.viewRequestDetails)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pharmacy Interface - v0.0.1 [ALPHA]"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Received Prescriptions</span></p><p><span style=\" font-size:10pt;\">Princeton Plainsboro Pharmacy</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "View Request"))

    def loadPrescriptions(self):
        global patientID
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client.Hospital
        prescriptions_collection = db.Patient_Prescriptions
        requests_collection = db.Patient_Requests
        patients_collection = db.Patients

        self.listWidget.clear()
        
        try:
            # Create a set to keep track of added prescriptions
            added_prescriptions = set()
            
            for prescription in prescriptions_collection.find():
                patientID = prescription["originalPatientID"]
                patient = patients_collection.find_one({"_id": ObjectId(patientID)})
                patient_request = requests_collection.find_one({"patientOriginalID": patientID})
                
                if patient and patientID not in added_prescriptions:
                    username = patient["UserName"]
                    request_id = prescription["originalPatientID"]
                    symptoms = ", ".join(patient_request["symptoms"]) if patient_request else "N/A"
                    
                    self.listWidget.addItem(f"{username} - {request_id} - Symptoms: {symptoms}")
                    
                    # Add to set to avoid duplication
                    added_prescriptions.add(patientID)
        except Exception as e:
            error("Debug Trace :" + str(e))
            error("No Prescriptions Available. Check Again Later...")


    def viewRequestDetails(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            selected_text = selected_item.text()
            request_id = selected_text.split(" - ")[1]  # Extract request_id from the text

            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client.Hospital
            requests_collection = db.Patient_Requests
            patients_collection = db.Patients
            prescriptions_collection = db.Patient_Prescriptions

            request = requests_collection.find_one({"patientOriginalID": request_id})
            if request:
                patient_id = request["patientOriginalID"]
                patient = patients_collection.find_one({"_id": ObjectId(patient_id)})
                if patient:
                    username = patient["UserName"]
                    symptoms = ", ".join(request["symptoms"]) if "symptoms" in request else "N/A"
                    # Fetch prescription details
                    prescription = prescriptions_collection.find_one({"originalPatientID": request_id})
                    prescription_details = (
                        f"Precription: {prescription['prescription']}<br>"
                        f"Prescribed Date: {prescription['PrescriptionTime']}<br>"
                        f"Prescribed Doctor: {prescription['doctor']}<br>"
                    ) if prescription else "No prescription details available"

                    # Display details in a new dialog
                    details_dialog = QtWidgets.QDialog()
                    details_dialog.setWindowTitle("Request Details")
                    layout = QtWidgets.QVBoxLayout()

                    patient_label = QtWidgets.QLabel(f"Patient: {username}")
                    request_label = QtWidgets.QLabel(f"Request ID: {request_id}")
                    symptoms_label = QtWidgets.QLabel(f"Symptoms: {symptoms}")
                    prescription_label = QtWidgets.QLabel(f"Prescription Details:<br>{prescription_details}")
                    prescription_label.setTextFormat(QtCore.Qt.RichText)  # Enable rich text formatting

                    layout.addWidget(patient_label)
                    layout.addWidget(request_label)
                    layout.addWidget(symptoms_label)
                    layout.addWidget(prescription_label)

                    # Add Delete Request and Close buttons
                    delete_button = QtWidgets.QPushButton("Complete Request")
                    close_button = QtWidgets.QPushButton("Close")

                    # Connect buttons to their respective slots
                    delete_button.clicked.connect(lambda: self.deleteRequest(request_id, details_dialog))
                    close_button.clicked.connect(details_dialog.close)

                    # Add buttons to the layout
                    button_layout = QtWidgets.QHBoxLayout()
                    button_layout.addWidget(delete_button)
                    button_layout.addWidget(close_button)

                    layout.addLayout(button_layout)

                    details_dialog.setLayout(layout)
                    details_dialog.exec_()

    def deleteRequest(self, request_id, dialog):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client.Hospital
        requests_collection = db.Patient_Requests
        prescriptions_collection = db.Patient_Prescriptions

        # Delete the request from the collection
        requests_collection.delete_one({"patientOriginalID": request_id})

        # Delete the corresponding prescription from the collection
        prescriptions_collection.delete_one({"originalPatientID": request_id})

        # Reload the prescriptions in the main window
        self.loadPrescriptions()

        # Close the dialog after deletion
        dialog.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
