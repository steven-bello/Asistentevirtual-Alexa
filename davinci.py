import os

def davinci():
    print ('Abriendo Da Vinci Resolve...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('DaVinci.lnk')

if __name__ == "__main__":
    davinci()
