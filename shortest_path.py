
graph = {'A': {'B': 22, 'C': 9, 'D': 12}, 'B': {'C': 35, 'F': 36, 'H': 34},
         'C': {'A': 9, 'B': 35, 'E': 65, 'F': 42},
         'D': {'A': 12, 'C': 4, 'E': 33, 'I': 30}, 'E': {'C': 65, 'D': 33, 'F': 18, 'G': 23},
         'F': {'B': 36, 'C': 42, 'E': 18, 'G': 39, 'H': 24}, 'G': {'E': 23, 'F': 39, 'I': 21, 'H': 25},
         'H': {'B': 34, 'F': 24, 'G': 25, 'I': 19}, 'I': {'D': 30, 'G': 21, 'H': 19}}

start = 'A'
path = {}
adj_node = {}
queue = []
#initialize  all paths to inf and starting node to 0
for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)

path[start] = 0
while queue:
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]
            min_val = path[key_min]
    current = key_min
    queue.remove(current)

    for i in graph[current]:
        alternate = graph[current][i] + path[current]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = current

x = 'H'
print('The path between A to H')
print(x, end='--')

while True:
    x = adj_node[x]
    if x is None:
        print("")
        break
    print(x, end="--")


