/*Intuition
The problem requires finding two numbers in an unsorted array that sum up to a given target. Instead of using brute force to check every pair (O(n²) complexity), we can store each number's complement (target - nums[i]) in a hash map while iterating through the array. This allows us to check for the required pair in constant time O(1), making the overall solution much more efficient.

Approach
1.) Create a hash map (unordered_map<int, int>) to store numbers and their indices.

2.) Iterate through the array:

Compute the complement (target - nums[i]).
If the complement already exists in the hash map, return both indices.
Otherwise, store nums[i] with its index in the hash map for future lookups.

3.) Since a solution is guaranteed, the function always returns a valid pair.

Complexity
Time complexity:
O(n)

Space complexity:
O(n)

Code*/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(); //size of nums (n)
        unordered_map<int,int> numsMap; //Hash Map is created as {element, index}

        //We scan the array in one pass
        for(int i = 0; i < n; i++) {
            int complement = target - nums[i]; // We are calculating missing complement.

            //If the complement was added before, it means that the solution has been reached
            if(numsMap.find(complement) != numsMap.end()) { 
                return {numsMap[complement] , i}; //Returned two indexes found
            }

            //Add current element to hash map (may be found as complement in future)
            numsMap[nums[i]] = i;
        }

        return {};  //This is never reached because the solution is guaranteed

    }
};