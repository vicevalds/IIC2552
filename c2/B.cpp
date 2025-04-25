
int func(){
    int i = 0;
}

int main(){
    int lo = 0, hi = 999999;
    while (lo <= hi) {
        int mid = lo + (hi - lo)/2;
        if (func(mid)){
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return 0;
}
