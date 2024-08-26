from PyQt5 import QtWidgets
from ui_sidebar import Ui_MainWindow
from dashboard import Ui_Dashboard

class SidebarApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Debug prints
        print("UI setup complete")

        self.dashboard_btn1.clicked.connect(self.show_dashboard)

    def show_dashboard(self):
        print("Dashboard button clicked")

        self.dashboard_widget = QtWidgets.QWidget()
        self.dashboard_ui = Ui_Dashboard()
        self.dashboard_ui.setupUi(self.dashboard_widget)
        
        layout = self.widget.layout()  # Get the existing layout
        if layout:
            layout.addWidget(self.dashboard_widget)  # Add new widget to layout
        else:
            # If there is no layout, create one and set it
            layout = QtWidgets.QVBoxLayout(self.widget)
            layout.addWidget(self.dashboard_widget)
            self.widget.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SidebarApp()
    window.show()
    sys.exit(app.exec_())
