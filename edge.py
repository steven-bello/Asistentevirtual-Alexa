import os

def edge():
    print ('Abriendo Microsoft Edge...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('MicrosoftEdge.lnk')

if __name__ == "__main__":
    edge()