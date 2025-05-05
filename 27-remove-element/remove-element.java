class Solution {
    public int removeElement(int[] nums, int val) {
        int vals = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=val){
                nums[vals]=nums[i];
                vals++;
            }
        }
    return vals;
    }
}