# Python Program to count
# cycles of length n
# in a given graph.


class GraphCycles:

    def __init__(self, vertices, graph):
        self.V = vertices  # No. of vertices
        self.graph = graph

    def DFS(self, marked, n, vert, start, count):

        # mark the vertex vert as visited
        marked[vert] = True

        # if the path of length (n-1) is found
        if n == 0:
            # mark vert as un-visited to make
            # it usable again.
            marked[vert] = False

            # Check if vertex vert can end with
            # vertex start
            if self.graph[vert][start] == 1:
                count = count + 1
                return count
            else:
                return count

        # For searching every possible path of
        # length (n-1)
        for i in range(self.V):
            if marked[i] is False and self.graph[vert][i] == 1:

                # DFS for searching path by decreasing
                # length by 1
                count = self.DFS(marked, n-1, i, start, count)

        # marking vert as unvisited to make it
        # usable again.
        marked[vert] = False
        return count

    # Counts cycles of length
    # N in an undirected
    # and connected graph.
    def count_cycles(self, n):

        # all vertex are marked un-visited initially.
        marked = [False] * self.V

        # Searching for cycle by using v-n+1 vertices
        count = 0
        for i in range(self.V-(n-1)):
            count = self.DFS(marked, n-1, i, i, count)

            # ith vertex is marked as visited and
            # will not be visited again.
            marked[i] = True

        return int(count/2)
