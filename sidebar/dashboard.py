from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import cv2
from encodeing import FaceEncoder

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(800, 600)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Dashboard)
        Dashboard.setLayout(self.verticalLayout)

        self.camera_widget1 = QtWidgets.QLabel(Dashboard)
        self.camera_widget1.setFixedSize(800, 400)
        self.camera_widget1.setStyleSheet("background-color: rgb(0, 0, 0); border: 2px solid #4a90e2; border-radius: 5px;")
        self.camera_widget1.setObjectName("camera_widget1")

        self.camera_widget2 = QtWidgets.QLabel(Dashboard)
        self.camera_widget2.setFixedSize(800, 400)
        self.camera_widget2.setStyleSheet("background-color: rgb(0, 0, 0); border: 2px solid #4a90e2; border-radius: 5px;")
        self.camera_widget2.setObjectName("camera_widget2")

        self.start_button = QtWidgets.QPushButton(Dashboard)
        self.start_button.setText("AI Processing")
        self.start_button.setStyleSheet("background-color: #4a90e2; color: white;")
        self.start_button.setObjectName("start_button")

        self.verticalLayout.addWidget(self.camera_widget1)
        self.verticalLayout.addWidget(self.camera_widget2)
        self.verticalLayout.addWidget(self.start_button)

        self.camera_thread1 = CameraThread(0)  # Camera index 0
        self.camera_thread2 = CameraThread(1)  # Camera index 1
        self.camera_thread1.change_pixmap_signal.connect(self.update_camera_widget1)
        self.camera_thread2.change_pixmap_signal.connect(self.update_camera_widget2)

        self.camera_thread1.start()
        self.camera_thread2.start()

        self.start_button.clicked.connect(self.toggle_ai_processing)
        self.ai_processing_active = False

    def update_camera_widget1(self, qt_img):
        self.camera_widget1.setPixmap(qt_img)

    def update_camera_widget2(self, qt_img):
        self.camera_widget2.setPixmap(qt_img)

    def toggle_ai_processing(self):
        if self.ai_processing_active:
            self.camera_thread1.stop_ai_processing()
            self.camera_thread2.stop_ai_processing()
            self.start_button.setText("AI")
            print("AI processing stopped.")
        else:
            self.camera_thread1.start_ai_processing()
            self.camera_thread2.start_ai_processing()
            self.start_button.setText("Stop AI Processing")
            print("AI processing started.")
        self.ai_processing_active = not self.ai_processing_active

    def closeEvent(self, event):
        """Ensure that threads are properly terminated when closing the application."""
        self.camera_thread1.stop()
        self.camera_thread2.stop()
        self.camera_thread1.wait()
        self.camera_thread2.wait()
        event.accept()

class CameraThread(QtCore.QThread):
    change_pixmap_signal = QtCore.pyqtSignal(QPixmap)

    def __init__(self, camera_index):
        super().__init__()
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        self.face_encoder = FaceEncoder()
        self.ai_processing = False
        self._running = True

    def run(self):
        while self._running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            if self.ai_processing:
                frame = self.face_encoder.detect_and_recognize_faces(frame)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.change_pixmap_signal.emit(QPixmap.fromImage(qt_img))

    def start_ai_processing(self):
        self.ai_processing = True

    def stop_ai_processing(self):
        self.ai_processing = False

    def stop(self):
        self._running = False
        self.cap.release()
        self.quit()
        self.wait()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
