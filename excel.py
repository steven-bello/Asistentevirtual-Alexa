import os

def excel():
    print ('Abriendo Excel...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('Excel.lnk')

if __name__ == "__main__":
    excel()


# OPCION 2
# import os
# import subprocess

# def main():
#     print ('Abriendo Excel...')
#     os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
#     os.system('Excel.lnk')
#     print ('Ejecutando Excel')
#     os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\RespaldoWD\\CODE\\PYTHON\\"))
#     alexa()

# def alexa():
#     alexa = subprocess.Popen("py MiAlexa.py",shell=True)
#     alexa.communicate

# if __name__ == "__main__":
#     main()