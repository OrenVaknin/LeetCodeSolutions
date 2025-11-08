class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prods=[]
        product=1
        isZero=False
        isAllZero=0
        for j in nums:
            if j!=0:
                product=product*j
            else:
                 isZero=True
                 isAllZero=isAllZero+1
        for i in nums:
            if isAllZero>1:
                prods.append(0)
            else:
                if i!=0:
                    if isZero: 
                            prods.append(0)
                    else:
                        product=product/i
                        prods.append(int(product))
                        product=product*i
                else:
                    prods.append(int(product))

        return prods
