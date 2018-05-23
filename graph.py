from sys import argv
import re

file = open(argv[1], "r");
p = re.compile("\d+");

vertices, edges = map(int, p.findall(file.readline()))
graph = [[0]*vertices for _ in range(vertices)]

for i in range(edges):
    u, v, weight = map(int, p.findall(file.readline()))
    graph[u][v] = weight
    graph[v][u] = weight

T = set();
X = set();

X.add(0);

while len(X) != vertices:
    crossing = set();
    for x in X:
        for k in range(vertices):
            if k not in X and graph[x][k] != 0:
                crossing.add((x, k))
    edge = sorted(crossing, key=lambda e:graph[e[0]][e[1]])[0];
    T.add(edge)
    X.add(edge[1])

for edge in T:
    print edge