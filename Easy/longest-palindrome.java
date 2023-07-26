class Solution {
    public int longestPalindrome(String s) {
        int numOdd = 0; 
        char[] arr = s.toCharArray();
        HashMap<Character, Integer> map = new HashMap<>(); 

        for (int i = 0; i < arr.length; i++) {
            if (map.containsKey(arr[i])) {
                int occ = map.get(arr[i]);
                map.put(arr[i], occ + 1);
            }
            else
                map.put(arr[i], 1);
            if (map.get(arr[i]) % 2 == 1)
                numOdd++;
            else
                numOdd--;
        }
        if (numOdd > 1)
            return s.length() - numOdd + 1;
        return s.length(); 
    }
}
