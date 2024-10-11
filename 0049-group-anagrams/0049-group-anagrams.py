class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        
        for str in strs:
            sorted_str = ''.join(sorted(str))
            result[sorted_str].append(str)
        
        return result.values()
            