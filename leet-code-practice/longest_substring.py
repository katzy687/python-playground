class Solution(object):
    def longestUniqueSubsttr(self, s):

        # Creating a dict to store the last positions of occurrence
        seen = {}
        maximum_length = 0

        # starting the inital point of window to index 0
        start = 0

        for i, curr_char in enumerate(s):
            if curr_char in seen:
                # If we have seen the number, move the start pointer to position after the last occurrence
                start = max(start, seen[curr_char] + 1)

            # Updating the last seen index of the character
            seen[curr_char] = i

            # update most recent maximum length
            maximum_length = max(maximum_length, i - start + 1)
            pass
        return maximum_length


if __name__ == "__main__":
    str_input = "abrkaabcdefghijjxxx"
    # str_input = "aba"
    print(Solution().longestUniqueSubsttr(str_input)) # 10