import eel
eel.init('templates')
import g4f

g4f.check_version = False  # Disable automatic version checking

@eel.expose
def getResponse(content):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
    )  # Alternative model setting
    return response

@eel.expose
def getMessage():
    return "Привет!"

eel.start('main.html')