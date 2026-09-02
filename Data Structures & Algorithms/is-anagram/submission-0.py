class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(s.split()).lower()
        t = "".join(t.split()).lower()

        if sorted(s) == sorted(t):
            return True

        return False