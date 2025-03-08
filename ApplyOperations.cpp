/*Intuition
The problem requires sequentially modifying the array by merging adjacent equal elements and shifting all zeros to the end. The key idea is to perform these operations in a step-by-step manner while ensuring minimal extra operations and maintaining the relative order of elements.

Approach
First, we iterate through the array to check adjacent elements. If two consecutive elements are equal, we merge them by doubling the first one and setting the second to zero. After this step, we make a second pass to shift all zeros to the end, ensuring the relative order of non-zero elements is preserved.

Complexity
Time complexity:
O(n)

Space complexity:
O(1)

Code*/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        int position = 0;
        int i;

        for (i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        for (i = 0; i < n; i++) {
            if (nums[i] != 0) {
                swap(nums[i], nums[position]);
                position++;
            }
        }
        return nums;
    }
};