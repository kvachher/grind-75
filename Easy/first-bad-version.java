/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return firstBadVersion(1, n); 
    }
    public int firstBadVersion(int start, int end) {
        if (start == end) {
            return start;
        }
        int middle = start + (end - start) / 2;
        if (isBadVersion(middle) && !isBadVersion(middle + 1)) {
            return middle;
        } else if (isBadVersion(middle)) {
            return firstBadVersion(start, middle);
        } else {
            return firstBadVersion(middle + 1, end); 
        }
    }
}
