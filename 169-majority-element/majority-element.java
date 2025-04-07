class Solution {
    public int majorityElement(int[] nums) {
        int counter;
        for(int j = 0; j<nums.length; j++){
            counter=0;
            for(int i=0; i<nums.length; i++){
                if(nums[i]==nums[j]) counter++;
            } if(counter>nums.length/2) return nums[j];
            j++;}
        return nums[0];
    } 
}