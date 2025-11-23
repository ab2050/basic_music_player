import pygame as pg
from pygame import mixer
import tkinter as tk
from tkinter import filedialog,messagebox
from queue import Queue

mixer.init()
global songqueue 
songqueue = Queue()

def addmusic():
    global path
    path = filedialog.askopenfilename()
    if path:
        s = path[path.rfind("/")+1:]
        currentSelection.config(text=s)
        songqueue.put(path)
        songs.insert(tk.END, s)

def playmusic():
    while songqueue.empty()!=True:
        playpath = songqueue.get()
        mixer.music.load(playpath)
        mixer.music.play()
        while mixer.music.get_busy():
            root.update()
        currentPlaying.config(text=path[path.rfind("/")+1:])
        songs.delete(0)
    currentPlaying.config(text="List is empty")

root = tk.Tk()
root.geometry("650x500")

currentSelection = tk.Label(text="")
currentSelection.pack()
currentPlaying = tk.Label(text="Nothing playing")
currentPlaying.pack()

openfiles = tk.Button(root,command=addmusic,text="Select song")
openfiles.pack()
songs = tk.Listbox(root,width=25,height=20)
songs.pack()
playmusicbutton = tk.Button(root,command=playmusic,text="Play all")
playmusicbutton.pack()
root.mainloop()