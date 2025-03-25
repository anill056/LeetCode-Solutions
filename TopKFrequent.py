# Intuition
This problem is a classic example of identifying top-k frequent elements — a pattern widely used in search engines, recommendation systems, and analytics dashboards.

We:

1.) Count how many times each number appears using a hash map.

2.) Sort these numbers by frequency in descending order.

3.) Return the first k elements from this sorted list.
# Approach
1.) Frequency Counting:
Use a defaultdict to track how many times each number appears.

2.) Sorting by Frequency:
Convert the dictionary to a list of key-value pairs and sort it in descending order based on the frequency values.

3.) Result Extraction:
Slice the first k keys from the sorted dictionary and return them as the result.

This approach is simple, readable, and works well when the size of the list is not extremely large.

In a world full of noise, let the most frequent voices lead the way!

# Complexity
- Time complexity:
O(n) — To count frequencies (n = number of elements in nums)

O(n log n) — To sort the frequency dictionary by values

O(k) — To slice and return top-k elements

Overall: O(n log n)

- Space complexity:
O(n) — For storing frequencies in the hash map

O(n) — For the sorted dictionary and result list

Overall: O(n)

# Code
```python3 []
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:

            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        frequency = dict(sorted(frequency.items() , key=lambda x : x[1] , reverse= True ))

        result = list(frequency.keys())[:k]

        return result
```