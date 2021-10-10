import os

def powerpoint():
    print ('Abriendo Power Point...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('PowerPoint.lnk')

if __name__ == "__main__":
    powerpoint()