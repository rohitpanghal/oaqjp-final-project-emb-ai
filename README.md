# Final Project
# Emotion Detection Flask App

A Flask web application for detecting emotions from input text or images. This project includes a backend service, an emotion detection module, a web interface, and supporting static assets for client-side interaction.

## Project Details

- **Name:** Emotion Detection Flask App
- **Description:** A simple emotion recognition web app that uses Flask to serve a frontend and process emotion detection requests through a Python module.
- **Backend:** Flask app in `server.py` with emotion detection logic in `EmotionDetection/emotion_detection.py`
- **Frontend:** HTML user interface in `templates/index.html` and JavaScript in `static/mywebscript.js`
- **Test:** Contains `test_emotion_detection.py` for validating emotion detection functionality.

## Features

- Submit text or image input for emotion detection
- Real-time response from the Flask backend
- Modular architecture separating web routing and emotion detection logic
- Easy setup and extension for additional input types or models

## Project Structure

- `server.py` - Main Flask server entry point
- `EmotionDetection/` - Emotion detection module package
- `templates/index.html` - Web page served by Flask
- `static/mywebscript.js` - Client-side JavaScript for UI interaction
- `test_emotion_detection.py` - Unit tests for emotion detection

## Getting Started

1. Create and activate a Python virtual environment.
2. Install Flask and any other required dependencies.
3. Run the app with:

```bash
python server.py
```

4. Open the app in your browser at `http://127.0.0.1:5000/`.

## Notes

- Update dependencies as needed for your environment.
- Add a requirements file if you want reproducible installation steps.
