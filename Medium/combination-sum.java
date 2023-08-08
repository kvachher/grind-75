class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        dfs(0, candidates, target, new ArrayList<>(), list);
        return list;
    }
    public void dfs(int i, int [] c, int target, List<Integer> comb, List<List<Integer>> list) {
        if (target == 0) {
            list.add(new ArrayList<>(comb));
            return;
        }
        for (int j = i; j < c.length; j++) {
            if (c[j] > target)
                continue;
            comb.add(c[j]);
            dfs(j, c, target - c[j], comb, list);
            comb.remove(comb.size() - 1);
        }
    }
}
