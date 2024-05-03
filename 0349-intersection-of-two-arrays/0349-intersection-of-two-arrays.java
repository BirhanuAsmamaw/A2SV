import java.util.*;

public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> uniqueElements = new HashSet<>();
        for (int num : nums1) {
            for (int num2 : nums2) {
                if (num == num2) {
                    uniqueElements.add(num);
                    break;
                }
            }
        }

        int[] result = new int[uniqueElements.size()];
        int index = 0;
        for (int num : uniqueElements) {
            result[index++] = num;
        }

        return result;
    }
}
