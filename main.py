
from PyQt5.QtWidgets import *


app = QApplication([])
window = QWidget()
window.setWindowTitle("Фото шоп ")
window.resize(900, 600)
window.show()



Golovna_linia = QHBoxLayout()
fotos_linia = QVBoxLayout()
foto_linia = QVBoxLayout()
knopki = QHBoxLayout()

papka = QPushButton("Папка")
v_livo = QPushButton("Вліво")
v_pravo = QPushButton("Вправо")
dzerkalo = QPushButton("Дзеркало")
rizkist = QPushButton("Різкість")
HB = QPushButton("Ч/Б")
pole = QListWidget()

Golovna_linia.addLayout(fotos_linia)
Golovna_linia.addLayout(foto_linia)
#Qlabel
foto_linia.addLayout(knopki)
fotos_linia.addWidget(papka)
fotos_linia.addWidget(pole)

knopki.addWidget(v_livo)
knopki.addWidget(v_pravo)
knopki.addWidget(dzerkalo)
knopki.addWidget(rizkist)
knopki.addWidget(HB)

app.setStyleSheet("""
    QWidget
    {
        background-color: #3a784e;
        border-radius: 4px;
        border-width: 2px;
        border-color: bleck;


    }


    QPushButton
    {
        min-height: 25px;
        border-style: double;
        border-width: 2px;
        border-color: bleck;
        background-color: #d9d9d9;
        font-size:16px;
    }
    QTextEdit
    {
        background-color: #d9d9d9;
        border-radius: 4px;
        border-style: double;
    }

    QListWidget
    {
        background-color: #d9d9d9;
        border-radius: 4px;
        border-width: 2px;
        border-color: bleck;  
        border-style: double;      
    }

    QLineEdit
    {
        background-color: #d9d9d9;
        border-radius: 4px;
        border-width: 7px;
        min-height: 20px;
        border-width: 2px;
        border-color: bleck;  
        border-style: double;      
    }



""")


window.setLayout(Golovna_linia)
app.exec_()