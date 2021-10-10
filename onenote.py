import os

def onenote():
    print ('Abriendo One Note...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('OneNote.lnk')

if __name__ == "__main__":
    onenote()