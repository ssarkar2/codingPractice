class MyCircularDeque {
public:
    MyCircularDeque(int k) : m_container(k), m_capacity{k} {
        
    }

    int rear_write_idx() {
        return (m_front + m_size) % m_capacity;
    }

    int rear_read_idx() {
        return (m_front + m_size - 1) % m_capacity;
    }
    
    bool insertFront(int value) {
        if (isFull())
            return false;
        m_front--;
        if (m_front < 0)
            m_front = m_capacity-1;
        m_container[m_front] = value;
        m_size++;
        return true;
        
    }
    
    bool insertLast(int value) {
        if (isFull())
            return false;
        m_container[rear_write_idx()] = value;
        m_size++;
        return true;
    }
    
    bool deleteFront() {
        if (isEmpty())
            return false;
        m_front++;
        m_front = m_front % m_capacity;
        m_size--;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty())
            return false;
        m_size--;
        return true;
    }
    
    int getFront() {
        if (isEmpty())
            return -1;
        return m_container[m_front];
    }
    
    int getRear() {
        if (isEmpty())
            return -1;
        return m_container[rear_read_idx()];
    }
    
    bool isEmpty() {
        return m_size==0;
    }
    
    bool isFull() {
        return m_size==m_capacity;
    }

    private:
    vector<int> m_container;
    int m_front = 0; // read ptr for front
    int m_size = 0;
    int m_capacity;
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
