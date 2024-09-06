import cv2
import os
import face_recognition
import numpy as np
import pickle

class FaceEncoder:
    def __init__(self, face_folder="detected_faces", encodings_file="face_encodings.pkl", max_images_per_person=5, similarity_threshold=0.6):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.face_folder = face_folder
        self.encodings_file = encodings_file
        self.max_images_per_person = max_images_per_person
        self.similarity_threshold = similarity_threshold
        self.face_encodings = {}
        self.next_face_id = 0

        if not os.path.exists(self.face_folder):
            os.makedirs(self.face_folder)
        
        self.load_encodings()

    def load_encodings(self):
        """Load the face encodings from a file if it exists."""
        if os.path.exists(self.encodings_file):
            with open(self.encodings_file, 'rb') as f:
                self.face_encodings = pickle.load(f)
                self.next_face_id = max(self.face_encodings.keys(), default=-1) + 1

    def save_encodings(self):
        """Save the face encodings to a file."""
        with open(self.encodings_file, 'wb') as f:
            pickle.dump(self.face_encodings, f)

    def detect_and_recognize_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
        face_ids = []

        for (x, y, w, h) in faces:
            x, y, w, h = x*2, y*2, w*2, h*2  # Rescale to original frame size
            face_img = frame[y:y + h, x:x + w]
            face_encoding = self.get_face_encoding(face_img)

            if face_encoding is not None:
                matched_id = self.find_face_id(face_encoding)

                if matched_id is not None:
                    self.save_face_if_needed(face_img, matched_id)
                    face_ids.append(matched_id)
                else:
                    new_id = self.register_new_face(face_img, face_encoding)
                    face_ids.append(new_id)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, f'ID: {matched_id if matched_id is not None else new_id}', 
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        return frame

    def get_face_encoding(self, face_img):
        small_face_img = cv2.resize(face_img, (0, 0), fx=0.5, fy=0.5)
        face_img_rgb = cv2.cvtColor(small_face_img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(face_img_rgb)
        return encodings[0] if encodings else None

    def find_face_id(self, face_encoding):
        for face_id, encoding in self.face_encodings.items():
            matches = face_recognition.compare_faces([encoding], face_encoding, tolerance=self.similarity_threshold)
            if matches[0]:
                return face_id
        return None

    def register_new_face(self, face_img, face_encoding):
        new_id = self.next_face_id
        self.face_encodings[new_id] = face_encoding

        person_folder = os.path.join(self.face_folder, f'person_{new_id}')
        os.makedirs(person_folder, exist_ok=True)
        self.save_face_image(face_img, new_id)

        self.next_face_id += 1
        self.save_encodings()  # Save encodings after adding a new face
        return new_id

    def save_face_if_needed(self, face_img, face_id):
        person_folder = os.path.join(self.face_folder, f'person_{face_id}')
        if len(os.listdir(person_folder)) < self.max_images_per_person:
            self.save_face_image(face_img, face_id)

    def save_face_image(self, face_img, face_id):
        person_folder = os.path.join(self.face_folder, f'person_{face_id}')
        face_img_path = os.path.join(person_folder, f'face_{len(os.listdir(person_folder))}.jpg')
        cv2.imwrite(face_img_path, face_img)
