class MyQueue {

    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> s2 = new Stack<>();

    public MyQueue() {
    }
    
    public void push(int x) {
        s1.push(x);
    }
    
    public int pop() {
        while (!s1.empty()) {
            s2.push(s1.pop());
        }
        int toReturn = s2.pop();
        while (!s2.empty()) {
            s1.push(s2.pop());
        }
        return toReturn;
    }
    
    public int peek() {
        while (!s1.empty()) {
            s2.push(s1.pop());
        }
        int toReturn = s2.peek();
        while (!s2.empty()) {
            s1.push(s2.pop());
        }
        return toReturn;
    }
    
    public boolean empty() {
        return s1.isEmpty();
    }
}

class Node {
    int val;
    Node next;
    public Node() {}
}
