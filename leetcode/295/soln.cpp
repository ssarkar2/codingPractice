class MedianFinder {
public:
    MedianFinder() {
        track_smallest.reserve(50000);
        track_largest.reserve(50000);
    }

    void print() {
        cout<<"------------\n";
        for(auto &i : track_largest) {
            cout << i << " ";
        }
        cout << " --- ";
        for(auto &i : track_smallest) {
            cout << -i << " ";
        }
        cout<<"===========\n";
    }

    void balance() {
        int smallest_tracker_size = track_smallest.size();
        int largest_tracker_size = track_largest.size();
        if (abs(smallest_tracker_size - largest_tracker_size) <= 1)
            return;
        auto& from = smallest_tracker_size > largest_tracker_size ? track_smallest : track_largest;
        auto& to = smallest_tracker_size > largest_tracker_size ? track_largest : track_smallest;
        std::pop_heap(from.begin(), from.end());
        int x = from.back();
        from.pop_back();
        to.push_back(-x);
        push_heap(to.begin(), to.end());
    }
    
    // maintain invarian, that | size1-size2 | <= 0
    void addNum(int num) {
        if (!added_first) {
            added_first = true;
            track_largest[0] = (num);
        } else {
            // track_largest will never be 0, ist insert goes in there
            //assert (track_largest.size() >= 0);
            if (num <= track_largest[0]) {
                track_largest.push_back(num);
                push_heap(track_largest.begin(), track_largest.end());
                //cout << "insert track_largest" << num << "\n";
            } else {
                track_smallest.push_back(-num);
                push_heap(track_smallest.begin(), track_smallest.end());
                //cout << "insert track_smallest" << num << "\n";
            }
        }
        /*
        cout << "sizes before balance:" << track_smallest.size() << " " << track_largest.size() << "\n";
        print();
        balance();
        print();
        cout << "sizes after balance:" << track_smallest.size() << " " << track_largest.size() << "\n";
        */
        balance();
        
    }
    
    double findMedian() {
        int smallest_tracker_size = track_smallest.size();
        int largest_tracker_size = track_largest.size();
        if (smallest_tracker_size == largest_tracker_size) {
            //cout << "even size" << track_largest[0] << " " << track_smallest[0] << "\n";
            return (track_largest[0] - track_smallest[0]) / 2.0;
        } else {
            //cout << "odd size\n";
            return largest_tracker_size > smallest_tracker_size ? track_largest[0] : -track_smallest[0];
        }
    }

    vector<int> track_smallest; // 2nd half. needs "-"
    vector<int> track_largest{1}; // 1st half. default. // to make address sanitizer happy, allocating 1
    bool added_first{false};
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
