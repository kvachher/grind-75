class LRUCache {
    int capacity;
    List<Integer> q = new ArrayList<>();
    Map<Integer, Integer> map = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            q.remove((Integer) key);
            q.add(key);
            return map.get(key);
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            q.remove((Integer) key);
        } else if (q.size() >= capacity) {
            int oldestKey = q.remove(0);
            map.remove(oldestKey);
        }
        q.add(key);
        map.put(key, value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
