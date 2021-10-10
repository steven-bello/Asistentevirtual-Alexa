import os

def teamviewer():
    print ('Abriendo Team Viewer...')
    os.chdir(os.path.dirname("C:\\Users\\steve\\OneDrive\\Documentos\\Ejecutables\\"))
    os.system('TeamViewer.lnk')

if __name__ == "__main__":
    teamviewer()