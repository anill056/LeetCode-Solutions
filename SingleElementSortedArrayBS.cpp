# Intuition
- The array is sorted, and every element appears exactly twice — except one.
- In such arrays, **duplicates always occupy even-odd index pairs**: (0-1), (2-3), etc.
- When a single non-duplicate disrupts this structure, **the pattern breaks**.
- So we can use binary search to find **where this break happens** by examining indices. 

# Approach
1. Apply binary search on index pairs (not values).
2. Always ensure mid is even — so it aligns with pair starts.
3. Compare nums[mid] with nums[mid + 1] to detect broken pairing.
4. Narrow down the search until only the single element remains.

# Complexity
- Time complexity:
O(Log n)
- Each iteration eliminates half of the remaining elements.

- Space complexity:
O(1)
- No extra memory is used; purely in-place logic.

# Code
```cpp []
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int middle = left + (right - left) / 2;

            // Force middle to be even to compare with its pair
            if(middle % 2 == 1) {
                middle--;
            }
            

            // If the pair is valid, move right
            if(nums[middle] == nums[middle + 1]) {
                left = middle + 2;
            }

            // Pair is broken, single element must be on the left side
            else right = middle;
        }


        // Left points to the single element
        return nums[left];
    }
};
```