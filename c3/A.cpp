#include <bits/stdc++.h>
#include <string>
using namespace std;

int main()
{
    int n;
    string name;
    cin >> n;
    vector<string> vn(n);
    for (int i = 0;i < n; i++) {
        cin >> name;
        if (name in vn) {
        }cin >> vn[i];
    }
    for (int i = 0; i < n; i++) {
        int l = 0;
        int r = n;
        while (l < r) {
            int med = l + (r - l)/2; // (l + r)/2;
            if (vg[med] <= vq[count]) {
                l = med + 1;
            } else {
                r = med;
            }
        }
    }
}
