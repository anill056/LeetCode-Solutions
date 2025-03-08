/*Intuition
The problem requires generating all possible letter combinations from a given digit string, based on a classic phone keypad mapping (just like old T9 keyboards).

Each digit (except 0 and 1) corresponds to a set of characters:

arduino
Kopyala
Düzenle
2 → "abc", 3 → "def", 4 → "ghi", ..., 9 → "wxyz"
Our goal is to generate all possible strings by selecting one letter per digit while preserving the order.

🔹 Example Input: "23"
🔹 Expected Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

This problem naturally translates into a combinatorial tree structure, where each level represents a digit, and each node branches into possible letter choices.

Approach
Instead of using a recursive backtracking approach (which can be costly in terms of call stack space), we leverage an iterative BFS strategy using a queue.

Step-by-Step Execution:
Use a queue (std::queue) to iteratively build letter combinations.
Initialize the queue with an empty string ("").
Iterate through each digit in the input:
Retrieve the corresponding letters from phone_map.
Expand each current string in the queue by appending every possible letter.
Push new combinations back into the queue.
After processing all digits, the queue contains all valid letter combinations.
Return the results stored in the queue.

Complexity
Time complexity:
O(3^n * 4^m)

Space complexity:
O(3^n * 4^m)

Code*/
#include <iostream>
#include <vector>
#include <queue>

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return {}; //base case

        vector<string>phone_map = {"" , "" , "abc" , "def" , "ghi" , "jkl" , "mno" , "pqrs" , "tuv" , "wxyz"};

        queue<string> q;
        q.push(""); //first value of queue

        for(char digit : digits) {
            int q_ofsize = q.size(); //queue size
            string letters = phone_map[digit - '0']; //writes the letter equivalent of the number

            // Expand each existing combination in the queue with the new letters.
            for(int i = 0; i < q_ofsize; i++) {
                string current = q.front(); // Get the front element from the queue.
                q.pop();

                 // Append each letter from the current digit to the existing combination.
                for(char letter : letters) {
                    q.push(current + letter); //Add the new combination to the queue
                }
            }

        }
         // Store all generated combinations in a result vector.
        vector<string> result;
        while(!q.empty()) {
            result.push_back(q.front()); // Add each element in the queue to the result list.
            q.pop(); //Remove it from the queue.
        }
        return result; // Return all possible letter combinations.
    }
};