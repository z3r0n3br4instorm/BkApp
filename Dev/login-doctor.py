# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login-signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
import subprocess
import threading
import time

global connStat, envStat, mainWin, switch
switch = 1
envStat = "login"
connStat = 2

def error(error):
        subprocess.Popen(["pythonw", "notifications/error.py", error])

def notif(data):
        subprocess.Popen(["pythonw", "notifications/notific.py", data])


def database_connection_successful():
        global connStat
        while connStat != 3:
                try:
                        client = pymongo.MongoClient("mongodb://localhost:27017/")
                        client.server_info()
                        connStat = 1
                except pymongo.errors.ConnectionFailure:
                        connStat = 0
                time.sleep(1)

connStatusThread = threading.Thread(target=database_connection_successful)
connStatusThread.start()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global mainWin
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 498)
        MainWindow.setStyleSheet("font: 8pt \"Space Grotesk\";\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Space Grotesk\";\n"
"")
        mainWin = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 390, 71, 71))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("../resources/Images/clothing.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-30, 360, 1241, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 390, 151, 71))
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(440, 40, 311, 41))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 181, 181))
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("../resources/Profile-PNG-Pic.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 42, 91, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 100, 91, 41))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(440, 100, 70, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(510, 100, 91, 41))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 160, 311, 41))
        self.textEdit_2.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 91, 41))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(440, 220, 311, 41))
        self.textEdit_3.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 220, 161, 41))
        self.label_6.setObjectName("label_6")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(670, 98, 81, 41))
        self.textEdit_4.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(620, 100, 41, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 260, 241, 41))
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 300, 241, 61))
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
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(440, 278, 61, 41))
        self.textEdit_5.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 280, 111, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(520, 282, 121, 41))
        self.label_10.setObjectName("label_10")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(640, 270, 111, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(640, 301, 121, 41))
        self.checkBox_4.setObjectName("checkBox_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(770, 110, 381, 81))
        self.textEdit_6.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(770, 40, 351, 61))
        self.label_11.setObjectName("label_11")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(770, 240, 381, 41))
        self.textEdit_7.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(770, 200, 351, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 1171, 351))
        self.label_13.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.label_13.setObjectName("label_13")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(770, 320, 381, 41))
        self.textEdit_8.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff; /* White background */\n"
"    border: 2px solid #000000; /* Black border */\n"
"    color: #000000; /* Black text color */\n"
"    padding: 5px; /* Padding */\n"
"    font-size: 14px; /* Text font size */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #000000; /* Border color on focus (black) */\n"
"}\n"
"")
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(770, 280, 131, 41))
        self.label_14.setObjectName("label_13")
        self.label_12.raise_()
        self.label_14.raise_()
        self.textEdit_8.raise_()
        self.textEdit_7.raise_()
        self.label.raise_()
        self.line.raise_()
        self.pushButton_2.raise_()
        self.textEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.textEdit_2.raise_()
        self.label_5.raise_()
        self.textEdit_3.raise_()
        self.label_6.raise_()
        self.textEdit_4.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_3.raise_()
        self.textEdit_5.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.textEdit_6.raise_()
        self.label_11.raise_()
        self.textEdit_7.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self._update_timer = QtCore.QTimer()
        self._update_timer.start(500)
        self._update_timer.timeout.connect(self.checkDatabase)
        self._update_timer.timeout.connect(self.loginSwitchLogic)
        #self._update_timer.timeout.connect(self.restartAnimation)
        ## IN AN UPDATE, COPY CODE FROM HERE ##
        self.pushButton_2.setText("Log In")
        ## System Starts in SignUP Interface
        # if envStat == "signup":
        #       self.pushButton_2.clicked.connect(self.signUp)
        # elif envStat == "login":
        #       self.pushButton_2.clicked.connect(self.login)

        ## Button Clicks
        # Write a logic to switch between Sign Up and Login
        self.pushButton_3.clicked.connect(self.loginSwitchLogic)
        self.pushButton_2.clicked.connect(self.login)
        envStat = "login"
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
                global envStat
                if envStat == "login":
                        print("logging in")
                else:
                        error("Environment Error")
                        return
                UserName = self.textEdit.toPlainText()
                Password = self.textEdit_2.text()
                # Validation
                if UserName == "" or Password == "":
                        error("Please fill all fields")
                        return 
                # Writing to Database
                try:
                        client = pymongo.MongoClient("mongodb://localhost:27017/")
                        db = client["Hospital"]
                        collection = db["doctors"]
                        # print(collection.find_one({"email": UserName, "password": Password}))
                        user_doc = collection.find_one({"email": UserName, "password": Password})
                        if user_doc:
                                results = collection.find_one({"email": UserName})
                                if results:  # Ensure results is not None
                                        notif("Login Successful, Welcome back " + results["name"] + "!")
                                        userID = collection.find_one({"email": UserName, "password": Password})["_id"]
                                        subprocess.Popen(["pythonw", "doctor.py", str(userID)])
                                else:
                                        error("User not found!")
                        else:
                                error("Email or Password is incorrect !")
                except Exception as e:
                        error(str(e))



    def loginSwitchLogic(self):
        global switch, envStat
        if switch == 1:
              self.pushButton_3.setText("Switch to Sign Up")
              self.label_8.setText("Interface Status : Log In")
              self.pushButton_2.setText("Log In")
              self.hideOtherStuffWhenLogin()

    def hideOtherStuffWhenLogin(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "Email :"))
        global mainWin
        self.pushButton_3.hide()
        self.label_8.hide()
        self.label_4.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.label_10.hide()
        self.checkBox_3.hide()
        self.checkBox_4.hide()
        self.label_11.hide()
        self.textEdit_6.hide()
        self.label_12.hide()
        self.textEdit_7.hide()
        self.label_9.hide()
        self.textEdit_5.hide()
        self.label_7.hide()
        self.textEdit_4.hide()
        self.textEdit_3.hide()
        self.label_6.hide()
        self.label_5.setGeometry(QtCore.QRect(330, 98, 91, 41))
        # Resize the window
        self.textEdit_2.setGeometry(QtCore.QRect(440, 98, 311, 41))
        MainWindow.resize(760, 498)
        # Set the pushButton_2 text to Login and position to the length of the window - 2
        self.pushButton_2.setGeometry(QtCore.QRect(mainWin.width() - 180, 390, 151, 71))

    def showOtherStuffWhenSignUp(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "Full Name :"))
        self.label_4.show()
        self.checkBox.show()
        self.checkBox_2.show()
        self.label_10.show()
        self.checkBox_3.show()
        self.checkBox_4.show()
        self.label_11.show()
        self.textEdit_6.show()
        self.label_12.show()
        self.textEdit_7.show()
        self.label_9.show()
        self.textEdit_5.show()
        self.label_7.show()
        self.textEdit_4.show()
        self.textEdit_3.show()
        self.label_6.show()
        # Resize the window to previous size
        self.textEdit_2.setGeometry(QtCore.QRect(440, 160, 311, 41))
        self.label_5.setGeometry(QtCore.QRect(330, 160, 91, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 390, 151, 71))
        MainWindow.resize(1212, 498)

    def checkDatabase(self):
        global connStat
        _translate = QtCore.QCoreApplication.translate
        if connStat == 1:
            self.label_13.hide()
            connStat = 3
            connStatusThread.join()
            self.pushButton_2.show()
        elif connStat == 0:
            self.label_13.setText("<html><head/><body><p align=\"center\">DATABASE CONNECTION FAILED /!\</p></body></html>")
            self.label_13.show()
            connStatusThread.join()
            self.pushButton_2.hide()
        elif connStat == 2:
                self.label_13.setText("<html><head/><body><p align=\"center\">CONNECTING TO DATABASE...</p></body></html>")
                self.label_13.show()
                self.pushButton_2.hide()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Princeton Plainsboro  Software Department - OPD Login [Doctor]"))
        # self.pushButton_2.setText(_translate("MainWindow", "<DYNAMIC>"))
        self.label_3.setText(_translate("MainWindow", "Full Name :"))
        self.label_4.setText(_translate("MainWindow", "Gender      :"))
        self.checkBox.setText(_translate("MainWindow", "Male"))
        self.checkBox_2.setText(_translate("MainWindow", "Female"))
        self.label_5.setText(_translate("MainWindow", "Password :"))
        self.label_6.setText(_translate("MainWindow", "Re-Type Password  :"))
        self.label_7.setText(_translate("MainWindow", "Age :"))
        self.label_14.setText(_translate("MainWindow", "Email :"))
        # self.label_8.setText(_translate("MainWindow", "Interface Status : <INTERFACE>"))
        # self.pushButton_3.setText(_translate("MainWindow", "Switch to <INTERFACE>"))
        self.label_9.setText(_translate("MainWindow", "Blood Group :"))
        self.label_10.setText(_translate("MainWindow", "Marital Status :"))
        self.checkBox_3.setText(_translate("MainWindow", "Married"))
        self.checkBox_4.setText(_translate("MainWindow", "Non-Married"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Disorders / Diseases you are currently taking</p><p>treatment for :</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Home Address :</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CONNECTING TO DATABASE...</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
#     ui.checkDatabase()
    MainWindow.show()
    sys.exit(app.exec_())
