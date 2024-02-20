import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class EmojiChooser(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Emoji Chooser")
        self.setGeometry(200, 200, 400, 300)

        self.label = QLabel("Choose your Emoji")
        self.label.setAlignment(Qt.AlignCenter)

        self.button1 = QPushButton("😍")
        self.button2 = QPushButton("🥰")
        self.button3 = QPushButton("😎")
        self.button1.clicked.connect(lambda: self.choose_emoji("val.png"))
        self.button2.clicked.connect(lambda: self.choose_emoji("wow.png"))
        self.button3.clicked.connect(lambda: self.choose_emoji("Glass.png"))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def choose_emoji(self, sticker_path):
        image = cv2.imread("a.jpg")
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

        cv2.imshow("out", image)
        cv2.waitKey()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmojiChooser()
    window.show()
    sys.exit(app.exec_())
