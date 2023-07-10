class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num_list = [i for i in range(1, n+1)]
        return list(itertools.combinations(num_list, k))
        