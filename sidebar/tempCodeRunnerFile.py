from PyQt5 import QtWidgets
from ui_sidebar import Ui_MainWindow

class SidebarApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Debug prints
        print("UI setup complete")
        self.dashboard_btn1.clicked.connect(self.show_dashboard)

    def show_dashboard(self):
        print("Dashboard button clicked")
        self.textEdit.setText("This is the Dashboard")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SidebarApp()
    window.show()
    sys.exit(app.exec_())
