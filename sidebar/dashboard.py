from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import cv2
import sys

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setObjectName("centralwidget")

        self.camera_widget1 = QtWidgets.QLabel(self.centralwidget)
        self.camera_widget1.setGeometry(QtCore.QRect(50, 50, 300, 200))
        self.camera_widget1.setStyleSheet("background-color: rgb(0, 0, 0); border: 2px solid #4a90e2; border-radius: 5px;")
        self.camera_widget1.setObjectName("camera_widget1")

        self.camera_widget2 = QtWidgets.QLabel(self.centralwidget)
        self.camera_widget2.setGeometry(QtCore.QRect(400, 50, 300, 200))
        self.camera_widget2.setStyleSheet("background-color: rgb(0, 0, 0); border: 2px solid #4a90e2; border-radius: 5px;")
        self.camera_widget2.setObjectName("camera_widget2")

        Dashboard.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Dashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Dashboard.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Dashboard)
        self.statusbar.setObjectName("statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

        # Start the camera feeds
        self.camera_thread1 = CameraThread(0)  # Camera index 0
        self.camera_thread2 = CameraThread(1)  # Camera index 1
        self.camera_thread1.change_pixmap_signal.connect(self.update_camera_widget1)
        self.camera_thread2.change_pixmap_signal.connect(self.update_camera_widget2)
        self.camera_thread1.start()
        self.camera_thread2.start()

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Dashboard"))

    def update_camera_widget1(self, qt_img):
        self.camera_widget1.setPixmap(qt_img)

    def update_camera_widget2(self, qt_img):
        self.camera_widget2.setPixmap(qt_img)

from PyQt5.QtCore import QThread, pyqtSignal

class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(QPixmap)

    def __init__(self, camera_index):
        super().__init__()
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise ValueError(f"Unable to open camera feed with index: {self.camera_index}")

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                continue

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.change_pixmap_signal.emit(QPixmap.fromImage(qt_img))

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
