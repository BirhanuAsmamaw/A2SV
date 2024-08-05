import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        Set<List<Integer>> set = new HashSet<>();
        while (set.size() != factorial(nums.length)) {
            shuffleArray(nums);
            List<Integer> permutation = new ArrayList<>();
            for (int num : nums) {
                permutation.add(num);
            }
            set.add(permutation);
        }
        return new ArrayList<>(set);
    }
    
    private int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    private void shuffleArray(int[] array) {
        Random rnd = new Random();
        for (int i = array.length - 1; i > 0; i--) {
            int index = rnd.nextInt(i + 1);
            int temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }
}
