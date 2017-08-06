from helper import *
'''
input arguments:
graph: dictionary of neighbours for each node in the maze
weights: dictionary of weights for each node in the maze

'''
def bfs(graph, weights, start, end):
    visited = set()
    unexplored = [start] # queue
    parents = {}
    node = None
    while len(unexplored) != 0 and node != end:
        node = unexplored.pop(0)
        if node in visited:
            continue
        visited.add(node)
        print(node)
        childs =  list(set(possible_moves(graph, weights[node], node)) - visited)
        #childs =  possible_moves(graph, weights[node], node)
        for child in childs:
            if child not in parents.keys():
                parents[child] = node
                unexplored.append(child)
    return get_path(parents, start, end)
