import sys #sistema
import time #trabalhar com o tempo
import random #trabalhar com numeros aleatorios
import watchdog #monitorar arquivos

import os #interagir sistema operacional
import shutil #faz andar de pasta pra outra

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"

from_dir = "C:/Users/Izabelli/Desktop/pasta"
to_dir = "C:/Users/Izabelli/Desktop/final"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
# Classe Gerenciadora de Eventos
#Esta é uma classe predefinida que irá gerenciarneventos do sistema de arquivos como criação, modificação, etc.
class FileMovementHandler(FileSystemEventHandler):
#: é chamado quando um arquivo ou diretório é criado.
    def on_created(self, event): #é chamado quando um arquivo ou diretório é criado.

        name, extension = os.path.splittext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Baixado" + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Diretório Existe...")
                    print("Movendo" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Criando Diretório...")
                    os.makedirs(path2)
                    print("Movendo" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    #Podemos usar um loop while com “True” como condição para continuar imprimindo até que o programa pare de executar.
    while True:
        time.sleep(2) #atraso de 2 segundos para imprimir “executando…” usando o método time.sleep().

        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()