from gtts import gTTS
import playsound
import os
import numpy as np
import sounddevice as sd

class SpeakController:
    def talk(sentence: str):
        tts = gTTS(sentence)
        tts.save("audio.mp3")
        playsound.playsound("audio.mp3")
        
    # def alarm():
    #     duration = 1.0  # segundos
    #     freq = 1000     # Hz
    #     sample_rate = 44100
    #     t = np.linspace(0, duration, int(sample_rate * duration), False)
    #     tone = 0.5 * np.sin(2 * np.pi * freq * t)
    #     sd.play(tone, sample_rate)
    #     sd.wait()