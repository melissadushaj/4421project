import time
from Hardware.audio import AudioManager

def main():
    print("[Test] Initializing AudioManager")
    audio = AudioManager()

    # pick one of the emotions you defined in EMOTION_SOUNDS
    test_emotion = "happy"

    print(f"[Test] Playing emotion sound: {test_emotion}")
    audio.play_for_emotion(test_emotion, loop=False)

    # let it play for a few seconds
    time.sleep(5)

    print("[Test] Stopping audio")
    audio.stop()

if __name__ == "__main__":
    main()
