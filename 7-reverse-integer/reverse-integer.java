class Solution {
    public int reverse(int x) {
        boolean negative = false;
        if (x<0){
            negative = true;
            x=x*-1;
        }
        long num=0;
        //if(Math.log(x)/Math.log(2)>=32)
         //   return 0;
        while (x>0){
            num=x%10+num*10;
            x=x/10;
        }
        if (num>Integer.MAX_VALUE)
            return 0;
        if (negative)
            num=num*-1;
        return (int) num;
    }
}