class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l_logs = list()
        d_logs = list()
        
        for l in logs:
            if l.split(' ')[1].isdigit(): d_logs.append(l)
            else: l_logs.append(l)
        l_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return l_logs + d_logs