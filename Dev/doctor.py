from PyQt5 import QtWidgets
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
import sys
import subprocess
import time
global haltcode, username, userCode, userID


userID = sys.argv[1]
haltcode = 0
userCode = userID

def error(error_msg):
    subprocess.Popen(["python", "notifications/error.py", error_msg])

class PatientRequestsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PatientRequestsDialog, self).__init__(parent)
        self.setWindowTitle("Patient Requests")
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "color: rgb(0, 0, 0);\n"
                           "font: 25 8pt \"Space Grotesk Medium\";\n")
        # Change window width

        self.resize(635, 600)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "User Code", "Symptoms", "Additional", "Status"])

        self.layout.addWidget(self.tableWidget)

        self.refreshButton = QtWidgets.QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.loadRequests)
        self.layout.addWidget(self.refreshButton)

        self.acceptButton = QtWidgets.QPushButton("Accept")
        self.acceptButton.clicked.connect(self.acceptRequest)
        self.layout.addWidget(self.acceptButton)

        self.declineButton = QtWidgets.QPushButton("Decline")
        self.declineButton.clicked.connect(self.declineRequest)
        self.layout.addWidget(self.declineButton)

        self.deleteButton = QtWidgets.QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteRequest)
        self.layout.addWidget(self.deleteButton)

        self.loadRequests()



    def fetchDataFromDatabase():
        global username, userCode, haltcode, userID
        try:
                #notif("UserID "+userCode+" is being processed...")
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                db = client["Hospital"]
                collection = db["doctors"]
                object_id = ObjectId(userCode)
                result = collection.find_one({"_id": object_id})
                if result:
                        username = result['name']
                else:
                        error("User not found in the database!")
                        haltcode = 1
                        sys.exit(1)
        except Exception as e:
                error("Database Communication Error occurred!<br>More Info:"+str(e))
                haltcode = 1
                sys.exit(1)
    fetchDataFromDatabase()

    def loadRequests(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.Hospital
        collection = db.Patient_Requests
        if haltcode == 0:
            self.tableWidget.setRowCount(0)

            for request in collection.find():
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)

                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(request['_id'])))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(request['UserCode']))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(', '.join(request['symptoms'])))
                self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(request['additional']))
                self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(request['status']))

            # Resize columns to contents
            self.tableWidget.resizeColumnsToContents()
        else :
             error("Unaouthorized Access Attempt Detected! Controlled System Crash Initiated!")
             time.sleep(1000)

    def acceptRequest(self):
        self.updateRequestStatus("accepted")

    def declineRequest(self):
        self.updateRequestStatus("declined")

    def deleteRequest(self):
        selectedRows = self.tableWidget.selectionModel().selectedRows()
        if not selectedRows:
            error("No row selected")
            return

        client = MongoClient('mongodb://localhost:27017/')
        db = client.Hospital
        collection = db.Patient_Requests

        for row in selectedRows:
            requestId = self.tableWidget.item(row.row(), 0).text()
            collection.delete_one({"_id": ObjectId(requestId)})

        self.loadRequests()

    def updateRequestStatus(self, status):
        selectedRows = self.tableWidget.selectionModel().selectedRows()
        if not selectedRows:
            error("No row selected")
            return

        client = MongoClient('mongodb://localhost:27017/')
        db = client.Hospital
        collection = db.Patient_Requests

        for row in selectedRows:
            requestId = self.tableWidget.item(row.row(), 0).text()
            collection.update_one({"_id": ObjectId(requestId)}, {"$set": {"status": status}})

        self.loadRequests()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    patientRequestsDialog = PatientRequestsDialog()
    patientRequestsDialog.show()
    sys.exit(app.exec_())
