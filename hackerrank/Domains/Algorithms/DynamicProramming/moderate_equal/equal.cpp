#include <bits/stdc++.h>

using namespace std;

int equal(vector <int> arr) {
    // Complete this function
	int nummoves, move5, move2, move1, mnmoves=-1;
	#the '-4' is a bit hacky. passes test 15
	for (int smallest = -4; smallest <= *std::min_element(arr.begin(), arr.end()); smallest++)
	{
		nummoves = 0;
		for(int k : arr)
		{
			if (k!=smallest)
			{
				move5 = (k-smallest)/5;
                move2 = (k-smallest-move5*5)/2;
                move1 = (k-smallest-move5*5-move2*2);
				nummoves += (move5+move2+move1);
				if (mnmoves >= 0)
                    if (nummoves > mnmoves)
                        break;
			}
		}
		if (mnmoves > nummoves || mnmoves < 0)
            mnmoves = nummoves;
	}
	return mnmoves;
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int arr_i = 0; arr_i < n; arr_i++){
           cin >> arr[arr_i];
        }
        int result = equal(arr);
        cout << result << endl;
    }
    return 0;
}
