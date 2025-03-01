#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int low = 0, high = m;
        while (low <= high) {
            int partitionM = (low + high) / 2;
            int partitionN = (m + n + 1) / 2 - partitionM;

            int maxLeftM = (partitionM == 0) ? INT_MIN : nums1[partitionM - 1];
            int minRightM = (partitionM == m) ? INT_MAX : nums1[partitionM];

            int maxLeftN = (partitionN == 0) ? INT_MIN : nums2[partitionN - 1];
            int minRightN = (partitionN == n) ? INT_MAX : nums2[partitionN];

            if (maxLeftM <= minRightN && maxLeftN <= minRightM) {
                if ((m + n) % 2 == 0) {
                    return (max(maxLeftM, maxLeftN) + min(minRightM, minRightN)) / 2.0;
                }
                else {
                    return (max(maxLeftM, maxLeftN));
                }

            }
            else if (maxLeftM > minRightN) {
                high = partitionM - 1;
            }
            else {
                low = partitionM + 1;
            }

        }
        return 0.0;
    }
};


/*
Intuition
Instead of merging two sorted arrays, we can find the median by performing a binary search on the smaller array. By partitioning the two arrays at the correct position, we ensure that the left half contains smaller elements and the right half contains larger elements. This allows us to determine the median without explicitly merging the arrays."

Approach
1.)Always apply binary search on the smaller array (nums1).
2.)Perform binary search to find a partition (partitionX) in nums1.
3.)Determine the corresponding partition in nums2 (partitionY)
4.)Check partition validity:
maxLeftX ≤ minRightY and maxLeftY ≤ minRightX conditions must hold.
5.)Calculate median:
If the total number of elements is odd, return max(maxLeftX, maxLeftY).
If the total number of elements is even, return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0.

Complexity
Time complexity:
O(log(m+n))

Space complexity:
o(1) */