import os

def brave():
    print ('Abriendo Brave...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('Brave.lnk')

if __name__ == "__main__":
    brave()


# opcion 2
# import os
# import subprocess

# def main():
#     print ('Abriendo Brave...')
#     os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
#     os.system('Brave.lnk')
#     print ('Ejecutando Brave')
#     os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\RespaldoWD\\CODE\\PYTHON\\"))
#     alexa()

# def alexa():
#     alexa = subprocess.Popen("py MiAlexa.py",shell=True)
#     alexa.communicate

# if __name__ == "__main__":
#     main()