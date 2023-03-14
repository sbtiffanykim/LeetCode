import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.findall('[a-z]+', paragraph)
        cnt = Counter()
        for word in paragraph:
            if word not in banned: cnt[word] += 1
        return cnt.most_common(1)[0][0]
        