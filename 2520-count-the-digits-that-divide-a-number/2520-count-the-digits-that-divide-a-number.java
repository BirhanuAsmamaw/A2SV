public class Solution {
    public int countDigits(int num) {
        String stri = Integer.toString(num);
        int result = 0;
        for (char single : stri.toCharArray()) {
            if (num % Character.getNumericValue(single) == 0) {
                result += 1;
            }  
        }
        return result;
        
    }
}
