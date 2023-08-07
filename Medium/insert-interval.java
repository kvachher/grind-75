class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> list = new LinkedList<>();
        int i = 0, n = intervals.length;
        while (i < n && intervals[i][1] < newInterval[0]) {
            list.add(intervals[i]);
            i++;
        }
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        list.add(newInterval);
        while (i < n) {
            list.add(intervals[i]);
            i++;
        }
        int[][] toReturn = new int[list.size()][2];
        for (int j = 0; j < list.size(); j++) {
            toReturn[j][0] = list.get(j)[0];
            toReturn[j][1] = list.get(j)[1];
        }
        return toReturn;
    }
}
