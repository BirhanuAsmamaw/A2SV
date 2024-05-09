import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i <= rowIndex; i++) {
            List<Integer> ladder = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    ladder.add(1);
                } else {
                    ladder.add(res.get(j - 1) + res.get(j));
                }
            }
            res = ladder;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int rowIndex = 3; // Example rowIndex
        List<Integer> result = solution.getRow(rowIndex);
        System.out.println(result);
    }
}
