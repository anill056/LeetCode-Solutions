**Intuition**
For each character, all of its occurrences must be in the same partition.
When we encounter a character, we need to include all of its occurrences in the
current partition, which means extending the partition end to at least the last
occurrence of that character. As we process more characters within the current
partition range, we may need to further extend the partition if we encounter
characters with last occurrences beyond our current partition end.
Once we reach the current partition's end index, we know we've processed all
characters that need to be in this partition, and can safely start a new one.

**Approach**
Find the last occurrence of each character in the string.
Use a greedy approach to form partitions:
For each character, extend the current partition to include its last occurrence.
When we reach the current partition's end, create a new partition.
Return the sizes of these partitions.
**Complexity**
**Time complexity:**

O(n) where n is the length of string s.
We iterate through the string twice: once to build the last_occurrence dictionary
and once to determine the partitions.
Both iterations are linear in the size of the input.
Space complexity:

O(1) since the input contains only lowercase English letters.
The last_occurrence dictionary stores at most 26 entries (for lowercase English letters).
The result list stores the sizes of partitions, which is at most n (in the worst case,
each character forms its own partition).

-----------------------------------------------------------------------------------------
**Code**
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last occurrence index of each character
        last_occurence = {}

        for i , char in enumerate(s):
            last_occurence[char] = i
        
        # Initialize variables to track partition boundaries
        result = []
        start = 0
        end = 0

        # Iterate through the string to find partitions
        for i , char in enumerate(s):

            # Expand the current partition's end if needed
            end = max(end , last_occurence[char])


            # If we've reached the end of the current partition
            if i == end:

                # Calculate partition length and add to result
                partition_length = end - start + 1
                result.append(partition_length)

                # Update start for the next partition
                start = i + 1

        return result
----------------------------------------------------------------------------------------------
