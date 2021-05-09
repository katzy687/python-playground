# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reversed_string(a_string):
    return a_string[::-1]


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverse()
        l2.reverse()

        str_l1 = ''.join(map(str, l1))
        str_l2 = ''.join(map(str, l2))

        total = int(str_l1) + int(str_l2)
        rev_total = reversed_string(str(total))
        final_list = list(rev_total)
        return final_list



if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    """
    342 + 605 = 807
    answer is [7,0,8]
    """
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))