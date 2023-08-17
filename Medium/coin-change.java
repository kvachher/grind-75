class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] arr = new int[amount + 1];
        int shortestPath = amount + 1;
        arr[0] = 0;

        if (amount == 0)
            return 0;
        
        for (int i = 1; i <= amount; i++) {
            arr[i] = amount + 1;
            for (int c : coins) {
                if (i >= c) {
                    arr[i] = Math.min(arr[i], arr[i - c] + 1);
                }
            }
        }

        for (int c : coins) {
            int lastPath = amount - c;
            int path = 0;
            if (lastPath >= 0) {
                path = arr[lastPath] + 1;
                shortestPath = Math.min(shortestPath, path);
            }
        }
        
        return shortestPath > amount ? -1 : shortestPath;
    }
}

