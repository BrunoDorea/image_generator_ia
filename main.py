import sys
import os
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from ui_main import Ui_MainWindow
from image_gen import create_images


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerador de Imagens IA | Bruno Dórea")

        self.image_folder = "imgs"
        self.current_img_index = 0
        self.image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.btn_right.clicked.connect(self.change_image)
        self.btn_left.clicked.connect(self.change_image)
        self.btn_generate.clicked.connect(self.create_imgs)
        self.update_image()


    def create_imgs(self):
        text = self.txt_description.text()
        image = create_images(text, self.txt_name_file.text())
        self.lbl_img.setPixmap(QPixmap(image))


    def change_image(self):
        if self.image_files:
            self.current_img_index = (self.current_img_index +1) % len(self.image_files)
            self.update_image()


    def update_image(self):
        if self.image_files:
            image_path = os.path.join(self.image_folder, self.image_files[self.current_img_index])
            pixmap = QPixmap(image_path)
            self.lbl_img.setPixmap(pixmap)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
