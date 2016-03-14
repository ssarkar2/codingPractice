#https://www.hackerrank.com/challenges/the-quickest-way-up
#https://github.com/yahavb/MultiLayerApp/blob/master/shortest_path.py

import sys
import heapq

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)  #uncomment this line to make the edge 2 ways

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start, target):
    #print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                #print 'updated : current = %s next = %s new_dist = %s' \
                #        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                pass
                #print 'not updated : current = %s next = %s new_dist = %s' \
                 #       %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return -1

def f(input):
    g = Graph()
    for i in range(1,101):
        g.add_vertex(str(i))

    ladderstart = [i[0] for i in input[0]]; ladderend = [i[1] for i in input[0]]
    snakestart = [i[0] for i in input[1]]; snakeend = [i[1] for i in input[1]]

    for i in range(1,101):
        for j in range(1,7):
            if i+j <= 100:
                t = find_element_in_list(i+j, ladderstart)
                if t >= 0:
                    g.add_edge(str(i), str(ladderend[t]), 1) #ladder moves
                else:
                    t = find_element_in_list(i+j, snakestart)
                    if t >= 0:
                        g.add_edge(str(i), str(snakeend[t]), 1) #snake moves
                    else:
                        g.add_edge(str(i), str(i+j), 1) #simple dice moves

##    for i in input[0]: #ladders
##        g.add_edge(str(i[0]), str(i[1]), 0, 'l')
##
##    for i in input[1]: #snakes
##        g.add_edge(str(i[0]), str(i[1]), 0, 's')


    dijkstra(g, g.get_vertex('1'), g.get_vertex('100'))
    target = g.get_vertex('100')
    path = [target.get_id()]
    shortest(target, path)
    #print path[::-1]
    #print len(path[::-1])
    #print path[::-1]
    pl = len(path)
    print [-1,pl-1][pl>1] #because if no path exists, print -1


#in = []#[[(32,62),(42,68),(12,98)],[(95,13),(97,25),(93,37),(79,27),(75,19),(49,47),(67,17)]]
#formGraph(in, 6)

#input = [[(32,62),(42,68),(12,98)],[(95,13),(97,25),(93,37),(79,27),(75,19),(49,47),(67,17)]]

testcases = int(raw_input())
for i in range(testcases):
    numladder = int(raw_input())
    ladder = []
    for j in range(numladder):
        ladder.append([int(i) for i in raw_input().split()])
    numsnake = int(raw_input())
    snake = []
    for j in range(numsnake):
        snake.append([int(i) for i in raw_input().split()])
    input = [ladder, snake]
    f(input)

