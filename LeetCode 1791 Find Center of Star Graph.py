class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        thing = {}
        for e in edges:
            try:
                print(thing[e[0]])
            except:
                try:
                    print(thing[e[1]])
                except:
                    thing[e[0]] = e[1]
                    thing[e[1]] = e[0]
                else:
                    return e[1]
            else:
                return e[0]
