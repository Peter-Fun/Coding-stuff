class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        
        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX>rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
        for i in range(len(s1)):
            union(s1[i],s2[i])
        res = []
        for c in baseStr:
            res.append(find(c))
            
        return ''.join(res)
