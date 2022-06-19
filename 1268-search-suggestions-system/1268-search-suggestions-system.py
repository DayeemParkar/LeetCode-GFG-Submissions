class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        productDict=defaultdict(list)
        for product in products:  
            for i in range(len(product)+1):
                productDict[product[:i]].append(product)
        crntstr=''
        output=[]
        for char in searchWord:
            crntstr+=char
            output.append(productDict[crntstr][:3])
        return output