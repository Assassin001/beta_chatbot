import tkinter as tk
from tkinter import ttk
import pygame

def play1():
    import tkinter as tk
    from tkinter import ttk
    import pygame

    def play_music(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def stop_music():
        pygame.mixer.music.stop()
        progress_bar["value"] = 0

    def update_progress_bar():
        if pygame.mixer.music.get_busy():
            position = pygame.mixer.music.get_pos() / 1000  # Get current position in seconds
            progress = int((position / music_duration) * 100)
            progress_bar["value"] = progress
            root.after(100, update_progress_bar)  # Update progress bar every 100 milliseconds
        else:
            progress_bar["value"] = 0

    def start_music():
        file_path = "b.mp3"  # Replace with the path to your music file
        play_music(file_path)
        global music_duration
        music_duration = pygame.mixer.Sound(file_path).get_length()
        update_progress_bar()

    root = tk.Tk()
    root.title("Music Player with Progress Bar")

    # Create and place the progress bar
    progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
    progress_bar.pack(pady=10)

    # Button to start playing the music
    start_button = tk.Button(root, text="Start Music", command=start_music)
    start_button.pack(pady=10)

    # Button to stop the music
    stop_button = tk.Button(root, text="Stop Music", command=stop_music)
    stop_button.pack(pady=10)

    root.mainloop()

