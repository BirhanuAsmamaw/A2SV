import java.util.*;
public class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        List<Integer> resultList = new ArrayList<>();
        for (int i : nums1) {
            int count = 0;
            for (int j : nums2) {
                if (i == j) {
                    for (int k = indexOf(nums2, j) + 1; k < nums2.length; k++) {
                        if (nums2[k] > j) {
                            count++;
                            resultList.add(nums2[k]);
                            break;
                        }
                    }
                    if (count == 0) {
                        resultList.add(-1);
                    }
                }
            }
        }
        // Convert List<Integer> to int[]
        int[] result = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            result[i] = resultList.get(i);
        }
        return result;
    }
    // Custom implementation of indexOf for arrays
    public static int indexOf(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }
}
