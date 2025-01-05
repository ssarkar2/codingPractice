class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        from collections import deque

        def get_neighbors(node, image):
            num_rows = len(image)
            num_cols = len(image[0])
            neighbors = []
            if node[0] > 0 and image[node[0]][node[1]] == image[node[0]-1][node[1]]:
                neighbors += [(node[0]-1, node[1])]
            if node[0] < num_rows-1 and image[node[0]][node[1]] == image[node[0]+1][node[1]]:
                neighbors += [(node[0]+1, node[1])]
            if node[1] > 0 and image[node[0]][node[1]] == image[node[0]][node[1]-1]:
                neighbors += [(node[0], node[1]-1)]
            if node[1] < num_cols-1 and image[node[0]][node[1]] == image[node[0]][node[1]+1]:
                neighbors += [(node[0], node[1]+1)]
            return neighbors
                    

        def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
            q = deque([(r,c)])
            visited = set([(r,c)])
            
            while(len(q) > 0):
                curr_node = q.pop()
                
                neighbors = get_neighbors(curr_node, image)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        q.appendleft(neighbor)
                        visited.add(neighbor)
                image[curr_node[0]][curr_node[1]] = replacement
            return image
        return flood_fill(sr, sc, color, image)
