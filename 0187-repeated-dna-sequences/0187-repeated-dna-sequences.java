import java.util.*;

public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> L1 = new HashSet<>();
        Set<String> L2 = new HashSet<>();
        int l = s.length();
        if (l <= 10)
            return new ArrayList<>(L1);
        for (int i = 0; i <= l - 10; i++) {
            String stri = s.substring(i, i + 10);
            if (L1.contains(stri) && !L2.contains(stri)) {
                L2.add(stri);
            } else if (!L1.contains(stri)) {
                L1.add(stri);
            }
        }
        
        return new ArrayList<>(L2);
    }
}
