lass Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] sch = magazine.toCharArray();
        char[] tch = ransomNote.toCharArray();

        Map<Character, Integer> map = new HashMap<>(); 

        for (int i = 0; i < sch.length; i++) { 
            if (map.containsKey(sch[i])) {
                int occurrences = map.get(sch[i]);
                map.put(sch[i], occurrences + 1);
            }
            else {
                map.put(sch[i], 1);
            } 
        }

        for (int i = 0; i < tch.length; i++) {
            if (map.containsKey(tch[i])) {
                int count = map.get(tch[i]);
                if (count > 1)
                    map.put(tch[i], count  - 1);
                else
                    map.remove(tch[i]);
            }
            else {
                return false;
            }
        }
        return true;
    }
}
