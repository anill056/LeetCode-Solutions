#include <iostream>

class Solution {
public:
    int romanToInt(string s) {
        int values[200] = {};
        values['I'] = 1; values['V'] = 5; values['X'] = 10; values['L'] = 50;
        values['C'] = 100; values['D'] = 500; values['M'] = 1000;
        int total=0;

        int len = s.length();

        for(int i = 0; i<len;i++) {
            if(i<len-1 && values[s[i]] < values[s[i+1]]) {
                total -= values[s[i]];
            }
            else {
                total += values[s[i]];
            }
        }
        return total;
    }
};