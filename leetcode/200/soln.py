class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        from collections import deque

        # copying this from floodfill
        def get_neighbors(node, image):
            num_rows = len(image)
            num_cols = len(image[0])
            neighbors = []
            assert image[node[0]][node[1]] == "1"
            if node[0] > 0 and image[node[0]][node[1]] == image[node[0]-1][node[1]]:
                neighbors += [(node[0]-1, node[1])]
            if node[0] < num_rows-1 and image[node[0]][node[1]] == image[node[0]+1][node[1]]:
                neighbors += [(node[0]+1, node[1])]
            if node[1] > 0 and image[node[0]][node[1]] == image[node[0]][node[1]-1]:
                neighbors += [(node[0], node[1]-1)]
            if node[1] < num_cols-1 and image[node[0]][node[1]] == image[node[0]][node[1]+1]:
                neighbors += [(node[0], node[1]+1)]
            return neighbors
                    

        def count_number_of_islands(grid: List[List[int]]) -> int:
            q = deque([])
            visited = set([])

            island_id = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if (r,c) not in visited and grid[r][c] == "1":
                        q.appendleft((r,c))
                        visited.add((r,c))

                        while(len(q) > 0):
                            curr_node = q.pop()
                            neighbors = get_neighbors(curr_node, grid)
                            for neighbor in neighbors:
                                if neighbor not in visited:
                                    q.appendleft(neighbor)
                                    visited.add(neighbor)
                        island_id+=1
            return island_id
        return count_number_of_islands(grid)
        
