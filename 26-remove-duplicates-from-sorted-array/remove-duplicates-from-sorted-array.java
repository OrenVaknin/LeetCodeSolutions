class Solution {
    public int removeDuplicates(int[] nums) {
                if(nums.length==1){
            return 1;
        }
        int k = 1;
        for (int a = 1; a<nums.length;a++){
            if (nums[a]!= nums[a-1]){
                nums[k] = nums[a];
                k++;
            }
        }
        return k;
    }
}
