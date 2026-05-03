import tkinter as tk
from tkinter import filedialog
import yt_dlp
import os

def select_folder():
    return filedialog.askdirectory(title="Select directory for downloaded files.")

def get_links(links_directory):
    links = []
    with open(links_directory, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                links.append(line)
    return links

def download_audio(link, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def main():
    root = tk.Tk()
    root.withdraw()

    final_directory = select_folder()
    if not final_directory:
        print("No directory selected")
        return

    ydl_opts = {
        'format': 'bestaudio/best',  # Best possible audio quality
        'outtmpl': os.path.join(final_directory, '%(title)s.%(ext)s'),  # Path + file name
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a'  # m4a codec for original quality
        }],
    }

    links = get_links("../links.txt")
    for link in links:
        download_audio(link, ydl_opts)

    print("Done")


if __name__ == "__main__":
    main()