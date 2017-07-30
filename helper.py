'''
input arguments:
graph: a dictionary of nodes , contains all possible neighbours of each node
weight: weight of node passed from search algorithms
node: (x,y) coordinates in a maze, x is row and y is column
remove node : variable to prevent node from moving to itself in case of even weight

output:
returns a list of possible moves from current node and its weight
a set to prevent repetitions
'''
def possible_moves(graph, weight, node, remove_node=True):
    childs = graph[node]
    if weight == 1:
        return childs
    ret = []
    for child in childs:
        ret += possible_moves(graph, weight - 1, child, False)
    ret = list(set(ret))
    if remove_node and node in ret:
        ret.remove(node)
    return ret
'''
function takes start, end and list of parents of all nodes in path
returns list ordered from 1st node after start and till then end node
'''
def get_path(parents, start, end):
    if end not in parents:
        return []
    ret = [end]
    parent = end
    while parent != start:
        parent = parents[parent]
        ret.insert(0, parent)
    return ret

