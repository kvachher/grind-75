class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> list = new ArrayList<>();
        if (intervals.length <= 1) {
            return intervals;
        }
        Arrays.sort(intervals, (a, b) -> Double.compare(a[0], b[0]));
        for (int[] curr : intervals) {
            if (list.isEmpty()) {
                list.add(curr);
            }
            int[] prev = list.remove(list.size() - 1);
            if (curr[0] <= prev[1]) {
                int[] pair = new int[2];
                pair[0] = prev[0];
                pair[1] = Math.max(prev[1], curr[1]);
                list.add(pair);
            }
            else {
                list.add(prev);
                list.add(curr);
            }
        }
        int[][] ans = new int[list.size()][2];
        for (int j = 0; j < list.size(); j++) {
            ans[j][0] = list.get(j)[0];
            ans[j][1] = list.get(j)[1];
        }
        return ans;
    }
}
