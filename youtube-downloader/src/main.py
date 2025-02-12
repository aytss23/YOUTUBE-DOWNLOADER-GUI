import sys
from ui import YoutubeDownloaderUI, QtWidgets 

if __name__ == "__main__":
    mainApp = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainUI = YoutubeDownloaderUI()
    mainUI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(mainApp.exec_())


