from re import search
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer

name = 'adri'

# Comienza a reconocer
listener = sr.Recognizer() 

#Inicialización de la librería pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')

#Colocación de la voz
engine.setProperty('voice', voices[0].id)

    #Este es un arreglo que permite imprimir en comsola un arreglo de las voces que exiten, En ESPAÑOL e INGLES
        # for i in voices:
        #     print(i)

#Función 
def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        # Abre el microfono para escuchar
        with sr.Microphone() as source:
            print("Escuchando")
        #Aquí realmente está escuchando lo que proviene del micrófono
            pc= listener.listen(source)
        #Ocupa los servicios de reconocimiento de google y esuche lo que viene de la variable "PC"
            rec = listener.recognize_google(pc, language="es")
        #Ahora vamos a decirle a nuestra computadora que le estamos hablando
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

    except:
        pass

    #Retorna la variable rec
    return rec

def run_adri():
    #El while permite seguir escuchando

    while True: 
        rec = listen()
        #Si decimos reproduce... hará lo siguiente...
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo "+music)
            talk("Reproduciendo "+music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            search = rec.replace('busca', '')
            #La búsqueda de Wikipedia será en español
            wikipedia.set_lang("es")
            #El método summary resume la búsqueda que queremos, el 1 es la cantidad de oraciones que queremos
            wiki = wikipedia.summary(search,1)
            print(search + ":" + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            #El strip corta el string vacío, evitar el espacio " 1:30"
            num = num.strip()
            talk("Alarma activada a las" + num + "horas")
            while True:
                #El now es para activar la fecha y hora de nuestra pc
                #El strftime se transorma en dateTime y el formato
                if datetime.datetime.now().strftime('%H:%M') == num:
                #El formato es en 24 hrs
                    print("Arriba flojo")
                    #Carga de música
                    mixer.init()
                    mixer.music.load("alarma.mp3")
                    mixer.music.play()
                    #Detener la alarma
                    if keyboard.read_key() == 's':
                        mixer.music.stop()
                        break 

if __name__ == '__main__':
    run_adri()


