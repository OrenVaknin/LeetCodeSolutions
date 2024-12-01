import java.util.*;
class Solution {
    public int romanToInt(String s) {
        char[] arr = s.toCharArray();
        int sum =0;
        Map<Character, Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M', 1000);
        if (arr.length == 1)
            return map.get(arr[0]);
        for (int i = 0; i<arr.length-1; i++){
            if(map.get(arr[i])>=map.get(arr[i+1]))
                sum= sum + map.get(arr[i]);
            else{
                sum= sum - map.get(arr[i]);
            } 
        }
        return (sum+ map.get(arr[arr.length-1]));
    }
}