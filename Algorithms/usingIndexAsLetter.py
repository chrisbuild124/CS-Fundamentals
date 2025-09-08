# Trick: Use the index in the array as the letter's value
# This can be applied to many things (not just letters) - for example, bucket sort
# Leetcode link: https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:     
            checkList = [0] * 26
            for c in string:
                checkList[ord(c) - ord('a')] += 1
            hashMap[tuple(checkList)].append(string)
        return list(hashMap.values())
