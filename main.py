from _thread import start_new_thread as thread
from dfs import dfs
from parser import *
from bfs import *
from ucs import ucs
from gen import *
maze = []
while True:
    try:
        command = input("> ")
    except:
        continue
    command = command.strip()
    if command == "":
        continue
    if command.lower() in ["exit", "q"]:
        exit()
    if command.lower() == "input":
        maze=read_layer()
    elif command.lower() == "rand":
        try:
            x = int(input("Length [Default: 8]: "))
        except:
            x = 8
        try:
            y = int(input("Width [Default: 8]: "))
        except:
            y = 8
        print(generate(x,y,40,bfs))
    elif command.lower() == "visualize":
        graph,weights,start,end=array2graph(maze)
        try:
            thread(visualize, (graph,weights,start,end))
        except:
            print("Unfortunately visualiztion wont work because you need xdot\n\ttry: `pip install xdot`")

    else:
        if command.lower() not in ["bfs", "dfs", "ucs"]:
            print("Unknown command")
            continue
        if not check_maze(maze):
            continue
        graph,weights,start,end=array2graph(maze)
        if command.lower() == "bfs":
            print(bfs(graph,weights,start,end))
        elif command.lower() == "dfs":
            print(dfs(graph,weights,start,end))
        elif command.lower() == "ucs":
            print(ucs(graph,weights,start,end))
