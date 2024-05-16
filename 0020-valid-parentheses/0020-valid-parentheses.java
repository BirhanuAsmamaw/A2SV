import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> checkClosing = new HashMap<>();
        checkClosing.put(')', '(');
        checkClosing.put(']', '[');
        checkClosing.put('}', '{');
        
        for (char i : s.toCharArray()) {
            if (checkClosing.containsKey(i)) {
                if (!stack.isEmpty() && stack.peek() == checkClosing.get(i)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(i);
            }
        }
        
        return stack.isEmpty();
    }
}
