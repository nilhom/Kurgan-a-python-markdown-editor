# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './design/design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1046)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(192)
        sizePolicy.setVerticalStretch(108)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.notesAlpha = QtWidgets.QListWidget(self.centralwidget)
        self.notesAlpha.setGeometry(QtCore.QRect(10, 89, 151, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.notesAlpha.setFont(font)
        self.notesAlpha.setStyleSheet("border: 0px\n"
"")
        self.notesAlpha.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.notesAlpha.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.notesAlpha.setObjectName("notesAlpha")
        self.smash = QtWidgets.QLabel(self.centralwidget)
        self.smash.setGeometry(QtCore.QRect(10, 890, 151, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.smash.setFont(font)
        self.smash.setAutoFillBackground(False)
        self.smash.setStyleSheet("border:0px;\n"
"background: #202020;\n"
"color: rgba(255, 255, 255, 50);")
        self.smash.setText("")
        self.smash.setWordWrap(True)
        self.smash.setObjectName("smash")
        self.notesBeta = QtWidgets.QListWidget(self.centralwidget)
        self.notesBeta.setGeometry(QtCore.QRect(10, 340, 151, 461))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.notesBeta.setFont(font)
        self.notesBeta.setStyleSheet("border: 0px\n"
"")
        self.notesBeta.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.notesBeta.setObjectName("notesBeta")
        self.leftSideBackground = QtWidgets.QFrame(self.centralwidget)
        self.leftSideBackground.setGeometry(QtCore.QRect(-30, -50, 200, 5000))
        self.leftSideBackground.setMinimumSize(QtCore.QSize(0, 5000))
        self.leftSideBackground.setMaximumSize(QtCore.QSize(16777215, 5000))
        self.leftSideBackground.setStyleSheet("border:0px;\n"
"background: #202020\n"
"")
        self.leftSideBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftSideBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftSideBackground.setObjectName("leftSideBackground")
        self.rightSideBackground = QtWidgets.QFrame(self.centralwidget)
        self.rightSideBackground.setGeometry(QtCore.QRect(1590, -460, 430, 5000))
        self.rightSideBackground.setMinimumSize(QtCore.QSize(0, 5000))
        self.rightSideBackground.setMaximumSize(QtCore.QSize(16777215, 5000))
        self.rightSideBackground.setStyleSheet("border:0px;\n"
"background: #202020\n"
"")
        self.rightSideBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightSideBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightSideBackground.setObjectName("rightSideBackground")
        self.rightside = QtWidgets.QTextEdit(self.rightSideBackground)
        self.rightside.setGeometry(QtCore.QRect(10, 470, 310, 981))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightside.setFont(font)
        self.rightside.setStyleSheet("border: 0px")
        self.rightside.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightside.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rightside.setObjectName("rightside")
        self.topLeftIcon_label = QtWidgets.QLabel(self.centralwidget)
        self.topLeftIcon_label.setGeometry(QtCore.QRect(17, 26, 31, 30))
        self.topLeftIcon_label.setStyleSheet("background: rgba(255, 255, 255, 0)")
        self.topLeftIcon_label.setText("")
        self.topLeftIcon_label.setScaledContents(True)
        self.topLeftIcon_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.topLeftIcon_label.setObjectName("topLeftIcon_label")
        self.kurgan_Label = QtWidgets.QLabel(self.centralwidget)
        self.kurgan_Label.setGeometry(QtCore.QRect(60, 10, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.kurgan_Label.setFont(font)
        self.kurgan_Label.setStyleSheet("border: 0px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: rgb(130, 130, 130)")
        self.kurgan_Label.setObjectName("kurgan_Label")
        self.App_Mainframe = QtWidgets.QFrame(self.centralwidget)
        self.App_Mainframe.setGeometry(QtCore.QRect(170, 0, 1421, 1051))
        self.App_Mainframe.setStyleSheet("border: 0px")
        self.App_Mainframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.App_Mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.App_Mainframe.setObjectName("App_Mainframe")
        self.list_App_Frame = QtWidgets.QFrame(self.App_Mainframe)
        self.list_App_Frame.setGeometry(QtCore.QRect(0, 0, 1421, 1041))
        self.list_App_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_App_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_App_Frame.setObjectName("list_App_Frame")
        self.list_label = QtWidgets.QLabel(self.list_App_Frame)
        self.list_label.setGeometry(QtCore.QRect(70, 70, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.list_label.setFont(font)
        self.list_label.setObjectName("list_label")
        self.list_list = QtWidgets.QListWidget(self.list_App_Frame)
        self.list_list.setGeometry(QtCore.QRect(50, 130, 271, 841))
        self.list_list.setObjectName("list_list")
        item = QtWidgets.QListWidgetItem()
        self.list_list.addItem(item)
        self.list_text = QtWidgets.QPlainTextEdit(self.list_App_Frame)
        self.list_text.setGeometry(QtCore.QRect(340, 50, 1031, 921))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.list_text.setFont(font)
        self.list_text.setObjectName("list_text")
        self.default_list_Button = QtWidgets.QPushButton(self.list_App_Frame)
        self.default_list_Button.setGeometry(QtCore.QRect(150, 90, 171, 31))
        self.default_list_Button.setObjectName("default_list_Button")
        self.list_label.raise_()
        self.list_text.raise_()
        self.default_list_Button.raise_()
        self.list_list.raise_()
        self.mainText_Frame = QtWidgets.QFrame(self.App_Mainframe)
        self.mainText_Frame.setGeometry(QtCore.QRect(20, 20, 1381, 1001))
        self.mainText_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainText_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainText_Frame.setObjectName("mainText_Frame")
        self.mainText = QtWidgets.QTextEdit(self.mainText_Frame)
        self.mainText.setGeometry(QtCore.QRect(40, 90, 1301, 871))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.mainText.setFont(font)
        self.mainText.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mainText.setToolTip("")
        self.mainText.setStyleSheet("border: 0px\n"
"")
        self.mainText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainText.setLineWidth(0)
        self.mainText.setObjectName("mainText")
        self.mainText_Label = QtWidgets.QLabel(self.mainText_Frame)
        self.mainText_Label.setGeometry(QtCore.QRect(43, 33, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mainText_Label.setFont(font)
        self.mainText_Label.setStyleSheet("border: 0px;\n"
"background: rgba(255, 255, 255, 0);\n"
"color: rgb(247, 247, 247)")
        self.mainText_Label.setText("")
        self.mainText_Label.setObjectName("mainText_Label")
        self.toolbarHolder_Frame = QtWidgets.QFrame(self.mainText_Frame)
        self.toolbarHolder_Frame.setGeometry(QtCore.QRect(310, 30, 921, 41))
        self.toolbarHolder_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolbarHolder_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolbarHolder_Frame.setObjectName("toolbarHolder_Frame")
        self.hide_Button = QtWidgets.QPushButton(self.centralwidget)
        self.hide_Button.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.hide_Button.setAutoFillBackground(False)
        self.hide_Button.setStyleSheet("background-color: transparent;border:0px")
        self.hide_Button.setText("")
        self.hide_Button.setObjectName("hide_Button")
        self.rightSideBackground.raise_()
        self.leftSideBackground.raise_()
        self.smash.raise_()
        self.notesAlpha.raise_()
        self.notesBeta.raise_()
        self.topLeftIcon_label.raise_()
        self.kurgan_Label.raise_()
        self.App_Mainframe.raise_()
        self.hide_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kurgan"))
        self.kurgan_Label.setText(_translate("MainWindow", "Kurgan"))
        self.list_label.setText(_translate("MainWindow", "List"))
        __sortingEnabled = self.list_list.isSortingEnabled()
        self.list_list.setSortingEnabled(False)
        item = self.list_list.item(0)
        item.setText(_translate("MainWindow", "test"))
        self.list_list.setSortingEnabled(__sortingEnabled)
        self.default_list_Button.setText(_translate("MainWindow", "List Description"))
        self.action5.setText(_translate("MainWindow", "5"))
