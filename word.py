import os

def word():
    print ('Abriendo Word...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('Word.lnk')

if __name__ == "__main__":
    word()