class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backTracking(1, n, k, new ArrayList<>(), result);
        return result;
    }

    private void backTracking(int start, int n, int k, List<Integer> combination, List<List<Integer>> result) {
        if (combination.size() == k) {
            result.add(new ArrayList<>(combination));
            return;
        }
        for (int i = start; i <= n; i++) {
            combination.add(i);
            backTracking(i + 1, n, k, combination, result);
            combination.remove(combination.size() - 1);
        }
    }
}
