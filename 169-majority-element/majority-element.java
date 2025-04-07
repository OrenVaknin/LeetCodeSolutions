class Solution {
    public int majorityElement(int[] nums) {
        int unq=nums[0];
        int cntr=0;
        for(int num: nums){
            if(cntr == 0)
                unq=num;
            cntr+=(num == unq)? 1:-1;
        } 
        return unq;
    } 
}