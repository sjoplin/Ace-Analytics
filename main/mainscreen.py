from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout

from scraper import scrape

def main():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    teamName = QLineEdit()
    teamName.setText('Georgia Tech')
    layout.addWidget(QLabel('Team Name from Website'))
    layout.addWidget(teamName)
    layout.addWidget(QLabel('7 Digit Number from URL'))
    buttonList = []
    for i in range(10):
        newField = QLineEdit()
        newField.setText('1234567')
        buttonList.append(newField)
        layout.addWidget(newField)
    submit = QPushButton('Submit')
    submit.clicked.connect(lambda: execute(teamName, buttonList))
    layout.addWidget(submit)
    window.setLayout(layout)
    window.show()

    app.exec_()


def execute(teamButton, urlButtons):
    desiredTeam = teamButton.text()
    urlList = []
    for bttn in urlButtons:
        urlList.append(bttn.text())
    scrape(desiredTeam, urlList)




if __name__ == "__main__":
    main()