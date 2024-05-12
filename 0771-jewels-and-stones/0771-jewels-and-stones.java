public class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int totJewel = 0;
        
        for (char stone : stones.toCharArray()) {
            if (jewels.contains(String.valueOf(stone))) {
                totJewel++;
            }
        }
        
        return totJewel;
    }
}