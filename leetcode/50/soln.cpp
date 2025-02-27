class Solution {
public:

    vector<int> binrep(long int n) {
        vector<int> res;
        while(true) {
            res.push_back(n%2);
            n /= 2;
            if (n==0)
               break;
        }
        return res;
    }

    double myPow(double x, int n_) {
        bool negexp = n_ < 0;
        if (x==1.0)
            return x;
        long int n;
        if (negexp) // static_cast here because one of the test cases had -int_max, which wouldnt support "-n" operation
            n = -static_cast<long int>(n_);
        else
            n = n_;
        //std::cout << "n is: " << n << "\n";
        auto binrep_n = binrep(n);
        vector<double> powers(binrep_n.size());
        // powers[i] = x^(2^i)
        for (int i = 0; i < binrep_n.size(); i++) {
            if (i==0)
                powers[i] = x;
            else {
                powers[i] = powers[i-1] * powers[i-1];
            }
        }
        double val = 1.0;
        for (int i = 0; i < binrep_n.size(); i++) {
            //cout << powers[i] << " " << binrep_n[i] << "\n";
            if (binrep_n[i] == 1)
                val *= (powers[i]);
        }
        return (negexp ? (1.0/val) : val);

    }
};
