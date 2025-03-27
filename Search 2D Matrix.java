**Intuition**

Think of the matrix like a book with sorted pages:

 - You first find the right page (row).

 - Then you scan that page (row) to find the exact word (target).

Instead of flattening the matrix into a 1D array, we break the problem into two cleaner sub-problems:

1.) Find the row.

2.) Search within it.

This makes the logic more intuitive and easy to follow, especially during interviews.

**Approach**
This solution uses a two-step binary search strategy:

1.) First, it identifies the correct row where the target could possibly exist.

2.) Then, it performs a binary search within that row to locate the target.

This works effectively because the matrix has two key properties:

Each row is sorted in ascending order.

The first element of each row is greater than the last element of the previous row.

These properties allow us to treat the matrix as a collection of sorted, non-overlapping segments.

**Complexity**
Time complexity:
Binary Search over rows: O(log m)
Binary Search within a row: O(log n)
→ Total: O(log m + log n)

Which is effectively the same as O(log (m * n)) — very efficient.

Space complexity:
No extra space used.
→ Space: O(1)


**Code**

-------------------------------------------------------------------------------
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        // Define the row search boundaries (for binary search)
        int low = 0;
        int high = (matrix.length - 1);
        int row = -1; // Will store the row index that may contain the target


        // Phase 1: Binary search to find the correct row
        while (low <= high) {
            int middle = low + (high - low) / 2; // Avoid overflow in middle calculation

             // Check if target could be in this row (between first and last element)
            if (matrix[middle][0] <= target && target <= matrix[middle][matrix[middle].length - 1]) {
                row = middle; // Correct row found
                break;
            }

             // If target is greater than the last element, search lower part
            else if (matrix[middle][0] < target) low = middle + 1;

             // If target is smaller than the first element, search upper part
            else high = middle - 1;
        }

      // If no valid row found, target does not exist in matrix
        if(row == -1) return false;


         // Phase 2: Binary search within the selected row
        int left = 0;
        int right = (matrix[row].length - 1);

        while (left <= right) {
            int middle = left + (right - left) / 2;

            // Target found
            if (matrix[row][middle] == target) return true;

            // Target is greater, move right
            else if (matrix[row][middle] < target) left = middle + 1;

            // Target is smaller, move left
            else right = middle - 1;
        }

        // Target not found in the selected row
        return false;
    }
}
--------------------------------------------------------------------------------