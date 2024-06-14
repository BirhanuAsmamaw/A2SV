class Solution {
    public String largestNumber(int[] nums) {
        
        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }
        
        Arrays.sort(strNums, new Comparator<String>() {
            public int compare(String a, String b) {
                String ab = a + b;
                String ba = b + a;
                return ba.compareTo(ab); // Reverse order
            }
        });
        
        if (strNums[0].equals("0")) {
            return "0";
        }
        
        StringBuilder result = new StringBuilder();
        for (String str : strNums) {
            result.append(str);
        }
        return result.toString();
    }
}
