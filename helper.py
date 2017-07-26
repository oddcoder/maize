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

def get_path(parents, start, end):
    if end not in parents:
        return []
    ret = [end]
    parent = end
    while parent != start:
        parent = parents[parent]
        ret.insert(0, parent)
    return ret

