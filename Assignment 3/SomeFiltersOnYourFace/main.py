import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class EmojiChooser(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Emoji Chooser")
        self.setGeometry(200, 200, 600, 480)

        self.label = QLabel("please Click buttons and set Emoji ")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.button1 = QPushButton("😍")
        self.button2 = QPushButton("🥰")
        self.button3 = QPushButton("😎")
        self.button4 = QPushButton("Blur Face")
        self.button5 = QPushButton("sunglasses and lips")  
        self.button7 = QPushButton("Mirror")

        self.button6 = QPushButton("Save")
        self.button1.clicked.connect(lambda: self.choose_emoji("Input/val.png"))
        self.button2.clicked.connect(lambda: self.choose_emoji("Input/wow.png"))
        self.button3.clicked.connect(lambda: self.choose_emoji("Input/Glass.png"))
        self.button4.clicked.connect(lambda: self.apply_blur("Input/a.jpg"))
        self.button5.clicked.connect(self.add_emoji)  
        self.button7.clicked.connect(lambda: self.apply_miror("Input/a.jpg"))

        self.button6.clicked.connect(self.save_image)

        self.button6.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button7)  
        layout.addWidget(self.button6)  

        self.setLayout(layout)

        self.image = None  

    def choose_emoji(self, sticker_path):
        self.hide_save_button()
        image = cv2.imread("Input/a.jpg")
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        faces = face_detector.detectMultiScale(image, scaleFactor=1.3)
        stickers = cv2.imread(sticker_path, cv2.IMREAD_UNCHANGED)

        for face in faces:
            x, y, w, h = face
            sticker = cv2.resize(stickers, (w, h))
            sticker_alpha = sticker[:, :, 3] / 255
            sticker_inv_alpha = 1.0 - sticker_alpha

            face_region = image[y:y+h, x:x+w]

            for c in range(0, 3):
                face_region[:, :, c] = (sticker_alpha * sticker[:, :, c] +
                                        sticker_inv_alpha * face_region[:, :, c])

      
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image_rgb.shape
        bytesPerLine = 3 * width

        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)
        self.button6.setEnabled(True)

        self.image = image  

    def apply_blur(self, image_path):
        self.hide_save_button()
        image = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        faces = face_detector.detectMultiScale(image_gray, 1.3)

        for face in faces:
            x, y, w, h = face
            face_image = image[y:y+h, x:x+w]

            face_image_small = cv2.resize(face_image, (10, 10)) 
            face_image_big = cv2.resize(face_image_small, (w, h), interpolation=cv2.INTER_NEAREST)  

            image[y:y+h, x:x+w] = face_image_big

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image_rgb.shape
        bytesPerLine = 3 * width

        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)
        self.button6.setEnabled(True)

        self.image = image  

    def apply_miror(self, image_path):
        self.hide_save_button()
        image = cv2.imread(image_path)

        height, width, channel = image.shape
        shift = 10

        flipVertical = cv2.flip(image[:,shift:width//2 + shift],1)
        flipVertical = cv2.resize(flipVertical, (width//2 - shift, height))
        image[:,width //2 + shift:] = flipVertical


        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image_rgb.shape
        bytesPerLine = 3 * width

        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)
        self.button6.setEnabled(True)
        self.image = image  

    def add_emoji(self):
        self.hide_save_button()
        image = cv2.imread("Input/a.jpg")
        Sunglasses_sticker = cv2.imread("Input/Sunglasess.png", cv2.IMREAD_UNCHANGED)
        lips_sticker = cv2.imread("Input/lips.png", cv2.IMREAD_UNCHANGED)

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        eyes_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
        eyes = eyes_detector.detectMultiScale(image_gray, 1.3, 30)

        lips_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
        lipses = lips_detector.detectMultiScale(image_gray, 1.3, 30)

        if len(eyes) >= 2:
            x_mid = sum((x + w // 2) for (x, y, w, h) in eyes) / len(eyes)
            y_mid = sum((y + h // 2) for (x, y, w, h) in eyes) / len(eyes)

            sticker_width = 200  
            sticker_height = 100  

            x_sticker = int(x_mid - sticker_width / 2)
            y_sticker = int(y_mid - sticker_height / 2)

            Sunglasses_sticker_resized = cv2.resize(Sunglasses_sticker, (sticker_width, sticker_height))

            Sunglasses_sticker_alpha = Sunglasses_sticker_resized[:, :, 3] / 255
            sticker_inv_alpha = 1.0 - Sunglasses_sticker_alpha
            face_region = image[y_sticker:y_sticker + sticker_height, x_sticker:x_sticker + sticker_width]

            for c in range(3):
                face_region[:, :, c] = (Sunglasses_sticker_alpha * Sunglasses_sticker_resized[:, :, c] +
                                        sticker_inv_alpha * face_region[:, :, c])

        for lips in lipses:
            x, y, w, h = lips

            x_lips_sticker = x + 5
            y_lips_sticker = y - 11

            lips_sticker_resized = cv2.resize(lips_sticker, (w, h))

            sticker_alpha_lips = lips_sticker_resized[:, :, 3] / 255
            sticker_inv_alpha_lips = 1.0 - sticker_alpha_lips
            face_region_lips = image[y_lips_sticker:y_lips_sticker + h, x_lips_sticker:x_lips_sticker + w]

            for c in range(3):
                face_region_lips[:, :, c] = (sticker_alpha_lips * lips_sticker_resized[:, :, c] +
                                            sticker_inv_alpha_lips * face_region_lips[:, :, c])

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image_rgb.shape
        bytesPerLine = 3 * width

        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)
        self.button6.setEnabled(True)  

        self.image = image  


    def hide_save_button(self):
        self.button6.setEnabled(False)

    def save_image(self):
        if self.image is not None:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self,"Save Image", "","All Files (*);;JPEG Files (*.jpg)", options=options)
            if file_path:
                cv2.imwrite(file_path, self.image)
                print("Image saved successfully as", file_path)
            else:
                print("No image to save!")
        else:
            print("No image to save!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmojiChooser()
    window.show()
    sys.exit(app.exec_())
