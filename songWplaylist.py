import pygame as pg
from pygame import mixer
import tkinter as tk
from tkinter import filedialog,messagebox
from queue import Queue
from collections import deque
import json

mixer.init()
global songqueue
global playlist
songqueue = deque()
playlist = deque()

def addmusic():
    global path
    path = filedialog.askopenfilename()
    if path:
        s = path[path.rfind("/")+1:]
        currentSelection.config(text=s)
        songqueue.append(path)
        songs.insert(tk.END, s)

def playmusic():
    while songqueue:
        path = songqueue.popleft()
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():
            root.update()
        currentPlaying.config(text=path[path.rfind("/")+1:])
        songs.delete(0)
    currentPlaying.config(text="List is empty")

def makeplaylist():
    global playlist, songqueue
    playlist= songqueue.copy()
    data = list(playlist)
    with open("E:\\filepath_here\\playlist.json","w") as f:
        json.dump(data,f)

def playFromplaylist():
    global songqueue
    with open("E:\\filepath_here\\playlist.json","r") as f:
        data = json.load(f)
    songqueue = deque(data)
    playerlab = tk.Label(text="Playing a playlist")
    playerlab.pack()
    playmusic()

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

turnintoplaylist = tk.Button(root,command=makeplaylist,text="Turn this into a playlist")
turnintoplaylist.pack()
playlistplayer = tk.Button(root, command=playFromplaylist, text="Play last playlist")
playlistplayer.pack()

root.mainloop()
