import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "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"

#


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower(0)          
    except:
        pass
    return rec



def escuchar():
    rec = listen()
    print("Usuario: ",rec)
    if rec != "salir":
        pregunta = rec
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "Eres un chatbot que siempre me preguntara cuando terminemos de hablar si necesito algo mas"},
             {"role": "user", "content": pregunta},
            ]
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        print("Chat: ",result)
        talk(result)
        escuchar()
    else:
        return
    

talk("¿En que puedo ayudarte?")
print("¿En que puedo ayudarte?")
escuchar()
