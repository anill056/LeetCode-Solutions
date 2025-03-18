Intuition
Anagrams are words that contain the same letters but in different orders. If we sort the letters in an anagram, they always form the same sorted version. This unique property allows us to group words efficiently by using a hash map (dictionary) where the key is the sorted version of the word and the value is a list of words that share this sorted form.

Approach
1.) Hash Map for Fast Lookup - We use a defaultdict(list) to store anagrams.
2.) Sorting as Key - Each word is sorted alphabetically to form a unique key.
3.) Grouping Anagrams - Words that share the same sorted key are added to the same list.
4.) Returning the Result - Convert the dictionary values to a list of lists.
5.) This approach leverages Python’s built-in sorting and dictionary operations, making it both clean and efficient.

Why This Works So Well? 🎯
Fast Retrieval 🏎️ - Hash map lookup is O(1)
Sorting is Stable 🎯 - Python’s sorted() ensures consistency.
Efficient Storage 📦 - Only unique sorted keys are stored, minimizing overhead.

Perfect for Large Datasets & Competitive Coding! 🚀

Complexity
Time complexity:
O(NMLogM)

Space complexity:
O(NM)
We store each word in the dictionary.)

Code
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        anagram_dict = defaultdict(list)

        for word in strs:
            # Sort the word and use it as a key
            sorted_words = tuple(sorted(word))
         # Append the original word to its corresponding anagram group
            anagram_dict[sorted_words].append(word)

        # Return grouped anagrams as a list of lists
        return list(anagram_dict.values())

        