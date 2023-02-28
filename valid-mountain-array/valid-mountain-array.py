class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_n = max(arr)
        max_idx = arr.index(max_n)
        valid = 1
        answer = True
        
        l_left = arr[0]
        for i in range(1, max_idx):
            if arr[i] <= l_left:
                valid = 0
                break
            l_left = arr[i]
        
        r_left = arr[max_idx]
        if valid == 1:
            for i in range(max_idx+1, len(arr)):
                if arr[i] >= r_left:
                    valid = 0
                    break
                r_left = arr[i]
        
        if valid == 0 or max_idx == 0 or max_idx == len(arr)-1:
            answer = False
        
        return answer