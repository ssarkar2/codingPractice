#include<iostream>
#include <future>
#include <functional>
#include <string>
#include <chrono>
#include <random>


class Node {
    public:
    Node(const std::string& name, bool async) : m_name{name}, m_async{async} {}
    virtual ~Node() {}
    virtual int compute() = 0;
    protected:
    const bool m_async=false;
    const std::string m_name;
    //std::mt19937_64 m_eng{std::random_device{}()};
};


class Add : public Node {
    public:
    Add(const std::string& name, Node* x, Node* y, bool async=true): Node(name, async), lhs{x}, rhs{y} {}

    int compute() {
        // We dont need to do this if its done once, maybe an optional to hold result oonce computed?
        std::cout<<this->m_name<<"\n";
        //std::uniform_int_distribution<> dist{10, 100};
        if (m_res) {
            return *m_res;
        } else {
            /*
            if present in result optional take it and go
            else, try acquiring a unique lock (as you intend to update result)
                you might be the first or there might be someone ahead of you
                if you are the first, go thru and update result
                else: once u acq the lock reattempt to read the optional, result should be there, take it and go
            */
            std::scoped_lock<std::mutex> sl{m_mtx};

            if (m_res) {
                return *m_res;
            }

            if (m_async){
                // ideally pull from a thread pool, else too many threads will be spun up
                std::future<int> lhs_result = std::async(std::launch::async, &Node::compute, lhs);
                std::future<int> rhs_result = std::async(std::launch::async, &Node::compute, rhs);
                //std::this_thread::sleep_for(std::chrono::milliseconds{dist(this->m_eng)});
                m_res = lhs_result.get() + rhs_result.get();
            } else {
                m_res = lhs->compute() + rhs->compute();
            }
            return *m_res;
        }
    }

    private:
    Node* lhs=nullptr;
    Node* rhs=nullptr;
    std::mutex m_mtx;
    std::optional<int> m_res;
};

class Const : public Node {
    public:
    Const(const std::string& name, int val): Node(name, false), m_val{val} {}

    int compute() {
        std::cout<<this->m_name<<"\n";
        //std::uniform_int_distribution<> dist{10, 100};
        //std::this_thread::sleep_for(std::chrono::milliseconds{dist(this->m_eng)});
        return m_val;}
    private:
    int m_val;
};

int main() {
    Const c0{"c0", 5};
    Const c1{"c1", 2};
    Add a0{"a0", &c0, &c1};
    Const c2{"c2", 3};
    Const c3{"c3", 6};
    Add a1{"a1", &c2, &a0};
    Add a2{"a2", &c3, &a0};
    Add a3{"a3", &a1, &a2};
    std::cout << "Res:: " << a3.compute() << "\n";
}