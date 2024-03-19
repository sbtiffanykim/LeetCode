from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)  # sort each word -> each sorted word would be a key of anagrams
            
        return anagrams.values()