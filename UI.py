from maze import *
from tkinter import *
# from tkinter import font
import tkinter.font as font

# font.families()

#buttonFont = font.Font(family='Courier', size=16, weight='bold')

# buttons:

generate_maze_button = tkinter.Button(master=window, text="Generate random maze", command=generate_random_maze)
generate_maze_button.config(bg="#51557E", fg="white", font="Philosopher")
generate_maze_button.grid(padx=20, pady=70, row=0, column=0, sticky='nsew')

bfs_button = tkinter.Button(master=window, text="Start BFS", command=play_bfs)
bfs_button.config(bg="#51557E", fg="white", font="Philosopher")
bfs_button.grid(padx=20, pady=70, row=1, column=0, sticky='nsew')

Shortest_path_button = tkinter.Button(master=window, text="Shortest path", command=shortest_path)
Shortest_path_button.config(bg="#51557E", fg="white", font="Philosopher")
Shortest_path_button.grid(padx=20, pady=70, row=2, column=0, sticky='nsew')

dfs_button = tkinter.Button(master=window, text="Start DFS", command=play_dfs)
dfs_button.config(bg="#51557E", fg="white", font="Philosopher")
dfs_button.grid(padx=2, pady=70, row=1, columnspan=8, column=11, sticky='nsew')

clear_maze_button = tkinter.Button(master=window, text="Clear Maze", command=clear_maze)
clear_maze_button.config(bg="#51557E", fg="white", font="Philosopher")
clear_maze_button.grid(padx=20, pady=70, columnspan=3, rowspan=3, row=2, column=11, sticky='nsew')


def prevPage():
    window.destroy()
    import home_page


back_to_home_button = Button(
    master=window,
    text="Back to Home",
    font="Philosopher",
    command=prevPage
)
back_to_home_button.config(bg="#51557E", fg="white", font="Philosopher")
back_to_home_button.grid(padx=20, pady=70, row=8, column=11, sticky='nsew')

window.mainloop()
