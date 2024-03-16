from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os
from PIL.ImageFilter import *
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image



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
kartinka = QLabel("катинка")
foto_linia.addWidget(kartinka)
foto_linia.addLayout(knopki)
fotos_linia.addWidget(papka)
fotos_linia.addWidget(pole)

knopki.addWidget(v_livo)
knopki.addWidget(v_pravo)
knopki.addWidget(dzerkalo)
knopki.addWidget(rizkist)
knopki.addWidget(HB)

class Bubliki:
    def __int__(self):
        self.image = None
        self.folder = None
        self.image_name = None
    def load(self):
        full_path = os.path.join(self.folder, self.image_name)
        self.image = Image.open(full_path)
    def show_imege(self):
        pixel = pil2pixmap(self.image)
        kartinka.setPixmap(pixel)

bubliki = Bubliki()

def show_sistem():
    bubliki.folder =QFileDialog.getExistingDirectory()
    list_files = os.listdir(bubliki.folder)
    pole.clear()
    for file in list_files:
        #якщо цей файл
        fileList.addItems(file)
    pole.addItems(list_files)


def show_photo():
    image_name = pole.currentItem().text()
    bubliki.image_name = image_name
    bubliki.load()
    bubliki.show_imege()
def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

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

pole.currentRowChanged.connect(show_photo)
papka.clicked.connect(show_sistem)
window.setLayout(Golovna_linia)
window.show()
app.exec_()