from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import cv2
import os
import face_recognition
import numpy as np

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(800, 600)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Dashboard)
        Dashboard.setLayout(self.verticalLayout)

        # Create camera widgets
        self.camera_widget1 = QtWidgets.QLabel(Dashboard)
        self.camera_widget1.setFixedSize(800, 400)
        self.camera_widget1.setStyleSheet("background-color: rgb(0, 0, 0); border: 2px solid #4a90e2; border-radius: 5px;")
        self.camera_widget1.setObjectName("camera_widget1")

        self.camera_widget2 = QtWidgets.QLabel(Dashboard)
        self.camera_widget2.setFixedSize(800, 400)
        self.camera_widget2.setStyleSheet("background-color: rgb(0, 0, 0); border: 2px solid #4a90e2; border-radius: 5px;")
        self.camera_widget2.setObjectName("camera_widget2")

        # Add widgets to layout
        self.verticalLayout.addWidget(self.camera_widget1)
        self.verticalLayout.addWidget(self.camera_widget2)

        # Start the camera feeds
        self.camera_thread1 = CameraThread(0)  # Camera index 0
        self.camera_thread2 = CameraThread(1)  # Camera index 1
        self.camera_thread1.change_pixmap_signal.connect(self.update_camera_widget1)
        self.camera_thread2.change_pixmap_signal.connect(self.update_camera_widget2)
        self.camera_thread1.start()
        self.camera_thread2.start()

    def update_camera_widget1(self, qt_img):
        self.camera_widget1.setPixmap(qt_img)

    def update_camera_widget2(self, qt_img):
        self.camera_widget2.setPixmap(qt_img)


class CameraThread(QtCore.QThread):
    change_pixmap_signal = QtCore.pyqtSignal(QPixmap)

    def __init__(self, camera_index):
        super().__init__()
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.face_folder = "detected_faces"
        self.max_images_per_person = 5
        self.face_encodings = {}  
        self.face_id_map = {}  
        self.next_face_id = 0  
        self.similarity_threshold = 0.6  

        if not os.path.exists(self.face_folder):
            os.makedirs(self.face_folder)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                continue

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            current_face_ids = []
            for (x, y, w, h) in faces:
                face_img = frame[y:y + h, x:x + w]
                face_encoding = self.get_face_encoding(face_img)
                
                if face_encoding is not None:
                    face_encoding_tuple = tuple(face_encoding.flatten())
                    matched_id = self.find_face_id(face_encoding)
                    
                    if matched_id is not None:
                        # Save image if less than max images
                        person_folder = os.path.join(self.face_folder, f'person_{matched_id}')
                        if len(os.listdir(person_folder)) < self.max_images_per_person:
                            self.save_face_image(face_img, matched_id)
                        current_face_ids.append(matched_id)
                    else:
                        # New face, create a new ID and save the face
                        new_id = self.next_face_id
                        person_folder = os.path.join(self.face_folder, f'person_{new_id}')
                        if not os.path.exists(person_folder):
                            os.makedirs(person_folder)
                        self.save_face_image(face_img, new_id)
                        self.face_encodings[new_id] = face_encoding
                        self.face_id_map[face_encoding_tuple] = new_id
                        self.next_face_id += 1
                        current_face_ids.append(new_id)
                    
                    # Draw bounding box and label
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(frame, f'ID: {new_id if matched_id is None else matched_id}', 
                                (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.change_pixmap_signal.emit(QPixmap.fromImage(qt_img))

    def get_face_encoding(self, face_img):
        # Convert face image to RGB (face_recognition expects RGB)
        face_img_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        # Get the face encodings for the detected face
        encodings = face_recognition.face_encodings(face_img_rgb)
        return encodings[0] if encodings else None

    def find_face_id(self, face_encoding):
        for face_id, encoding in self.face_encodings.items():
            matches = face_recognition.compare_faces([encoding], face_encoding, tolerance=self.similarity_threshold)
            if matches[0]:
                return face_id
        return None

    def save_face_image(self, face_img, face_id):
        person_folder = os.path.join(self.face_folder, f'person_{face_id}')
        face_img_path = os.path.join(person_folder, f'face_{len(os.listdir(person_folder))}.jpg')
        cv2.imwrite(face_img_path, face_img)

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()


