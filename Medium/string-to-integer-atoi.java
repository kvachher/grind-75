class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty()) {
            return 0;
        }
        
        char[] c = s.toCharArray();
        int i = 0;
        boolean neg = false;
        
        if (c[i] == '+' || c[i] == '-') {
            neg = (c[i] == '-');
            i++;
        }
        
        long num = 0;
        while (i < c.length && Character.isDigit(c[i])) {
            num = num * 10 + (c[i] - '0');
            if (!neg && num > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            } else if (neg && -num < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
            i++;
        }
        
        return neg ? (int) -num : (int) num;
    }
}
