# Facial Recognition Door Monitor

## Overview

This project uses facial recognition to detect and log when individuals enter or exit through a door. It determines the direction of movement based on predefined zones within the camera's field of view.

## Project Structure

- `main.py`: Main script to run the application.
- `config.py`: Configuration variables and parameters.
- `face_recognition_module.py`: Handles face detection and recognition.
- `movement_tracking_module.py`: Manages movement tracking and direction determination.
- `database_module.py`: Interfaces with the SQLite database for logging events.
- `requirements.txt`: Python package requirements.
- `README.md`: Project documentation.

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- A compatible camera (e.g., USB webcam, Raspberry Pi camera)
- Internet connection for installing packages

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/facial_recognition_door_monitor.git
   cd facial_recognition_door_monitor
