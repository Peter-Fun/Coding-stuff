class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        output = []
        for i in range(1,len(searchWord)+1):
            given = []
            typed = searchWord[0:i]
            for product in products:
                if product[0:i] == typed:
                    given.append(product[:])
            output.append(given[0:3])
        return output
