import java.util.List;

public class Solution {
    
    private int countSetBits(int num) {
        int count = 0;
        while (num > 0) {
            count += num & 1;
            num >>= 1;
        }
        return count;
    }

    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        int totalSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            int countBits = countSetBits(i);
            if (countBits == k) {
                totalSum += nums.get(i);
            }
        }
        return totalSum;
    }
}
