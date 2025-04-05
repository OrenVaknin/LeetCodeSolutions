class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=0;
        int j=0;
        int[] uni = new int[n+m];
        for (int c=0; c<n+m;c++){
            if(j<n&&i<m){
                if (nums1[i]<nums2[j]){
                    uni[c] = nums1[i];
                    i++;
                } else{
                    uni[c]=nums2[j];
                    j++;
                }
            }
            else if(i>=m){
                uni[c]=nums2[j];
                j++; 
            } else{
                uni[c]=nums1[i];
                i++;
            }
        } 
        for(int c=0;c<n+m;c++){
            nums1[c]=uni[c];
        }
        return;
    }
 }