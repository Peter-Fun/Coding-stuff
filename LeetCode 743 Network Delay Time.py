class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)] # initializing minheap with given source node 
        visited = set()   # initializing a set to keep track of visited node
        time = 0          # initial time delay 
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time,w1)
            
            for n2,w2 in edges[n1]: # applying bfs on all the neighbour node
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1+w2,n2)) # if the neighbour not visited yet then
                                                       # pushing it to heap and all along path value
            
        return time if len(visited) == n else -1
