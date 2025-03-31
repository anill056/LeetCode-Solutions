Intuition

🎯 Problem Overview:
We are given an array weights and need to split it into k contiguous groups (bags). The score of a split is defined as the sum of the first and last marble in each group. We're asked to return the difference between the maximum and minimum possible scores for such a split.

The first and last elements of the entire array always contribute to the final score — no matter how we split — so they don’t affect the difference between maximum and minimum scores.

What does matter?
➡️ The sum of the borders between groups — specifically, the elements at the cuts.

If we think about cuts between weights[i] and weights[i+1], each cut contributes a border pair sum:

cut between i and i + 1 -> weights[i] + weights[i+1]
So, we calculate all n - 1 such adjacent pair sums.

Then:

To minimize the score → pick the k-1 smallest pair sums

To maximize the score → pick the k-1 largest pair sums

The difference of these two is our answer.

Approach
1.) Calculate all adjacent pair sums: weights[i] + weights[i+1]

2.) Sort them.

3.) Take the sum of:

The smallest k-1 pair sums for min_score

The largest k-1 pair sums for max_score

4.) Return max_score - min_score

🧩 Reformulating the Problem:
Each split introduces two new boundaries between groups:

The end of the previous group

The start of the next group

Given that every group contributes its first and last marble to the total score, and we split into k groups, the total score becomes:

score = weights[0] + weights[n-1] + sum of 2*(k-1) inner boundary elements  
➡️ So we’re really optimizing the selection of k-1 cuts, where each cut adds the pair (weights[i] + weights[i+1]) to the score.

But since the weights[0] and weights[n-1] are constants, the only variable part is:

sum of (k - 1) chosen pair sums (weights[i] + weights[i+1])
🧠 Key Insight:
We can precompute all n-1 pair sums (weights[i] + weights[i+1]) — each represents a possible boundary between two bags.

We must choose k-1 of these boundaries to maximize the total score
Or choose k-1 to minimize it.

This becomes a selection problem on the sorted list of pair sums.

🚀 Why This Works:
Instead of trying all possible segmentations (which would be exponential), we reduce the problem to picking optimal border pairs — which can be done greedily in a single sort. Clean, efficient, and elegant.

🧩 Powerful Insight:
The problem secretly reduces to a greedy border optimization — identifying the most/least valuable places to cut. It’s a great example of transforming a segmentation problem into a sorting one.

**Complexity**
- Time complexity:

O(n log n): for sorting the n-1 pair sums.

Other operations are linear.

- Space complexity:

O(n): storing n-1 pair sums.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
**Code**
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        Find the difference between maximum and minimum scores when distributing marbles into k bags.
        
        Args:
            weights: A list of integers representing weights of marbles
            k: The number of bags to distribute marbles into
            
        Returns:
            The difference between maximum and minimum scores
            """

        # Edge case: if k=1 or k=len(weights), there's only one way to distribute
        if k == 1 or  k == len(weights):
            return 0

        # For each potential cut between positions i and i+1, calculate the cost
        # This cost equals weights[i] + weights[i+1]
        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i+1])

        #Sort the pair nums
        pair_sums.sort()

        # We need to make k-1 cuts
        # For minimum score: use the k-1 smallest pair sums as cut points
        # For maximum score: use the k-1 largest pair sums as cut points
        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])

        # Note: The first and last elements of weights always contribute to the total cost
        # regardless of how we split (they're always endpoints of bags)
        # So they don't affect the difference between max and min scores
        
        
        return max_score - min_score
----------------------------------------------------------------------------------------------------------------------------------------------------------------