from speech_recognition import Microphone, Recognizer, UnknownValueError
import sys
import time
import pyttsx3
import pywhatkit
import webbrowser
import subprocess
import datetime
import pyjokes
# from os import urandom

global mi_asistente
mi_asistente = 'alexa'

global texto

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
        print('Te escucho...')
        recognizer = Recognizer()
        microfono = Microphone()
        with microfono:
            recognizer.adjust_for_ambient_noise(microfono)
        global source
        source = recognizer.listen_in_background(microfono, callback, phrase_time_limit=5)
        # source = recognizer.listen_in_background(microfono, callback)

def callback(recognizer, source):
    print('Reconociendo tu bellísima voz...')
    try:
        reconocer = recognizer.recognize_google(source, language='es-ES')
        texto = str(reconocer).lower()
        print('Has dicho: ' + texto)
        
        if (texto.__contains__('escucha') or 
            texto.__contains__('estás ahí') or 
            texto.__contains__('estas ahi')):
            print('HEY...sigo aquí')
            hey()

        if(texto.__contains__('detente') or
            texto.__contains__('adiós') or
            texto.__contains__('para')):
            talk('Entendido. Hasta luego.')
            detener()

        if(texto.__contains__(mi_asistente)):
            talk('He oido tu voz mi comandante')
            texto = texto.replace(mi_asistente, '')
            accion(texto)

    except UnknownValueError:
        print('////////// HABLA AHORA //////////')
        ahora()

def accion(texto: str):
    print('Reconociendo acción...')

    # Buscador
    if (texto.__contains__('busca')):
        order = texto.replace('busca', '')
        print('Buscando' +order)
        talk('Buscando' +order)
        pywhatkit.search(order)
        time.sleep(1)

    # Video
    elif (texto.__contains__('reproduce')):
        music = texto.replace ('reproduce', '')
        print('reproduciendo ahora ' +music)
        talk('reproduciendo ahora ' +music)
        pywhatkit.playonyt(music)
        time.sleep(1)

    # Musica
    elif(texto.__contains__('spotify')):
        print('abriendo spotify')
        talk('abriendo spotify...')
        webbrowser.open('https://open.spotify.com/')
        time.sleep(1)

    # Whatsapp
    elif(texto.__contains__('whatsapp')):
        print('abriendo whatsapp')
        talk('abriendo...')
        webbrowser.open('https://web.whatsapp.com/send?phone=+525613357058')
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

        # elif (texto.__contains__('un chiste')):
        #     print('contando chiste')
        #     aleatorio = urandom.randrange(2)
        #     print('chiste: ', str(aleatorio))

        #     if (aleatorio == 1):
        #         chiste_dos_ciegos()
        #     else:
        #         hey()

        #     time.sleep(1)
            # return

    # Miamor
    elif (texto.__contains__('fuera prendas')):
        print('tu primero mi amor')
        talk('tu primero mi amor')
        time.sleep(1)

    # Modo sexo
    elif (texto.__contains__('modo texto') or 
        texto.__contains__('modo sexo')):
        print('hora del delicioso')
        talk('hora del delicioso')
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
                talk('Ejecutando Microsoft Edge')
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
                talk('Ejecutando ' +texto)
                visualstudio()
                time.sleep(1)
            elif (texto.__contains__('musica') or 
                texto.__contains__('música')):
                talk('Ejecutando ' +texto)
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
        brave.open('https://www.youtube.com/watch?v=_KprFCkj2SU')
        time.sleep(1)

    elif (texto.__contains__('olvídalo')):
        print("No te entendi muy bien, vuelve a intentarlo")
        talk("No te entendi muy bien, vuelve a intentarlo")
        time.sleep(1)

# Funciones para abrir programas
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

# SONIDOS
def hey():
    hey = subprocess.Popen("py hey.py",shell=True)
    hey.communicate

def ahora():
    ahora = subprocess.Popen("py ahora.py",shell=True)
    ahora.communicate

# CHISTES
def chiste_dos_ciegos():
    chiste_dos_ciegos = subprocess.Popen("py chiste_dos_ciegos.py",shell=True)
    chiste_dos_ciegos.communicate

# TODO:
# def chiste():
#     print('contando chiste')
#     aleatorio = urandom.randrange(2)
#     print('chiste: ', str(aleatorio))

#     if (aleatorio == 1):
#         chiste_dos_ciegos()
#     else:
#         hey()
    
#     time.sleep(1)
#     return

# TODO:
# def hablar(texto: str):
#     print('hablando...')
#     audio = gTTS(text=texto, lang='es-us', slow=False)
#     audio.save('./detente.mp3')
#     # time.sleep(1)
#     # playsound('./chiste1.mp3')
#     return

# Detener escucha del asistente
def detener():
    sys.is_finalizing()
    sys.exit()

# Inicio del programa
if __name__ == "__main__":
    activarAsistente()

# Grabación de texto a audio 

# hablar('Hola, aqui lavan ropa     No    Uy, que sucios')
# hablar('Me detengo...')