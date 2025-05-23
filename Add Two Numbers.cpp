/*Intuition
The problem requires us to add two numbers represented as reversed linked lists. Instead of reversing the lists or converting them into numbers, we can directly perform digit-wise addition while traversing both lists simultaneously. The key challenge is handling the carry when the sum of two digits exceeds 9.

Approach
1.)Initialize a dummy head node to simplify linked list construction.
2.)Use a pointer to traverse both lists simultaneously.
3.)At each step, compute the sum of corresponding digits from both lists and the carry from the previous step.
4.)If the sum is greater than 9, store only the last digit and carry over the remainder.
5.)Continue until both lists are fully traversed, and if a carry remains, add a new node at the end.

Complexity
Time complexity:
O(n)

Space complexity:
O(n)

Code*/
#include <iostream>

using namespace std;

/*struct ListNode { //linked list node struct
    int val;
    ListNode* next;
    ListNode() : val(0) , next(NULL) {} //constructor default value

    ListNode(int a) : val(a) , next(NULL) {} //constructor int value
};*/

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* tempHead = new ListNode(0); //temporary starting node
        ListNode* current = tempHead;  //The pointer we will use when creating the new linked list
        int carry = 0; //Carry initially 0

        while(l1 != NULL || l2 != NULL || carry) {
            int sum = carry; //we are adding carry first.

            if(l1) { //If l1 exists, add its value
                sum += l1->val;
                l1 = l1->next;
            }

            if(l2) { //If l2 exists, add its value
                sum += l2->val; 
                l2 = l2->next;
            }

            carry = sum / 10; //If total is 10 or greater, calculate carry
            sum = sum % 10; //Take only the ones digit as the value of the new node

            //Create and add new node
            current->next = new ListNode(sum);
            current = current->next;
        }

        return tempHead->next; // Return the result skipping the starting node
    }
};
