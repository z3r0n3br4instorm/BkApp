from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
import subprocess
import sys
import threading
from bson.objectid import ObjectId
import pymongo
import re
import time

global username, doctor, userCode, symptoms, haltcode
symptoms = []
doctor = "NULL"
username = "Loading..."
haltcode = 0
userCode = sys.argv[1]


doctors = {
    "family_doctor": "FD",
    "ent_specialist": "EET",
    "orthopedic_specialist": "OS",
    "gynecologist": "G"
}


keywords = {
    "family_doctor": ["fever", "cough", "cold", "headache", "fatigue", "stomach ache", "flu"],
    "ent_specialist": ["ear", "throat", "eyes", "hearing", "vision", "infection", "sinus", "sore throat"],
    "orthopedic_specialist": ["bone", "joint", "fracture", "arthritis", "sprain", "back pain", "knee pain", "shoulder pain"],
    "gynecologist": ["pregnancy", "baby", "menstruation", "period", "fertility", "cramps", "contraception", "ovary", "uterus"]
}

def error(error):
        subprocess.Popen(["python", "notifications/error.py", error])

def notif(data):
        subprocess.Popen(["python", "notifications/notific.py", data])


def classify_symptoms():
        global symptoms
        symptom_counts = {doctor: 0 for doctor in doctors} 

        for doctor, kw_list in keywords.items():
                for keyword in kw_list:
                        for symptom in symptoms:
                                if re.search(r'\b' + re.escape(keyword) + r'\b', symptom.lower()):
                                        symptom_counts[doctor] += 1

        suggested_doctor = max(symptom_counts, key=symptom_counts.get)

        if symptom_counts[suggested_doctor] == 0:
                return "general_physician"
        else:
                return doctors[suggested_doctor]
        

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
                else:
                        error("User not found in the database!")
                        haltcode = 1
                        sys.exit(1)
        except Exception as e:
                error("Database Communication Error occurred!<br>More Info:"+str(e))
                haltcode = 1
                sys.exit(1)

dataFetchThread = threading.Thread(target=fetchDataFromDatabase)
dataFetchThread.start()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 695)
        MainWindow.setStyleSheet("font: 8pt \"Space Grotesk\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 560, 271, 61))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 201, 31))
        self.label_2.setStyleSheet("/* QLabel Style */\n"
"QLabel {\n"
"    color: #000; /* Black */\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 195, 871, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 220, 161, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 450, 541, 101))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 420, 191, 31))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 250, 261, 51))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 221, 31))
        self.label_4.setObjectName("label_4")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 330, 261, 81))
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 300, 221, 31))
        self.label_5.setObjectName("label_5")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(310, 330, 261, 81))
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 220, 161, 31))
        self.label_6.setObjectName("label_6")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(310, 250, 261, 51))
        self.listWidget_4.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 561, 81))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 630, 561, 51))
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 560, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Space Grotesk")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("/* QPushButton Style */\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 100, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Space Grotesk")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("/* QPushButton Style */\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Space Grotesk")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("/* QPushButton Style */\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self._update_timer = QtCore.QTimer()
        self._update_timer.start(500)
        self._update_timer.timeout.connect(self.onloadUpdateComponents)
        self.pushButton_5.clicked.connect(self.openPreviousSubmissions)
        self.pushButton_2.clicked.connect(self.submitData)
        self.pushButton_3.clicked.connect(self.logout)
        self.pushButton_4.clicked.connect(self.clearSelections)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitData(self):
        global userCode, symptoms, doctor, haltcode, username
        symptoms = []
        _translate = QtCore.QCoreApplication.translate
        try:
                if haltcode == 0:
                        client = pymongo.MongoClient("mongodb://localhost:27017/")
                        db = client["Hospital"]
                        collection = db["Patient_Requests"]
                        for i in self.listWidget.selectedItems():
                                symptoms.append(i.text())
                        for i in self.listWidget_2.selectedItems():
                                symptoms.append(i.text())
                        for i in self.listWidget_3.selectedItems():
                                symptoms.append(i.text())
                        for i in self.listWidget_4.selectedItems():
                                symptoms.append(i.text())
                        additionalData = self.textEdit.toPlainText()
                        if symptoms == []:
                                error("Please Select Atleast One Symptom !")
                                return
                        if additionalData == "":
                                additionalData = "NULL"
                        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Processing Your Symptoms...</span></p></body></html>"))
                        doctor = classify_symptoms()
                        doctorName = db["doctors"].find_one({"occupation": doctor})["name"]
                        # Get Current Time
                        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # add 24 hours to current time to get the appoinment time
                        appointmentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 86400))
                        collection.insert_one({"UserName": username, "symptoms": symptoms, "additional": additionalData, "status": "pending", "doctor": doctor, "patientOriginalID": userCode, "time": current_time, "appointmentTime": appointmentTime})
                        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">You Should Meet : Dr."+doctorName+"</span></p></body></html>"))
                        notif("Symptoms Submitted Successfully !<br>Thank You For Your Submission !")
                else :
                       error("Unauthorized Access or Request Detected !<br>Controlled Session Crash Active<br>Program will now halt...")
                       time.sleep(100000)
        except Exception as e:
                error("Database Communication Error occured !<br>Please Contact System Administrator...<br>"+str(e))

    
    def clearSelections(self):
        self.listWidget.clearSelection()
        self.listWidget_2.clearSelection()
        self.listWidget_3.clearSelection()
        self.listWidget_4.clearSelection()
        self.textEdit.clear()

    def logout(self):
        sys.exit(0)

    def openPreviousSubmissions(self):
        if haltcode == 0:
                try:
                        subprocess.Popen(["python", "patient-submissions.py", userCode])
                except Exception as e:
                        error(str(e))
        else :
                error("Unauthorized Access or Request Detected !<br>Controlled Session Crash Active<br>Program will now halt...")
                time.sleep(100000)

    def onloadUpdateComponents(self):
        global username, doctor
        # Retrive the user name from the database _id = userCode
        # Retrieve the doctor name from the database
        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Welcome Back</span></p><p align=\"center\"><span style=\" font-size:10pt;\">"+str(username)+"</span></p></body></html>"))
        if doctor == "NULL":
                self.label_8.setText("")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Princeton Plainsboro Software Department - OPD Management System |  Patient"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Symptom Selection</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Common Symptoms</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Additional Informations</span></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Fever"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Cough"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Cold"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Headache"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Fatigue"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Stomach Ache"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Flue"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Eyes, Ears and Throat Related</span></p></body></html>"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Ear Pain"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Throat Pain"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Eye Related"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "Hearing Related"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "Vision Related"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "Infection Related"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Pregnancy Related</span></p></body></html>"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Pregnany"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("MainWindow", "Period"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("MainWindow", "Fertility"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("MainWindow", "Cramps"))
        item = self.listWidget_3.item(4)
        item.setText(_translate("MainWindow", "Contraception"))
        item = self.listWidget_3.item(5)
        item.setText(_translate("MainWindow", "Overy"))
        item = self.listWidget_3.item(6)
        item.setText(_translate("MainWindow", "Uterus"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Bone Related</span></p></body></html>"))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("MainWindow", "Joint Pain"))
        item = self.listWidget_4.item(1)
        item.setText(_translate("MainWindow", "Fracture"))
        item = self.listWidget_4.item(2)
        item.setText(_translate("MainWindow", "Sprain"))
        item = self.listWidget_4.item(3)
        item.setText(_translate("MainWindow", "Back Pain"))
        item = self.listWidget_4.item(4)
        item.setText(_translate("MainWindow", "Knee Pain"))
        item = self.listWidget_4.item(5)
        item.setText(_translate("MainWindow", "Shoulder Pain"))
        item = self.listWidget_4.item(6)
        item.setText(_translate("MainWindow", "Hip Pain"))
        item = self.listWidget_4.item(7)
        item.setText(_translate("MainWindow", "Leg Pain"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Welcome Back</span></p><p align=\"center\"><span style=\" font-size:10pt;\">&lt;UserName&gt;</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">You Should Meet :&lt;DOCTOR NAME&gt;</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Selections"))
        self.pushButton_3.setText(_translate("MainWindow", "LogOut"))
        self.pushButton_5.setText(_translate("MainWindow", "Previous Submissions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
