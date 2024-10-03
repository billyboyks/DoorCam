# config.py

# Camera settings
CAMERA_INDEX = 0  # Default camera index
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Zones definition (coordinates based on your camera's field of view)
ZONE_A_COORDS = ((0, FRAME_HEIGHT // 2), (FRAME_WIDTH, FRAME_HEIGHT))  # Zone A: Near the door
ZONE_B_COORDS = ((0, 0), (FRAME_WIDTH, FRAME_HEIGHT // 2))             # Zone B: Inside area

# Face recognition settings
KNOWN_FACES_DIR = 'known_faces'  # Directory with known faces
TOLERANCE = 0.6                  # Face recognition tolerance
MODEL = 'hog'                    # 'hog' or 'cnn' for face detection model

# Database settings
DATABASE_PATH = 'event_log.db'

# Logging settings
LOG_LEVEL = 'INFO'               # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'

# Display settings
DISPLAY_VIDEO = True             # Set to False if you don't want to display the video window
