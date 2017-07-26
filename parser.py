import math

def read_layer():
    """
    Returns array of strings with no borders
    Input example via stdin:
        ##########
        ###23S321#
        #11#21##2#
        #3##31231#
        #E2312####
        #23#######
        ##########
    Output example: 
        ["##23S321", "11#21##2", "3##31231", "E2312###", "23######"]
    On error it returns empty array and print error with logging 
    """
    print('Please enter your Maize:')
    maize = []
    level0 = input().lower()
    maize_len = len(level0)
    if len(set(level0)) != 1 or level0[0] != '#':
        print('\nThe Maize should be bordered by Walls(#) like this one\n        ##########\n        ###23S321#\n        #11#21##2#\n        #3##31231#\n        #E2312####\n        #23#######\n        ##########')
        return []
    while True:
        level = input().lower()
        if len(level) != maize_len or level[0] != '#' or level[maize_len - 1] != '#':
            print("Either level is too short or too long or it isn't borderd with #")
            return []
        if len(set(level)) == 1:
            break
        maize += [level[1:maize_len - 1]]

    return maize


def check_maize(maize_array):
    """
    check for the existence of only one start and one end
    and 0 < n <= Min(n,M)/2
    and check that there is no illegal character in them maize
    maize array example
    ["##23S321", "11#21##2", "3##31231", "E2312###", "23######"]
    return either True or false of if the array follows the rules
    no checks are made on the length of the maize or its height
    """
    start = 0
    end = 0
    M = len(maize_array)
    N = len(maize_array[0])
    n = math.ceil(min(M, N) / 2)
    for element in maize_array:
        for cell in element:
            if cell == 's':
                start += 1
            elif cell == 'e':
                end += 1
            elif cell == '#':
                continue
            else:
                if cell not in '0123456789':
                    return False
                if int(cell) > n or int(cell) <= 0:
                    return False

    if end != 1 or start != 1:
        return False
    return True


def array2graph(maize_array):
    """
        this converts the maize_array into a dictionary based graph and a dictionary of
        wieghts (number of steps required to move), start and end.
        graph is implemented this way
        https://www.python.org/doc/essays/graphs/
        return value (graph, weight, (startY, startX), (endY, endX))
        input example:
            ["##23S321", "11#21##2", "3##31231", "E2312###", "23######"]
        example output
            OMMITTED
        exmple output type
            ({}, {}, (int, int), (int, int))
    """
    start = tuple()
    end = tuple()
    weight = {}
    graph = {}
    imax = len(maize_array) - 1
    jmax = len(maize_array[0]) - 1
    for i in range(imax + 1):
        for j in range(jmax + 1):
            if maize_array[i][j] == '#':
                continue
            elif maize_array[i][j] == 's':
                start = (
                 i, j)
                weight[start] = 1
            elif maize_array[i][j] == 'e':
                end = (
                 i, j)
                weight[end] = 1
            else:
                weight[i, j] = int(maize_array[i][j])
            graph[i, j] = []
            if i > 0:
                if maize_array[i - 1][j] != '#':
                    graph[(i, j)] += [(i - 1, j)]
            if j > 0:
                if maize_array[i][j - 1] != '#':
                    graph[(i, j)] += [(i, j - 1)]
            if i < imax:
                if maize_array[i + 1][j] != '#':
                    graph[(i, j)] += [(i + 1, j)]
            if j < jmax:
                if maize_array[i][j + 1] != '#':
                    graph[(i, j)] += [(i, j + 1)]

    return (
     graph, weight, start, end)


def visualize(graph, weight, start, end, verbose=False):
    """
    for debug purposes only ... you know the rest
    """
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    import xdot
    window = xdot.DotWindow()
    dotcode = 'strict graph {\n'
    for node in graph:
        n = str(node) + '\\nSteps: ' + str(weight[node])
        if node == start:
            n = 'START ' + n
        elif node == end:
            n = 'END ' + n
        for node2 in graph[node]:
            n2 = str(node2) + '\\nSteps: ' + str(weight[node2])
            if node2 == start:
                n2 = 'START ' + n2
            elif node2 == end:
                n2 = 'END ' + n2
            dotcode += '"' + n + '"--"' + n2 + '";\n'

    dotcode += '"START ' + str(start) + '\\nSteps: ' + str(weight[start]) + '" [shape=Mdiamond, color=red];\n'
    dotcode += '"END ' + str(end) + '\\nSteps: ' + str(weight[end]) + '" [shape=Msquare, color=blue];\n'
    dotcode += '}'
    if verbose:
        print(dotcode)
    window.set_dotcode(dotcode)
    window.connect('delete-event', Gtk.main_quit)
    Gtk.main()
