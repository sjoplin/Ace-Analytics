import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QMessageBox, QMainWindow
from PyQt5.QtCore import QSize
import requests

from scraper import singleurlscrape

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 200))
        self.setWindowTitle("Ace Analytics")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Team Name:')
        self.teamName = QLineEdit(self)
        self.teamName.setText('Georgia Tech')

        self.teamName.move(160, 20)
        self.teamName.resize(300, 32)
        self.nameLabel.move(20, 20)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Current Season URL:')
        self.firsturl = QLineEdit(self)
        self.firsturl.setText('Required')

        self.firsturl.move(160, 60)
        self.firsturl.resize(300, 32)
        self.nameLabel2.move(20, 60)
        self.nameLabel2.resize(140, 32)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Last Season URL:')
        self.secondurl = QLineEdit(self)
        self.secondurl.setText('Required if first 10 games of season')

        self.secondurl.move(160, 100)
        self.secondurl.resize(300, 32)
        self.nameLabel3.move(20, 100)
        self.nameLabel3.resize(140, 32)


        pybutton = QPushButton('Submit', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(200, 160)



    def clickMethod(self):
        desiredTeam = self.teamName.text()
        url = self.firsturl.text()
        url2 = self.secondurl.text()
        try:
            singleurlscrape(desiredTeam, url, url2)
            QMessageBox.about(self, "Success", "Spread is in the PDFs folder for " + desiredTeam)
        except requests.exceptions.MissingSchema:
            QMessageBox.about(self, "Error", "Invalid URL")
        except Exception as e:
            text = 'Exception code: ' + str(type(e)) + '\n' + 'Error Message: ' + str(e)
            QMessageBox.about(self, "Error", text)




# def main():
#     launch()


# def launch():
#     app = QApplication([])
#     window = QWidget()
#     layout = QVBoxLayout()

#     teamName = QLineEdit()
#     teamName.setText('Georgia Tech')
#     layout.addWidget(QLabel('Team Name from Website'))
#     layout.addWidget(teamName)
#     layout.addWidget(QLabel('Team HomePage'))

#     newField = QLineEdit()
#     newField.setText('Team URL')
#     button = (newField)
#     layout.addWidget(newField)
#     newField2 = QLineEdit()
#     newField2.setText('Previous Season URL')
#     button2 = (newField2)
#     layout.addWidget(newField2)
#     submit = QPushButton('Submit')
#     submit.clicked.connect(lambda: execute(teamName, button, button2))
#     layout.addWidget(submit)
#     window.setLayout(layout)
#     window.show()

#     app.exec_()


# def execute(teamButton, button, previousSeason):
#     desiredTeam = teamButton.text()
#     url = button.text()
#     url2 = previousSeason.text()
#     QMessageBox.about(self, "Title", "Message")
#     #singleurlscrape(desiredTeam, url, url2)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
