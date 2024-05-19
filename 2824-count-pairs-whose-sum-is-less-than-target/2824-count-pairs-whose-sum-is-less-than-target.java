import java.util.List;

public class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int n = nums.size();
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {  // Start j from i + 1 to ensure i < j
                if (nums.get(i) + nums.get(j) < target) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}
