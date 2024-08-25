from PyQt5 import QtCore, QtGui, QtWidgets

from ui_sidebar import Ui_MainWindow

class SidebarApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        # self.icons_names.setHidden(True)

    def setup_connections(self):
        self.ui.dashboard_btn2.clicked.connect(lambda: self.change_stack_index(0))
        self.ui.search_btn2.clicked.connect(lambda: self.change_stack_index(1))
        self.ui.notification_2.clicked.connect(lambda: self.change_stack_index(2))
        self.ui.settings_2.clicked.connect(lambda: self.change_stack_index(3))
        self.ui.pushButton_11.clicked.connect(lambda: self.change_stack_index(4))
        
        self.ui.dashboard_btn1.clicked.connect(lambda: self.change_stack_index(0))
        self.ui.search_btn1.clicked.connect(lambda: self.change_stack_index(1))
        self.ui.notification_1.clicked.connect(lambda: self.change_stack_index(2))
        self.ui.settings_1.clicked.connect(lambda: self.change_stack_index(3))
        self.ui.pushButton_11.clicked.connect(lambda: self.change_stack_index(4))


    def change_stack_index(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
