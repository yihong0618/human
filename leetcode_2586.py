class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        words = words[left : right + 1]
        ww = {"a", "e", "i", "o", "u"}
        c = 0
        for i in words:
            if i[0] in ww and i[-1] in ww:
                c += 1
        return c
