from PyQt5 import QtCore, QtGui, QtWidgets
from procces import YoutubeDownloaderProcces, DOWNLOAD_PATH
from math import floor
import os
import time

class YoutubeDownloaderUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.inputLinkHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.inputLinkHLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLinkHLayout.setObjectName("inputLinkHLayout")
        
        self.linkInputLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.linkInputLabel.setObjectName("linkInputLabel")
        
        self.inputLinkHLayout.addWidget(self.linkInputLabel)
        
        self.linkInputLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.linkInputLineEdit.setObjectName("lineEdit")
        
        self.inputLinkHLayout.addWidget(self.linkInputLineEdit)
        
        self.getLinkStreamsPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.getLinkStreamsPushButton.setObjectName("getLinkStreamsPushButton")
        self.getLinkStreamsPushButton.clicked.connect(self.getLinkStreamsButtonClicked)
        self.inputLinkHLayout.addWidget(self.getLinkStreamsPushButton)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setVisible(False)

        self.setStreamTypeHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.setStreamTypeHLayout.setContentsMargins(0, 0, 0, 0)
        self.setStreamTypeHLayout.setObjectName("setStreamTypeHLayout")
        
        self.setStreamTypeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.setStreamTypeLabel.setObjectName("setStreamTypeLabel")
        
        self.setStreamTypeHLayout.addWidget(self.setStreamTypeLabel)
        
        self.setStreamTypeOnlyAudioRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.setStreamTypeOnlyAudioRadioButton.setObjectName("setStreamTypeOnlyAudioRadioButton")
        self.setStreamTypeHLayout.addWidget(self.setStreamTypeOnlyAudioRadioButton)
        self.setStreamTypeOnlyAudioRadioButton.setChecked(True)

        self.setStreamTypeOnlyVideoRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.setStreamTypeOnlyVideoRadioButton.setObjectName("setStreamTypeOnlyVideoRadioButton")
        self.setStreamTypeHLayout.addWidget(self.setStreamTypeOnlyVideoRadioButton)

        self.setStreamTypeProgressiveRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.setStreamTypeProgressiveRadioButton.setObjectName("setStreamTypeProgressiveRadioButton")
        self.setStreamTypeHLayout.addWidget(self.setStreamTypeProgressiveRadioButton)

        self.setStreamTypeButtonGroup = QtWidgets.QButtonGroup(self.horizontalLayoutWidget_2)
        self.setStreamTypeButtonGroup.addButton(self.setStreamTypeOnlyAudioRadioButton, 0)
        self.setStreamTypeButtonGroup.addButton(self.setStreamTypeOnlyVideoRadioButton, 1)
        self.setStreamTypeButtonGroup.addButton(self.setStreamTypeProgressiveRadioButton, 2)
        self.setStreamTypeButtonGroup.buttonClicked.connect(self.setStreamTypePreferences)
        
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setVisible(False)
        self.setStreamQualityHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.setStreamQualityHLayout.setContentsMargins(0, 0, 0, 0)
        self.setStreamQualityHLayout.setObjectName("setStreamQualityHLayout")
        
        self.setStreamQualityLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        
        self.setStreamQualityLabel.setObjectName("setStreamQualityLabel")
        self.setStreamQualityHLayout.addWidget(self.setStreamQualityLabel)
        

        self.setStreamQualityHighRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.setStreamQualityHighRadioButton.setObjectName("setStreamQualityHighRadioButton")
        self.setStreamQualityHLayout.addWidget(self.setStreamQualityHighRadioButton)
        self.setStreamQualityHighRadioButton.setChecked(True)

        self.setStreamQualityLowRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.setStreamQualityLowRadioButton.setObjectName("setStreamQualityLowRadioButton")
        self.setStreamQualityHLayout.addWidget(self.setStreamQualityLowRadioButton)
        
        self.setStreamQualityButtonGroup = QtWidgets.QButtonGroup(self.horizontalLayoutWidget_3)
        self.setStreamQualityButtonGroup.addButton(self.setStreamQualityHighRadioButton, 0)
        self.setStreamQualityButtonGroup.addButton(self.setStreamQualityLowRadioButton, 1)
        self.setStreamQualityButtonGroup.buttonClicked.connect(self.setStreamQualityPreferences)
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setVisible(False)

        self.streamDataLabelsVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.streamDataLabelsVLayout.setContentsMargins(0, 0, 0, 0)
        self.streamDataLabelsVLayout.setObjectName("streamDataLabelsVLayout")
        
        self.streamTitleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.streamTitleLabel.setObjectName("streamTitleLabel")
        self.streamDataLabelsVLayout.addWidget(self.streamTitleLabel)
        
        self.streamChannelLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.streamChannelLabel.setObjectName("streamChannelLabel")
        self.streamDataLabelsVLayout.addWidget(self.streamChannelLabel)
        
        self.streamLengthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.streamLengthLabel.setObjectName("streamLengthLabel")
        self.streamDataLabelsVLayout.addWidget(self.streamLengthLabel)
        
        self.streamSizeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.streamSizeLabel.setObjectName("streamSizeLabel")
        self.streamDataLabelsVLayout.addWidget(self.streamSizeLabel)
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setVisible(False)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
    
        self.streamTitleDataLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.streamTitleDataLabel.setObjectName("streamTitleDataLabel")
        self.verticalLayout_3.addWidget(self.streamTitleDataLabel)
        
        self.streamChannelDataLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.streamChannelDataLabel.setObjectName("streamChannelDataLabel")
        self.verticalLayout_3.addWidget(self.streamChannelDataLabel)
        
        self.streamLengthDataLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.streamLengthDataLabel.setObjectName("streamLengthDataLabel")
        self.verticalLayout_3.addWidget(self.streamLengthDataLabel)
        
        self.streamSizeDataLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.streamSizeDataLabel.setObjectName("streamSizeDataLabel")
        self.verticalLayout_3.addWidget(self.streamSizeDataLabel)
        
        self.downloadSelectedStreamPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadSelectedStreamPushButton.setObjectName("pushButton")
        self.downloadSelectedStreamPushButton.clicked.connect(self.setDownloadButtonClicked)
        self.downloadSelectedStreamPushButton.setVisible(False)

        self.downloadProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.downloadProgressBar.setProperty("value", 24)
        self.downloadProgressBar.setObjectName("progressBar")
        self.downloadProgressBar.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.setUIGeometry(MainWindow)
        self.setStyleSheets(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setUIGeometry(self, MainWindow):
        MainWindow.resize(640, 360)
        
        self.titleLabel.setGeometry(QtCore.QRect(5, 5, 320, 20))
        
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 471, 51))
        
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 471, 41))
        
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 149, 281, 41))
        
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 140, 101, 141))
        
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 140, 221, 141))
        
        self.downloadSelectedStreamPushButton.setGeometry(QtCore.QRect(10, 240, 271, 41))
        
        self.downloadProgressBar.setGeometry(QtCore.QRect(10, 300, 611, 21))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "YOUTUBE DOWNLOADER - mp3/mp4"))

        MainWindow.setWindowIcon(QtGui.QIcon("youtube-downloader-icon.png"))

        #MainWindow.setStyleSheet("QMainWindow {background-image: url('youtube-downloader-background.png'); background-repeat: no-repeat; background-position: center;}")

        self.titleLabel.setText(_translate("MainWindow", "@YOUTUBE DOWNLOADER - furkanaytass"))
        
        self.linkInputLabel.setText(_translate("MainWindow", "YOUTUBE LİNK : "))

        self.linkInputLineEdit.setPlaceholderText("youtube linki yapıştırın/paste youtube link")

        self.getLinkStreamsPushButton.setText(_translate("MainWindow", "DÖNÜŞTÜR"))
        
        self.setStreamTypeLabel.setText(_translate("MainWindow", "VİDEO/SES :"))
        
        self.setStreamTypeOnlyAudioRadioButton.setText(_translate("MainWindow", "Ses"))
        
        self.setStreamTypeOnlyVideoRadioButton.setText(_translate("MainWindow", "Video"))
        
        self.setStreamTypeProgressiveRadioButton.setText(_translate("MainWindow", "Tümleşik"))
        
        self.setStreamQualityLabel.setText(_translate("MainWindow", "KALİTE : "))
        
        self.setStreamQualityHighRadioButton.setText(_translate("MainWindow", "HD"))
        
        self.setStreamQualityLowRadioButton.setText(_translate("MainWindow", "SD"))
        
        self.streamTitleLabel.setText(_translate("MainWindow", "Başlık :"))
        
        self.streamChannelLabel.setText(_translate("MainWindow", "Kanal : "))
        
        self.streamLengthLabel.setText(_translate("MainWindow", "Uzunluk :"))
        
        self.streamSizeLabel.setText(_translate("MainWindow", "Dosya Boyutu :"))
        
        self.streamTitleDataLabel.setText(_translate("MainWindow", "Yok"))
        
        self.streamChannelDataLabel.setText(_translate("MainWindow", "Yok"))
        
        self.streamLengthDataLabel.setText(_translate("MainWindow", "Yok"))
        
        self.streamSizeDataLabel.setText(_translate("MainWindow", "Yok"))
        
        self.downloadSelectedStreamPushButton.setText(_translate("MainWindow", "YÜKLEMEYİ BAŞLAT"))
    
    def setStyleSheets(self, MainWindow):
        self.titleLabel.setStyleSheet("QLabel {font-weight: bold; background-color: rgb(183, 58, 31); color: white;}")

        self.getLinkStreamsPushButton.setStyleSheet("QPushButton {font-weight: bold; background-color: rgb(214, 94, 34); color: white} QPushButton:pressed {background-color: black; color: white}")
    
        self.downloadSelectedStreamPushButton.setStyleSheet("QPushButton {font-weight: bold; background-color: rgb(193, 200, 34); color: white} QPushButton:pressed {background-color: red; color: white}")

        self.streamTitleLabel.setStyleSheet("QLabel {background-color: rgb(114, 28, 178); font-weight: bold; color: white; border: 4px solid white}")
        self.streamChannelLabel.setStyleSheet("QLabel {background-color: rgb(114, 28, 178); font-weight: bold; color: white; border: 4px solid white}")
        self.streamLengthLabel.setStyleSheet("QLabel {background-color: rgb(114, 28, 178); font-weight: bold; color: white; border: 4px solid white}")
        self.streamSizeLabel.setStyleSheet("QLabel {background-color: rgb(114, 28, 178); font-weight: bold; color: white; border: 4px solid white}")
    
        self.streamTitleDataLabel.setStyleSheet("QLabel {font-style: italic;}")
        self.streamChannelDataLabel.setStyleSheet("QLabel {font-style: italic;}")
        self.streamLengthDataLabel.setStyleSheet("QLabel {font-style: italic;}")
        self.streamSizeDataLabel.setStyleSheet("QLabel {font-style: italic;}")

    def getLinkStreamsButtonClicked(self):
        if self.linkInputLineEdit.text() != '':
            try:
                self.streamData = YoutubeDownloaderProcces.getStreamData(self.linkInputLineEdit.text())

                self.streamTitleDataLabel.setText(str(self.streamData.title))
                self.streamChannelDataLabel.setText(str(self.streamData.author))
                self.streamLengthDataLabel.setText(str(str(floor(self.streamData.length / 60)) + "dk. " + str(self.streamData.length % 60) + " sn."))
            
            except Exception as YoutubeLinkError: return False
            
            self.horizontalLayoutWidget_2.setVisible(True)
            self.horizontalLayoutWidget_3.setVisible(True)
            self.verticalLayoutWidget.setVisible(True)
            self.verticalLayoutWidget_2.setVisible(True)
            self.downloadSelectedStreamPushButton.setVisible(True)
            #self.downloadProgressBar.setVisible(True)

        else: 
            print("no link!") 
    
    def setStreamQualityPreferences(self): self.streamQuality = self.setStreamQualityButtonGroup.checkedId()
    def setStreamTypePreferences(self): self.streamType = self.setStreamTypeButtonGroup.checkedId()

    def setDownloadButtonClicked(self):
        self.setStreamQualityPreferences()
        self.setStreamTypePreferences()

        if not self.streamType: 

            if not self.streamQuality: self.selectedStream = YoutubeDownloaderProcces.getOnlyAudioStreams(self.streamData).last()

            else: self.selectedStream = YoutubeDownloaderProcces.getOnlyAudioStreams(self.streamData).first()

        elif self.streamType == 1: 
            
            if not self.streamQuality: self.selectedStream = YoutubeDownloaderProcces.getOnlyVideoStreams(self.streamData).first()

            else: self.selectedStream = YoutubeDownloaderProcces.getOnlyVideoStreams(self.streamData).last()

        elif self.streamType == 2: 
            
            if not self.streamQuality: self.selectedStream = YoutubeDownloaderProcces.getProgressiveStreams(self.streamData).first()

            else: self.selectedStream = YoutubeDownloaderProcces.getProgressiveStreams(self.streamData).last()
        
        #self.streamSizeDataLabel.setText(str(self.selectedStream.filesize_mb) + " MB")
        #self.downloadProgressPath = str(DOWNLOAD_PATH + self.selectedStream.default_filename)
        
        #while self.updateProgressBar():
            #self.downloadProgressBar.setValue(self.updateProgressBar)
    
    #def updateProgressBar(self):
        #if os.path.getsize(self.downloadProgressPath) != self.selectedStream.filesize: return (os.path.getsize(self.downloadProgressPath) / self.selectedStream.filesize) * 100
        #return False