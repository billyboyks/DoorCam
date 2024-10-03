# face_recognition_module.py

import os
import face_recognition

class FaceRecognitionModule:
    def __init__(self, known_faces_dir, tolerance, model):
        self.known_face_encodings = []
        self.known_face_names = []
        self.tolerance = tolerance
        self.model = model
        self.load_known_faces(known_faces_dir)

    def load_known_faces(self, known_faces_dir):
        for person_name in os.listdir(known_faces_dir):
            person_dir = os.path.join(known_faces_dir, person_name)
            if not os.path.isdir(person_dir):
                continue
            for image_name in os.listdir(person_dir):
                image_path = os.path.join(person_dir, image_name)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    self.known_face_encodings.append(encodings[0])
                    self.known_face_names.append(person_name)
                else:
                    print(f"Warning: No face found in {image_path}")

    def recognize_faces(self, frame):
        rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
        face_locations = face_recognition.face_locations(rgb_frame, model=self.model)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, self.tolerance)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]

            face_names.append(name)
        return face_locations, face_names
