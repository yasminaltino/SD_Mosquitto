from gtts import gTTS
import playsound


class SpeakController:
    def talk(sentence: str):
        tts = gTTS(sentence)
        tts.save("audio.mp3")
        playsound.playsound("audio.mp3")
        
    