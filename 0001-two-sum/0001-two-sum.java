import java.util.*;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int another = target - nums[i];
            if (numMap.containsKey(another)) {
                return new int[] {numMap.get(another), i};
            }
            numMap.put(nums[i], i);
        } 
        return new int[0];
    }
    
}
