import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

def pobierz_i_konwertuj():
    try:
        url = entry_url.get()
        if not url:
            raise ValueError("URL nie może być pusty")

        folder_zapis = filedialog.askdirectory()
        if not folder_zapis:
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(folder_zapis, '%(title)s.%(ext)s'),
            'ffmpeg_location': r'D:\Aplikacje\ffmpeg\ffmpeg\bin\ffmpeg.exe',  # Ścieżka do pliku ffmpeg.exe
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            tytul = info_dict.get('title', None)
            messagebox.showinfo("Sukces", f"Pobrano i skonwertowano plik audio: {tytul}")

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")

app = tk.Tk()
app.title("YouTube to MP3 Downloader")

frame = tk.Frame(app)
frame.pack(pady=20, padx=20)

label_url = tk.Label(frame, text="URL wideo:")
label_url.grid(row=0, column=0, padx=5, pady=5)

entry_url = tk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, padx=5, pady=5)

button_pobierz = tk.Button(frame, text="Pobierz i konwertuj", command=pobierz_i_konwertuj)
button_pobierz.grid(row=1, columnspan=2, pady=10)

app.mainloop()
