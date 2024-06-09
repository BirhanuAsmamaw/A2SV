class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        int target = graph.length - 1;
        Queue<List<Integer>> queue = new LinkedList<>();
        List<Integer> initialPath = new ArrayList<>();
        initialPath.add(0);
        queue.add(initialPath);
        
        while (!queue.isEmpty()) {
            List<Integer> temp = queue.poll();
            if (temp.get(temp.size() - 1) == target) {
                result.add(new ArrayList<>(temp));
            }
            
            for (int neighbor : graph[temp.get(temp.size() - 1)]) {
                List<Integer> newPath = new ArrayList<>(temp);
                newPath.add(neighbor);
                queue.add(newPath);
            }
        }
        
        return result;
    }
}
