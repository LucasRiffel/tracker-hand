from tkinter import Tk, Label, Entry, Button, filedialog
import yt_dlp

def baixar_video(url, diretorio):
    try:
        ydl_opts = {
            'outtmpl': f'{diretorio}/%(title)s.%(ext)s',  # Formato do nome do arquivo
            'format': 'best'  # Formato de vídeo de melhor qualidade
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    diretorio_entry.delete(0, 'end')
    diretorio_entry.insert(0, diretorio)

def iniciar_download():
    url = url_entry.get()
    diretorio = diretorio_entry.get()
    baixar_video(url, diretorio)

def fechar_janela():
    root.destroy()

root = Tk()

Label(root, text="URL do vídeo:").pack()
url_entry = Entry(root, width=50)
url_entry.pack()

Label(root, text="Diretório de download:").pack()
diretorio_entry = Entry(root, width=50)
diretorio_entry.pack()

Button(root, text="Selecionar diretório", command=selecionar_diretorio).pack()
Button(root, text="Iniciar download", command=iniciar_download).pack()
Button(root, text="Fechar", command=fechar_janela).pack()

root.mainloop()
