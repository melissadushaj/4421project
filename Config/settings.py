from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOUNDS_DIR = BASE_DIR / "Sounds"

# Audio settings.
AUDIO_VOLUME = 0.7  # 0.0 - 1.0

# Display settings.
# The LCD is 240x320 with ST7789 controller.
# Don't want to hand-draw 240x320 faces.
# Define a smaller grid for the "pixel art" face then scale.
FACE_COLS = 16   
FACE_ROWS = 16   

# Brightness percentage for the backlight.
BRIGHTNESS = 60 

# List of supported emotions.
EMOTIONS = [
    "happy",
    "surprised",
    "empathetic",
    "confused",
    "sad",
    "sleeping",
]

# Mapping from emotion to sound effect.
EMOTION_SOUNDS = {
    "happy": "happy_robotic.mp3",
    "surprised": "sparkle_se.mp3",
    "empathetic": "empathetic.mp3",
    "confused": "confused.mp3",
    "sad": "sad_face_squish.mp3",
    "sleeping": "calming_music.mp3",
}

# List of emotions used by the app loop
EMOTIONS = list(EMOTION_SOUNDS.keys())
