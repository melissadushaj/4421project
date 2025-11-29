import os
import pygame
from Config.settings import SOUNDS_DIR, AUDIO_VOLUME, EMOTION_SOUNDS

class AudioManager:
    
    def __init__(self):
        
        pygame.mixer.init()
        pygame.mixer.music.set_volume(AUDIO_VOLUME)

        # preload file paths for quick lookup
        self.emotion_sounds = {}
        for emotion, filename in EMOTION_SOUNDS.items():
            path = SOUNDS_DIR / filename
            if path.exists():
                self.emotion_sounds[emotion] = str(path)
            else:
                print(f"[Audio] WARNING: sound file not found for {emotion}: {path}")

    def play_for_emotion(self, emotion: str, loop: bool = False):
        
        filepath = self.emotion_sounds.get(emotion)
        
        if not filepath:
            print(f"[Audio] No sound configured for emotion '{emotion}'")
            return
        
        pygame.mixer.music.stop()

        try:
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play(-1 if loop else 0)
            print(f"[Audio] Playing sound for emotion '{emotion}'")
        except Exception as e:
            print(f"[Audio] Error playing sound for {emotion}: {e}")

    def stop(self):
        pygame.mixer.music.stop()
        print("[Audio] Stopped all sounds")
