# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        This code takes a string as input and returns the length of the longest within the string that does not contain any repeating characters.

        The code initializes a maximum length variable to 1 and sets two pointers, i and j, to the beginning and second character of the string, respectively. It then enters a while loop that continues until j reaches the end of the string.

        Within the loop, the code checks if the character at index j is already in the substring between i and j. If it is, the code updates i to the index of the first occurrence of that character plus one, effectively moving the start of the substring to the character immediately after the first occurrence of the repeated character. If the character is not already in the substring, the code updates the maximum length variable if the length of the current substring (j-i+1) is greater than the current maximum length.

        Finally, the code returns the maximum length variable, which represents the length of the longest substring without repeating characters.

        Time Complexity: O(n)
        Space Complexity: O(1)

        :param s: string
        :return: int
        '''
        if len(s) == 0:
            return 0
        max_len = 1
        i = 0
        j = 1
        while j < len(s):
            if s[j] in s[i:j]:
                i = i + s[i:j].index(s[j]) + 1
            else:
                max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
