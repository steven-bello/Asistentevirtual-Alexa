# pip install pip = instala pip una libreria util para instalar paquetes de python más facilmente
# pip install SpeechRecognition = instala la libreria para reconocimiento de voz
# pip install pyttsx3 = instala libreria que transforma el texto a voz
# pip install pywhatkit = instala el paquete que abre el navegador y busca contenido o videos en youtube, incluso puede mandar mensajes en whatsapp
# pip install pyWebBrowser = instala la dependencia que abre el navegador predeterminado usando el link de cualquier pagina que deeseemos
# pip install DateTime = instala la libreria que detalla la fecha y la hora de nuestra pc
# pip install pyjokes = instala la dependencia de chistes

# librerias que servirán para otros programas python
# pip install Py-OS = instala una dependencia que ejecuta códigos en nuestra pc, para abrir programas etc.
# pip install playsound = instala la libreria que reproduce audios en python

from speech_recognition import Microphone, Recognizer, UnknownValueError
import sys
import time
import pyttsx3
import pywhatkit
import webbrowser
import subprocess
import datetime
import pyjokes

global texto, mi_asistente
mi_asistente = 'alexa'

# funcion principal que siempre esta corriendo
def activarAsistente():
    escuchar()
    while True:
        time.sleep(1)

def talk(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# activacion del micro para la escucha en segundo plano
def escuchar():
        print('Modo escucha activado')
        recognizer = Recognizer()
        microfono = Microphone()
        with microfono:
            recognizer.adjust_for_ambient_noise(microfono)
        global source
        source = recognizer.listen_in_background(microfono, callback, phrase_time_limit=5)

def callback(recognizer, source):
    print('Reconociendo tu bellísima voz...')
    try:
        reconocer = recognizer.recognize_google(source, language='es-ES')
        texto = str(reconocer).lower()
        print('Has dicho: ' + texto)
    
        if (texto.__contains__('escucha') or 
            texto.__contains__('estás ahí')):
            print('HEY...sigo aquí')
            hey_sonido()
            time.sleep(1)

        if(texto.__contains__('detente') or
            texto.__contains__('adiós')):
            talk('Entendido. Hasta luego.')
            print('Entendido. Hasta luego.')
            detener()

        if(texto.__contains__(mi_asistente)):
            talk('He oido tu voz')
            texto = texto.replace(mi_asistente, '')
            accion(texto)
        
    except UnknownValueError:
        time.sleep(2)
    print('////////// HABLA AHORA //////////')

def accion(texto: str):
    print('Reconociendo acción...')

    # Buscador
    if (texto.__contains__('busca')):
        order = texto.replace('busca', '')
        print('Buscando ' +order)
        talk('Buscando' +order)
        pywhatkit.search(order)
        time.sleep(1)

    # Video en YT
    elif (texto.__contains__('reproduce')):
        music = texto.replace ('reproduce', '')
        print('Reproduciendo ahora ' +music)
        talk('Reproduciendo ahora' +music)
        pywhatkit.playonyt(music)
        time.sleep(1)

    # Musica en spotify
    elif(texto.__contains__('spotify')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo spotify')
        talk('Abriendo ' +texto )
        webbrowser.open('https://open.spotify.com/')
        time.sleep(1)

    # Youtube
    elif(texto.__contains__('youtube')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo youtube')
        talk('Abriendo ' +texto )
        webbrowser.open('https://www.youtube.com/')
        time.sleep(1)

    # Whatsapp
    elif(texto.__contains__('whatsapp')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo whatsapp')
        talk('Abriendo ' +texto)
        webbrowser.open('https://web.whatsapp.com/send?phone=+525613357058')
        time.sleep(1)

    # Netflix
    elif(texto.__contains__('netflix')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo netflix')
        talk('Abriendo ' +texto)
        webbrowser.open('https://www.netflix.com/browse')
        time.sleep(1)

    # Amazon prime video
    elif(texto.__contains__('amazon video') or
        texto.__contains__('amazon prime video')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo amazon prime video')
        talk('Abriendo ' +texto)
        webbrowser.open('https://www.primevideo.com/?_encoding=UTF8&language=es_ES')
        time.sleep(1)

    # Udemy
    elif(texto.__contains__('udemy') or
        texto.__contains__('demie')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo udemy')
        talk('Abriendo ' +texto)
        webbrowser.open('https://www.udemy.com/home/my-courses/learning/')
        time.sleep(1)

    # Keep
    elif(texto.__contains__('keep') or 
        texto.__contains__('google keep')):
        texto = texto.replace (mi_asistente, '')
        print('Abriendo google keep')
        talk('Abriendo ' +texto)
        webbrowser.open('https://keep.google.com/')
        time.sleep(1)

    # Dime
    elif(texto.__contains__('dime')):

        # Hora
        if (texto.__contains__('la hora')):
            hora = datetime.datetime.now().strftime('%I:%M %p')
            print("Son las " +hora)
            talk("Son las " +hora)
            time.sleep(1)

        # Fecha
        elif (texto.__contains__('la fecha')):
            fecha = datetime.datetime.now().strftime('%d/%m/%Y')
            print("Hoy es " +fecha)
            talk("Hoy es " +fecha)
            time.sleep(1)

        # Chistes
        elif (texto.__contains__('un chiste')):
            talk(pyjokes.get_joke('es'))
            time.sleep(1)

    # Ejecución de aplicaciones
    elif (texto.__contains__('ejecuta')):
        texto = texto.replace('ejecuta','')

        # Ejecución de excel
        if (texto.__contains__('excel')):
            time.sleep(1)
            talk('Ejecutando ' +texto)
            excel()
            time.sleep(1)

        # Ejecución de word
        elif (texto.__contains__('word')):
                time.sleep(1)
                talk('Ejecutando ' +texto)
                word()
                time.sleep(1)

        # Ejecución de navegadores 
        elif (texto.__contains__('navegador')):
            if (texto.__contains__('uno') or 
                texto.__contains__('1')):
                talk('Ejecutando Brave')
                brave()
                time.sleep(1)
            elif (texto.__contains__('dos') or 
                texto.__contains__('2')):
                talk('Ejecutando Edge')
                edge()
                time.sleep(1)

        # Ejecución de logitech
        elif (texto.__contains__('logi') or 
                texto.__contains__('logitech')):
                talk('Ejecutando ' +texto)
                logitech()
                time.sleep(1)

        # Ejecución de discord
        elif (texto.__contains__('discord')):
                talk('Ejecutando ' +texto)
                discord()
                time.sleep(1)

        # Ejecución de editores
        elif (texto.__contains__('editor de')):
            if (texto.__contains__('videos')):
                talk('Ejecutando Da Vinci')
                davinci()
                time.sleep(1)
            elif (texto.__contains__('codigo') or
                texto.__contains__('código')):
                talk('Ejecutando Visual Studio Code')
                visualstudio()
                time.sleep(1)
            elif (texto.__contains__('musica') or 
                texto.__contains__('música')):
                talk('Ejecutando Fl studio')
                flstudio()
                time.sleep(1)

        # Ejecución de onenote
        elif (texto.__contains__('one note') or 
                texto.__contains__('onenote')):
                talk('Ejecutando ' +texto)
                onenote()
                time.sleep(1)

        # Ejecución de virtualbox
        elif (texto.__contains__('virtual box')):
                talk('Ejecutando ' +texto)
                virtualbox()
                time.sleep(1)

        # Ejecución de powerpoint
        elif (texto.__contains__('powerpoint') or 
                texto.__contains__('power point')):
                talk('Ejecutando ' +texto)
                powerpoint()
                time.sleep(1)

        # Ejecución de teamviewer
        elif (texto.__contains__('teamviewer')):
                talk('Ejecutando ' +texto)
                teamviewer()
                time.sleep(1)

        # Ejecución de telegram
        elif (texto.__contains__('telegram')):
                talk('Ejecutando ' +texto)
                telegram()
                time.sleep(1)

    elif (texto.__contains__('creditos')):
        brave.open('https://www.instagram.com/stevenbello_/')
        time.sleep(1)

    elif (texto.__contains__('olvídalo')):
        print("No te entendi muy bien, vuelve a intentarlo")
        talk("No te entendi muy bien, vuelve a intentarlo")
        time.sleep(1)

# Funciones para abrir programas -------------------->
def excel():
    excel = subprocess.Popen("py excel.py",shell=True)
    excel.communicate

def word():
    word = subprocess.Popen("py word.py",shell=True)
    word.communicate

def brave():
    brave = subprocess.Popen("py brave.py",shell=True)
    brave.communicate

def logitech():
    logitech = subprocess.Popen("py logitech.py",shell=True)
    logitech.communicate

def discord():
    discord = subprocess.Popen("py discord.py",shell=True)
    discord.communicate

def davinci():
    davinci = subprocess.Popen("py davinci.py",shell=True)
    davinci.communicate

def flstudio():
    flstudio = subprocess.Popen("py flstudio.py",shell=True)
    flstudio.communicate

def edge():
    edge = subprocess.Popen("py edge.py",shell=True)
    edge.communicate

def onenote():
    onenote = subprocess.Popen("py onenote.py",shell=True)
    onenote.communicate

def virtualbox():
    virtualbox = subprocess.Popen("py virtualbox.py",shell=True)
    virtualbox.communicate

def powerpoint():
    powerpoint = subprocess.Popen("py powerpoint.py",shell=True)
    powerpoint.communicate

def teamviewer():
    teamviewer = subprocess.Popen("py teamviewer.py",shell=True)
    teamviewer.communicate

def telegram():
    telegram = subprocess.Popen("py telegram.py",shell=True)
    telegram.communicate

def visualstudio():
    visualstudio = subprocess.Popen("py visualstudio.py",shell=True)
    visualstudio.communicate

# SONIDOS ---------------------------------------->
def hey_sonido():
    hey = subprocess.Popen("py hey_sonido.py",shell=True)
    hey.communicate

def habla_sonido():
    habla = subprocess.Popen("py habla_sonido.py",shell=True)
    habla.communicate

# TODO:
# CHISTES ---------------------------------------->
def chiste_dos_ciegos():
    chiste_dos_ciegos = subprocess.Popen("py chiste_dos_ciegos.py",shell=True)
    chiste_dos_ciegos.communicate

# Detener escucha del asistente
def detener():
    sys.is_finalizing()
    sys.exit()

# Inicio del programa
if __name__ == "__main__":
    activarAsistente()
