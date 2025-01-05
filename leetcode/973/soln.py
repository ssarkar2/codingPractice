class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        from heapq import heappop, heappush


        # could have just sorted as well
        def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
            distsq = {(x,y):x*x+y*y for x, y in points}
            heap = []
            
            for x, y in points:
                heappush(heap, (x ** 2 + y ** 2, (x,y)))

            result = []
            for i in range(k):
                _, pt = heappop(heap)
                result += [pt]
            return result
        return k_closest_points(points, k)
