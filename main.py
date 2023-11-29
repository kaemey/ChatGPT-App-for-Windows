import eel
eel.init('templates')
import g4f

g4f.check_version = False  # Disable automatic version checking
context = list()

@eel.expose
def getResponse(content):
    context.append({"role": "user", "content": content})
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=context,
    )  # Alternative model setting
    context.append({"role": "assistant", "content": response})
    return response

eel.start('main.html')
