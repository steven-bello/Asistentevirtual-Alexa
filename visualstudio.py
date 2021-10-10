import os

def visualstudio():
    print ('Abriendo Visual Studio Code...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('VisualStudio.lnk')

if __name__ == "__main__":
    visualstudio()