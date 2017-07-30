from dfs import dfs
from parser import *
from bfs import *
from ucs import ucs

maze=read_layer()
graph,weights,start,end=array2graph(maze)

if check_maze(maze):

#    visualize(graph,weights,start,end)

    print("bfs")
    print(bfs(graph,weights,start,end))

    print("dfs")
    print(dfs(graph,weights,start,end))

    print("ucs")
    print(ucs(graph,weights,start,end))

else:
    print("error")
    


