import os

def logitech():
    print ('Abriendo Logitech Options...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('Logitech.lnk')

if __name__ == "__main__":
    logitech()