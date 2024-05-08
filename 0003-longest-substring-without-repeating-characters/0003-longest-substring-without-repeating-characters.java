import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> mySet = new HashSet<>();
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            while (mySet.contains(s.charAt(right))) {
                mySet.remove(s.charAt(left));
                left++;
            }
            mySet.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
