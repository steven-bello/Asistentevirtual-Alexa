import os

def virtualbox():
    print ('Abriendo Virtual Box...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('VirtualBox.lnk')

if __name__ == "__main__":
    virtualbox()