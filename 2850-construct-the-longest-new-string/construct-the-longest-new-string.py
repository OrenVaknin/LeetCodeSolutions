class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        ans=0
        if z<x and z<y:
            x-=z
            y-=z
            ans+=z*4
        if z>y and z>x:
            ans+=2*(z-max(x,y))
            z=max(x,y)
        if x>0 and y>0 and z>0:
            tmp= (min(x,y,z))
            ans+=6*tmp
            x-=tmp
            y-=tmp
            z-=tmp
        if (x==0 and y!=0 and z!=0) or (x!=0 and y==0 and z!=0):
            ans+=2*(1+z)
        if(x!=0 and y!=0 and z==0):
            tmp=min(x,y)
            ans+=4*tmp
            x-=tmp
            y-=tmp
        if (x!=0 and y==0 and z==0) or (x==0 and y!=0 and z==0):
            ans+=2
        return ans