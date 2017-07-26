import random
import math
from parser import *
from bfs import *
from ucs import *
def generate(l, w, d, search):
    """
    This function generates a maze with length l width w and and walls density
    d and search algorithm s
    d should be number from 0 to 100
    """
    if l > 18 and w > 18:
        print("both dimentions can't be above 18")
        return ""
    if d < 3 or d > 100:
        print ("d should be between 3 and 100")
    maze_list,start,end = get_trivial_maze(l,w,search)
    walls = [(i,j)for i in range(l) for j in range(w)]
    random.shuffle(walls)
    walls.remove(start)
    walls.remove(end)
    old_weight = 0
    wallcount = 0
    while wallcount*100/(l*w) < d or len(walls) == 0:
        old_weight = maze_list[walls[0][0]][walls[0][1]]
        maze_list[walls[0][0]][walls[0][1]] = "#"
        maze = array2maze(maze_list)
        graph, weight, start, end = array2graph(maze)
        solution = search(graph, weight, start, end)
        if not connected(graph) or  solution == []:
            maze_list[walls[0][0]][walls[0][1]] = old_weight
        else:
            wallcount += 1
        walls.pop(0)
    maze = "#"*( w + 2) + "\n"
    for line in array2maze(maze_list):
        maze += "#" + line + "#\n"
    maze +="#"*( w + 2)
    return maze

def connected(graph):
    visited = {i:False for i in graph.keys()}
    unexplored = [list(graph.keys())[0]]
    while len(unexplored) != 0:
        node = unexplored.pop()
        if visited[node]:
            continue
        visited[node] = True
        unexplored += graph[node]
    return False not in visited.values()

def get_trivial_maze(l,w,search):
    n = math.ceil(min(l,w)/2.0)
    maze_list = []
    filled = False
    maze = [] 
    solution = []
    start = (random.randrange(l), random.randrange(w))
    end = start
    while end[0] == start[0] or end[1] == start[1]:
        end = (random.randrange(l), random.randrange(0, w))
    while len(solution) == 0:
        for i in range(l):
            maze_list.append([])
            for _ in range(w):
                maze_list[i].append(random.randint(1, n))
        maze_list[start[0]][start[1]] = "s"
        maze_list[end[0]][end[1]] = "e"
        maze = array2maze(maze_list)
        graph, weight, start, end = array2graph(maze)
        solution = search(graph, weight, start, end)
    return maze_list,start,end
