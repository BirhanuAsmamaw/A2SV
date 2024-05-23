import java.util.HashMap;

public class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> dictionary = new HashMap<>();
        
        // Count the frequency of each character
        for (char c : s.toCharArray()) {
            dictionary.put(c, dictionary.getOrDefault(c, 0) + 1);
        }
        
        // Find the first unique character
        for (int i = 0; i < s.length(); i++) {
            if (dictionary.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
