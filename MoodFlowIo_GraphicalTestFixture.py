'''
Author: Alexander Kidd
Created: 12/19/20
Revised: 4/25/21
Version: 1.0
Description: A basic Tkinter graphical representation of uploaded/hard-coded algorithms
based on generating pseudo-random/specific colors to each pixel/square on the canvas.
Recommended settings: Python 3.7+

References:
https://codegolf.stackexchange.com/questions/124049/display-random-colored-pixels?noredirect=1&lq=1
https://www.kite.com/python/docs/tkinter.PhotoImage.put
'''
from tkinter import *
from random import *
import gc as gc
import numpy as np


# CONSTANTS
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 325
WINDOW_DIMENSIONS = {"width": WINDOW_WIDTH, "height": WINDOW_HEIGHT}
CANVAS_LENGTH = 300
CANVAS_DIMENSIONS = {"width": CANVAS_LENGTH, "height": CANVAS_LENGTH}
TILE_LENGTH = 8
TILES_PER_ROW = int(CANVAS_LENGTH / TILE_LENGTH)

# Play/pause state
global play_state
play_state = False

# Play button
global toggle_play_button

# Play button text
global play_button_text
play_button_text = "▶️Play"

# Random color fcn
global rand_color
rand_color = np.random.randint(0, 0xffffff)

# Reduce mem with global select tile x & y
global select_tile_x
global select_tile_y

# Random coordinate fcn
rand_coord = randrange

# Window/canvas setup
w = Tk()
w.title("Pinecone Graphical Test Fixture 1.0")
w.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
w.resizable(False, False)

# Create canvas & frame
c = Canvas(w, **CANVAS_DIMENSIONS)
c.configure(highlightthickness=0, borderwidth=0, bg='red')
c.pack(side="top", fill="none", expand=True)

# Continuously generate randomly-colored pixels at a random coord.
def play():
    global rand_color
    global select_tile_x
    global select_tile_y
    while True:
        select_tile_x = rand_coord(0, TILES_PER_ROW)
        select_tile_y = rand_coord(0, TILES_PER_ROW)
        c.itemconfig(TILE_ARRAY[select_tile_x][select_tile_y], fill=f"#{(hex(rand_color)[2:]).rjust(6, '0')}")
        rand_color = np.random.randint(0, 0xffffff)
        c.update()
        if play_state == False:
            break
    return

def pause():
    gc.collect()
    return

def toggle_play():
    global play_state
    if play_state == True:
        toggle_play_button['text']="▶️Play"
        play_state = False
        pause()
    else:
        toggle_play_button['text']="⏸️     Pause"
        play_state = True
        play()
    return

# Create controls & frame
controls_frame = Frame(w)
controls_frame.pack(side="bottom")
toggle_play_button = Button(controls_frame, text=play_button_text, borderwidth=1, relief="raised", command=toggle_play)
toggle_play_button.pack()

# Tile creation for reuse
TILE_ARRAY = [[0 for x in range(TILES_PER_ROW)] for y in range(TILES_PER_ROW)]
for j in range(TILES_PER_ROW):
    for i in range(TILES_PER_ROW):
        tile_x = i * TILE_LENGTH
        tile_y = j * TILE_LENGTH
        TILE_ARRAY[i][j] = c.create_rectangle(tile_x, tile_y, tile_x + 8, tile_y + 8, fill=f"#{(hex(rand_color)[2:]).rjust(6, '0')}")
        rand_color = np.random.randint(0, 0xffffff)

mainloop()
