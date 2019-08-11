import pyttsx3


def tts(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()


tts("好吧哈哈哈哈，我等你啊")
