Intuition
To maximize the final score using at most k operations, we need to multiply the score by the most "valuable" numbers first. A number’s value is not just its magnitude, but also how many unique subarrays it dominates in terms of prime score (number of distinct prime factors).

So, the idea is:

Compute a prime score for each element.

Use a monotonic stack to find the range of subarrays where each element is the maximum prime score.

Multiply the current score by the elements that dominate the most subarrays, starting from the largest numbers.

This is a combination of greedy selection and mathematical reasoning.

Approach
1.) Prime Score Calculation:

For each number, compute its number of distinct prime factors (its "prime score").
2.) Monotonic Stack Ranges:

Use two passes with a monotonic stack to find the range of subarrays where each number is the maximum prime score.

Left boundary: first greater on the left.

Right boundary: first greater-or-equal on the right.

3.) Subarray İnfluence Calculation:

For each element, count how many subarrays it dominates:
(i - left[i]) x (right[i] - i)
4.) Greedy Multiplication:

Sort elements by value descending order.
Repeatedly multiply the current score by each element’s value as many times as its subarray influence allows — until k operations are used.
Complexity
Time complexity:

Prime Score Calculation : O(n · √num) (worst-case for - - factorization)
Monotonic Stack Processing : O(n)
Influence Calculation : O(n)
Sorting Elements : O(n log n)
Score Computation : O(n)
Total : O(n √m + n log n) where m = max(nums[i])
Space complexity:

O(n) for storing prime scores, boundaries, subarray influences, and the monotonic stack.

O(1) auxiliary space for prime factorization (excluding output).

Code
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Compute prime scores for each element in the array
        # Prime score = number of distinct prime factors
        prime_scores = [self.count_distinct_primes(num) for num in nums]

        # Step 2: Use monotonic stack to find left and right bounds for each element
        # where it is the maximum prime score in a subarray
        left = [-1] * n  # Index of previous greater prime score
        right = [n] * n  # Index of next greater or equal prime score
        stack = []

        # Calculate left boundaries
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Clear the stack for reuse
        stack.clear()

        # Calculate right boundaries
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Step 3: Calculate the number of subarrays in which each element
        # is the maximum prime score holder
        influence = []
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            influence.append((nums[i], count))

        # Step 4: Sort the elements by their value in descending order
        # to maximize score by using larger numbers first
        influence.sort(reverse=True)

        score = 1

        # Step 5: Select elements greedily until k operations are used
        for value, count in influence:
            if k == 0:
                break
            use = min(k, count)
            score = (score * pow(value, use, MOD)) % MOD
            k -= use

        return score

    def count_distinct_primes(self, num: int) -> int:
        """
        Returns the number of distinct prime factors of a given number.
        For example:
        - 10 -> 2 (factors: 2, 5)
        - 12 -> 2 (factors: 2, 3)
        - 30 -> 3 (factors: 2, 3, 5)
        """
        if num == 1:
            return 0

        primes = set()

        # Check for factor 2
        if num % 2 == 0:
            primes.add(2)
            while num % 2 == 0:
                num //= 2

        # Check for odd factors starting from 3
        factor = 3
        while factor * factor <= num:
            if num % factor == 0:
                primes.add(factor)
                while num % factor == 0:
                    num //= factor
            factor += 2

        # If remaining num is a prime number
        if num > 1:
            primes.add(num)

        return len(primes)