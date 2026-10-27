#include <iostream>
using namespace std;

// comparator for sorting based on last digit
bool cmp(int a, int b) {
    int lastDigitA = a%10;
    int lastDigitB = b%10;

    if(lastDigitA < lastDigitB) {
        return true;
    } else {
        return false;
    }
}

int main() {
    // Your code here
    int a[] = {12, 54, 1, 3, 69, 70, 85};
    int n = 7;

    sort(a, a+n, cmp);
    for (int i = 0; i<n; i++) {
        cout << a[i] << ' ';
    }
    return 0;
}