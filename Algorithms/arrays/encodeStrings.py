# Encode and Decode Strings
# LEETCODE PREMIUM: https://leetcode.com/problems/encode-and-decode-strings/

# This is a handy trick when encoding strings!
# Notice we add the '#' and string afterwards 

class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ''
        tempList = list()
        for string in strs:
            tempList.append(str(len(string)) + '#' + string)
        newString = ''.join(tempList)
        return newString

    def decode(self, s: str) -> List[str]:
        i = 0
        returnList = list()
        while i < len(s):
            length = list()
            while s[i] != '#':
                length.append(s[i])
                i += 1
            totalLength = int(''.join(length))
            tempString = s[i+1:totalLength+i+1]
            returnList.append(tempString)
            i += totalLength + 1
        return returnList
