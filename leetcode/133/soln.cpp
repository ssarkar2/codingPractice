/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/



class Solution {
public:
    Node* cloneGraph(Node* node) {
        //unordered_map<int, Node*> created_nodes;

        /*
        perform traversal on the orig graph, (BFS or DFS)
        processing current node:
        create its neighbors (if not already created). created_new set is used.
        So its job is to make sure all the outgoing edges of this node are created
        */
        if (node == nullptr)
            return node;

        stack<Node*> stk_old;
        stk_old.push(node);
        
        set<int> visited_old;
        unordered_map<int, Node*> created_new; 
        while(stk_old.size()>0) {
            auto curr_node_old = stk_old.top();
            stk_old.pop();
            //cout << "PROCESSING------" << curr_node_old->val << "\n";

            auto curr_node_new = create_or_get(curr_node_old, created_new);

            if (visited_old.find(curr_node_old->val) == visited_old.end()) {
                for (auto n : curr_node_old->neighbors) {
                        auto neighbor_node_new = create_or_get(n, created_new);
                        curr_node_new->neighbors.push_back(neighbor_node_new);
                    if (visited_old.find(n->val) == visited_old.end()) {
                        stk_old.push(n);
                    }
                }
            }
            //cout << "inserting to visited " << curr_node_old->val << "\n";
            visited_old.insert(curr_node_old->val); // assert curr_node_old not in visited_old
        }
        // assert (visited_old.size() == created_new.size());
        return create_or_get(node, created_new);
    }

    Node* create_and_copyval(Node* n) {
        return (new Node(n->val));
    }

    Node* create_or_get(Node* n, unordered_map<int, Node*>& created_new) {
        auto itr = created_new.find(n->val);
        Node* new_node;
        if (itr == created_new.end()) {
            new_node = create_and_copyval(n);
            created_new.insert({n->val, new_node});
        } else {
            new_node = itr->second;
        }
        return new_node;
    }
};
