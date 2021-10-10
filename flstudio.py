import os

def flstudio():
    print ('Abriendo FL Studio...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('FLStudio.lnk')

if __name__ == "__main__":
    flstudio()