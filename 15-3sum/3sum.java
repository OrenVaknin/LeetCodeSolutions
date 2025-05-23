class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        int sum;
        Arrays.sort(nums);
        int left = 1;
        int right = nums.length-1;
        for(int i=0; i<nums.length-2;i++){
            left = i+1;
            right = nums.length-1;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            while(left<right){
                sum = nums[left]+nums[right]+nums[i];
                if(sum==0){
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while(left <right && nums[left] == nums[left - 1]) left++;
                    while(left <right && nums[right] == nums[right + 1]) right--;
                    }
                else if(sum<0) left++;
                else if(sum>0) right--;
            }
        } return ans;
    }
}
