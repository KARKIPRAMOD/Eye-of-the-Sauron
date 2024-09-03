from PyQt5 import QtWidgets
import pandas as pd
import os

def show_notifications(parent_widget):
    """Read the CSV file and display the information in a table format."""
    log_path = 'detection_log.csv'
    
    if not os.path.exists(log_path):
        QtWidgets.QMessageBox.warning(parent_widget, "No Data", "No detection data found.")
        return

    # Read CSV file
    df = pd.read_csv(log_path)

    # Create a new widget to display the table
    table_widget = QtWidgets.QWidget()
    table_layout = QtWidgets.QVBoxLayout(table_widget)

    # Create QTableWidget
    table = QtWidgets.QTableWidget()
    table.setRowCount(len(df))
    table.setColumnCount(len(df.columns))
    
    # Set column headers
    column_headers = ['Camera Index', 'Image from Target', 'Name', 'Timestamp']
    table.setHorizontalHeaderLabels(column_headers)

    # Populate table with data
    for row_idx, row in df.iterrows():
        for col_idx, column_name in enumerate(column_headers):
            value = row.get(column_name.lower().replace(" ", "_"), "")
            item = QtWidgets.QTableWidgetItem(str(value))
            table.setItem(row_idx, col_idx, item)

    table_layout.addWidget(table)

    # Create a new window for the table
    table_window = QtWidgets.QWidget()
    table_window.setWindowTitle("Detection Notifications")
    table_window.setLayout(table_layout)
    table_window.resize(800, 600)  # Adjust size as needed
    table_window.show()
