from linkedlist import Node
from tkinter import *
from tkinter import ttk
import os
from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames
import pygame
from mutagen.id3 import ID3
from ttkthemes import themed_tk as tk

root = tk.ThemedTk()
root.get_themes()
root.set_theme('plastik')
root.title("Music Player")
root.iconbitmap(r"musicicon_gxm_icon.ico")
root.geometry("900x450")
root.maxsize(900,450)
root.configure(background='yellow')


leftframe = ttk.Frame(root, relief=RAISED, borderwidth=1)
leftframe.place(x=600, y=60)
Label(leftframe, text="Songs", font=("Verdana", 10)).pack(side=TOP, pady=10)
listbox = Listbox(leftframe)
listbox.pack()
frame = ttk.Frame(root, relief=RAISED, borderwidth=1)
frame.place(y=100, x=190)
# frame.pack()
frame1 = ttk.Frame(root, relief=RAISED, borderwidth=1)
frame1.place(y=200, x=150)




playimage = PhotoImage(file="001-resume.png")
stopimage = PhotoImage(file="006-stop.png")
resumeimage = PhotoImage(file="005-end.png")
pauseimage = PhotoImage(file="004-pause-button.png")
nextimage = PhotoImage(file="003-fast-forward-button.png")
previmage = PhotoImage(file="002-fast-rewind-button.png")



pygame.mixer.init()
songlist = []
llist = Node()
addimage = PhotoImage(file="007-plus.png")
add = ttk.Button(leftframe,image=addimage, width=50)
add.pack()

def getfile(event):
    file = list(askopenfilenames(initialdir=os.getcwd(), title='Select songs'))

    try:
        for f in file:
            if f.endswith('.mp3'):
                realdir = os.path.realpath(f)
                audio = ID3(realdir)
                songlist.append(f)
                listbox.insert('end',audio['TIT2'].text[0])
                llist.add(f)

    except:
        pass


def nextsong(event):
    try:
        if llist.head.next is None:
            return
        llist.head = llist.head.next
        pygame.mixer.music.load(llist.head.data)
        pygame.mixer.music.play()
    except AttributeError as e:
        pass


def prevsong(event):
    try:
        if llist.head.prev is None:
            return
        llist.head = llist.head.prev
        pygame.mixer.music.load(llist.head.data)
        pygame.mixer.music.play()
    except AttributeError as e:
        pass


def playthis(event):
    try:
        pygame.mixer.music.load(llist.head.data)
        pygame.mixer.music.play()
    except AttributeError as e:
        pass

def stopsong(event):
    try:
        pygame.mixer.music.stop()
    except AttributeError as e:
        pass

def pausesong(event):
    try:
        pygame.mixer.music.pause()
    except AttributeError as e:
        pass

def resume(event):
    try:
        pygame.mixer.music.unpause()
    except AttributeError as e:
        pass

def set_vol(val):
    volume = int(val)/100
    pygame.mixer.music.set_volume(volume)






play = ttk.Button(frame,image=playimage,  width=50)
play.pack(side=LEFT)
prevb = ttk.Button(frame1,image=previmage, width=50)
prevb.pack(side=LEFT)
stop = ttk.Button(frame,image=stopimage, width=50)
stop.pack(side=LEFT)
pause = ttk.Button(frame1,image=pauseimage,  width=50)
pause.pack(side=LEFT)
upause = ttk.Button(frame1,image=resumeimage,  width=50)
upause.pack(side=LEFT)
nextb = ttk.Button(frame1, image=nextimage,  width=50)
nextb.pack(side=LEFT)
scale = Scale(root, from_=0, to=100, orient_=HORIZONTAL, command=set_vol)
scale.set(70)
scale.place(y=175, x=400)

add.bind("<Button-1>",getfile)
play.bind("<Button-1>",playthis)
nextb.bind("<Button-1>",nextsong)
prevb.bind("<Button-1>",prevsong)
stop.bind("<Button-1>",stopsong)
upause.bind("<Button-1>",resume)
pause.bind("<Button-1>",pausesong)





root.mainloop()

