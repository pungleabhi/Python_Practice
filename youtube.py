from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # get highest quality stream
        stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()
    
    if save_dir:
        print("Started Download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")