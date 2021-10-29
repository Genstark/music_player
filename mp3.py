import tkinter as tk
import pygame
import os


#start funtion area 
def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/gauta/Documents/songs/The Script - Hall Of Fame.mp3")
    pygame.mixer.music.play()

def pause(task):
    global pause_button

    if task == 0:
        pygame.mixer.music.pause()
        pause_button.configure(text="CONTINUE")
        pause_button.configure(command=lambda task = 1: pause(task))

    elif task == 1:
        pygame.mixer.music.unpause()
        pause_button.configure(text="PAUSE")
        pause_button.configure(command=lambda task = 0: pause(task))

def stop(number):
    global pause_button
    pygame.mixer.music.stop()
    pause_button.configure(text="CONTINUE")
    pause_button.configure(command=lambda task = number: pause(task))

def next():
    print("hello world")
#end of function area

#start graphical user interface of mp3 player

player = tk.Tk()
player.title("MP3 PLAYER")
player.minsize(340,380)

#variable section

song_list = []

#end variable section

songlist = tk.Listbox(player,
                    borderwidth=4)

for path, folder, file in os.walk("C:/Users/gauta/Documents"):
    for files in file:
        if files.endswith("mp3"):
            song_list.append(os.path.join(path,files))
            songlist.insert(0,files)

print(song_list)
songlist.pack(fill="x")


play_button = tk.Button(player,
                        text="PLAY",
                        font=("times new roman",12,"bold"),
                        borderwidth=2,
                        height=2,
                        command=play)
play_button.pack(fill="x")

pause_button = tk.Button(player,
                        text="PAUSE",
                        font=("times new roman",12,"bold"),
                        borderwidth=2,
                        height=2,
                        command=lambda task = 0: pause(task))   
pause_button.pack(fill="x")

stop_button = tk.Button(player,
                        text="STOP",
                        font=("times new roman",12,"bold"),
                        borderwidth=2,
                        height=2,
                        command=lambda num = 1: stop(num))
stop_button.pack(fill="x")

next_button = tk.Button(player,
                        text="NEXT",
                        font=("times new roman",12,"bold"),
                        borderwidth=2,
                        height=2,
                        command=next)
next_button.pack(fill="x")
#stop grphical user interface of mp3 player

#end of program
player.mainloop()