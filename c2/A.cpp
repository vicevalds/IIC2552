#include <bits/stdc++.h>
using namespace std;

int main()
{
int n, q;
cin >> n >> q;
vector<int> vg(n);
for (int i = 0;i < n; i++) {
    cin >> vg[i];
}
vector<int> vq(q);
for (int i = 0;i < q; i++) {
    cin >> vq[i];
}
int count = 0;
for (int i = 0; i < n; i++) {
    int l = 0;
    int r = n;
    while (l < r) {
        int med = (l + r)/2;
        if (vg[med] <= vq[count]) {
            l = med + 1;
        } else {
            r = med;
        }
    }
    cout << l << " ";
    count += 1;
}
}
