# main.py

import cv2
import logging
from datetime import datetime

from config import (
    CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT,
    ZONE_A_COORDS, ZONE_B_COORDS,
    KNOWN_FACES_DIR, TOLERANCE, MODEL,
    DATABASE_PATH, LOG_LEVEL, DISPLAY_VIDEO
)

from face_recognition_module import FaceRecognitionModule
from movement_tracking_module import MovementTrackingModule
from database_module import DatabaseModule

def main():
    # Set up logging
    logging.basicConfig(level=getattr(logging, LOG_LEVEL))
    logger = logging.getLogger(__name__)

    # Initialize modules
    face_recognizer = FaceRecognitionModule(KNOWN_FACES_DIR, TOLERANCE, MODEL)
    movement_tracker = MovementTrackingModule(ZONE_A_COORDS, ZONE_B_COORDS)
    database = DatabaseModule(DATABASE_PATH)

    # Set up video capture
    video_capture = cv2.VideoCapture(CAMERA_INDEX)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    logger.info("Starting the facial recognition door monitor.")

    try:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                logger.error("Failed to read frame from camera.")
                break

            # Face recognition
            face_locations, face_names = face_recognizer.recognize_faces(frame)

            # Movement tracking
            events = movement_tracker.update_positions(face_locations, face_names)

            # Log events
            for event in events:
                name = event['name']
                action = event['event']
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logger.info(f"{timestamp}: {name} has {action}.")
                database.log_event(name, action)

            # Display results
            if DISPLAY_VIDEO:
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # Draw rectangle around face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    # Draw label with name
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                cv2.imshow('Facial Recognition Door Monitor', frame)

                # Press 'q' to exit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except KeyboardInterrupt:
        logger.info("Application interrupted by user.")

    finally:
        # Release resources
        video_capture.release()
        if DISPLAY_VIDEO:
            cv2.destroyAllWindows()
        database.close()
        logger.info("Facial recognition door monitor stopped.")

if __name__ == '__main__':
    main()
