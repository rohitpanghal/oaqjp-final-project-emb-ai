import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from EmotionDetection import emotion_detector

def test_emotion_detector():
    """Test dominant emotions."""

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected in test_cases.items():
        response = emotion_detector(statement)
        actual = response["dominant_emotion"]

        print(f"Testing: '{statement}' -> expected: '{expected}', actual: '{actual}'")
        assert actual == expected

    print("All tests passed!")


test_emotion_detector()