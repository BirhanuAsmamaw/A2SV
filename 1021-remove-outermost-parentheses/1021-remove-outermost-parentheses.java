class Solution {
    public String removeOuterParentheses(String s) {
        if (s == null || s.length() <= 2) {
            return "";
        }
        
        StringBuilder result = new StringBuilder();
        int count = 1;
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                count++;
                if (count >= 2) {
                    result.append(s.charAt(i));
                }
            } else {
                count--;
                if (count >= 1) {  
                    result.append(s.charAt(i));
                }
            }
        }
        
        return result.toString();
    }
}