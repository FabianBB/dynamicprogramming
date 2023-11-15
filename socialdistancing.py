from collections import deque
import time
import networkx as nx
import sys


class Graph:

    def __init__(self):
        self.V = 0
        self.adj_list = {}  # adjacency list
        self.shortest_paths = {}  # shortest paths

    def read_input(self, filename):
        with open("testcases/" + filename, "r") as f:
            # read first line into ints
            self.V, E, T, D = map(int, f.readline().split())
            # zero based indexing so -1 (unlike networkx)
            sa, ta, sb, tb = [int(x) - 1 for x in f.readline().split()]

            # init adj list
            self.adj_list = {i: [] for i in range(self.V)}

            # read edges
            for line in f:
                # zero based indexing again :)
                u, v = [int(x) - 1 for x in line.split()]
                # bidirectional
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)

        # init shortest paths
        self.shortest_paths = dict(nx.all_pairs_shortest_path_length(nx.Graph(self.adj_list)))
        # return everything
        return T, D, sa, ta, sb, tb


    def distance(self, va, vb):
        return self.shortest_paths[va][vb]

    # Function to reconstruct the paths from a predecessor map given the start and end states
    def reconstruct_paths(self, pred, start_state, end_state):
        path_a, path_b = [], []  # init paths
        current_state = end_state  # essentially backtracking from end state

        # follow predecessor map
        while current_state != start_state:
            path_a.insert(0, current_state[0])
            path_b.insert(0, current_state[1])
            current_state = pred[current_state]

        # start state missing so add it
        path_a.insert(0, start_state[0])
        path_b.insert(0, start_state[1])

        return path_a, path_b

    # Function to find paths for two individuals that are at least D units apart at all times
    # Function to find paths for two individuals that are at least D units apart at all times and do not exceed path length T
    def socially_distant_paths(self, sa, ta, sb, tb, D, T):
        queue = deque([((sa, sb), 0)])  # Initialize queue with start positions and path length 0
        visited = {(sa, sb): True}  # Mark start positions as visited
        pred = {}  # Predecessor map for path reconstruction

        while queue:
            (pa, pb), length = queue.popleft()  # Get current positions and path length

            if pa == ta and pb == tb:  # Check if end state is reached
                return self.reconstruct_paths(pred, (sa, sb), (ta, tb)), True

            if length < T:  # ensure shorter than T
                # check all neighbour pairs
                for neighbor_a in self.adj_list[pa]:
                    for neighbor_b in self.adj_list[pb]:
                        # ensure more than D apart
                        if self.distance(neighbor_a, neighbor_b) > D:
                            new_state = (neighbor_a, neighbor_b)
                            if new_state not in visited:  # unvisited
                                queue.append((new_state, length + 1))  # Increment path length
                                visited[new_state] = True  #
                                pred[new_state] = (pa, pb)  # add to predecessor map

        return ([], []), False  # Return empty and False if no solution is found


def main():
    g = Graph()  # Create a new Graph object
    # get command line argument or input
    filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter filename: ")
    T, D, sa, ta, sb, tb = g.read_input(filename)

    start_time = time.time()

    (path_a, path_b), success = g.socially_distant_paths(sa, ta, sb, tb, D, T)

    duration = time.time() - start_time

    # print paths nad lengths if sol found
    # check if length of path is less than T as per instructions
    if success:
        print(len(path_a) - 1)  # Length of path a
        print(' '.join(str(v + 1) for v in path_a))  # a
        print(' '.join(str(v + 1) for v in path_b))  # b
    else:
        # if no solution print T+1 as per instructions
        print(T + 1)

    # tiem taken
    print("Time taken: {:.2f}ms".format(duration * 1000))
    # I think time complexity for this might be O(T*V^3) but idk


if __name__ == "__main__":
    main()




# calc shortest path distance between 2 nodes
# obsolete code, used networkx instead
# could just call this in a for loop and create the shortest paths dict that way, but netowrkx is more optimized
# since it only gets created once anyways, it doesnt affect runtime that much.
def dist(self, va, vb):
    # obvious base case
    if va == vb:
        return 0

    # init BFS queueue
    queue = deque([va])
    visited = [False] * self.V
    visited[va] = True
    distance = [0] * self.V  # init distance array

    # BFS
    while queue:
        current = queue.popleft()
        for neighbor in self.adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                if neighbor == vb:
                    return distance[neighbor]  # return distance if target found
                queue.append(neighbor)
    return -1  # no path
