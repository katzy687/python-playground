class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        exceptions = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        total = 0

        # clean string of exceptions and add to count
        for exc in exceptions.keys():
            occur_count = s.count(exc)
            total += exceptions[exc] * occur_count
            s = s.replace(exc, "")

        # count cleaned data
        for char in s:
            curr_val = int_map[char]
            total += curr_val

        return total


if __name__ == "__main__":
    input = "III"
    # input = "IV"
    # input = "IX"
    # input = "MCMXCIV"
    input = "LVIII"
    sol = Solution()
    print(sol.romanToInt(input))