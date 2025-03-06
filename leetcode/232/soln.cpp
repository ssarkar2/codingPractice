class MyQueue {
public:
    MyQueue() {}
    
    void push(int x) {
        exchange(exit, entry);
        entry.push(x);
    }
    
    int pop() {
        exchange(entry, exit);
        auto top = exit.top();
        exit.pop();
        return top;
    }
    
    int peek() {
        exchange(entry, exit);
        return exit.top();
    }
    
    bool empty() {
        return entry.size() == 0 && exit.size() == 0;
        
    }
private:

    void exchange(stack<int>& from, stack<int>& to) {
        while(from.size() > 0) {
            auto top = from.top();
            from.pop();
            to.push(top);
        }
    }

    stack<int> entry;
    stack<int> exit;

};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
