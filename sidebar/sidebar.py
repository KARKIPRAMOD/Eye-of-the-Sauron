from PyQt5 import QtWidgets
from ui_sidebar import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

from dashboard import Ui_Dashboard, CameraThread

class SidebarApp(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Debug prints
        print("UI setup complete")
        self.dashboard_btn1.clicked.connect(self.open_dashboard)

    def open_dashboard(self):
        print("Dashboard button clicked")
        self.dashboard_window = DashboardWindow()
        self.dashboard_window.show()

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)

        self.ui.camera_thread1 = CameraThread(0)  # Camera index 0
        self.ui.camera_thread2 = CameraThread(1)  # Camera index 1
        self.ui.camera_thread1.change_pixmap_signal.connect(self.ui.update_camera_widget1)
        self.ui.camera_thread2.change_pixmap_signal.connect(self.ui.update_camera_widget2)
        self.ui.camera_thread1.start()
        self.ui.camera_thread2.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SidebarApp()
    window.show()
    sys.exit(app.exec_())
