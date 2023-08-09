class Solution {
    public int lengthOfLongestSubstring(String s) {
        char [] c = s.toCharArray();
        if (c.length == 0) {
            return 0;
        }
        int longestLength = 1;
        for (int i = 0; i < c.length; i++) {
            HashSet<Character> set = new HashSet<>();
            int j = i;
            int length = 0;
            while (j < c.length && !set.contains(c[j])) {
                set.add(c[j]);
                length++;
                j++;
            }
            longestLength = Math.max(length, longestLength);
        }
        return longestLength; 
    }
}
