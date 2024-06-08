from tkinter import Tk, Label, Entry, Button, filedialog
from pytube import YouTube

def baixar_audio(url, diretorio):
    youtube = YouTube(url)
    audio_stream = youtube.streams.get_audio_only()
    audio_stream.download(diretorio)

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    diretorio_entry.delete(0, 'end')
    diretorio_entry.insert(0, diretorio)

def iniciar_download():
    url = url_entry.get()
    diretorio = diretorio_entry.get()
    baixar_audio(url, diretorio)

root = Tk()

Label(root, text="URL do vídeo:").pack()
url_entry = Entry(root, width=50)
url_entry.pack()

Label(root, text="Diretório de download:").pack()
diretorio_entry = Entry(root, width=50)
diretorio_entry.pack()

Button(root, text="Selecionar diretório", command=selecionar_diretorio).pack()
Button(root, text="Iniciar download", command=iniciar_download).pack()

root.mainloop()
