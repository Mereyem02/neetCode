class Solution:
    def isAnagram(self, s: str, t: str) -> bool :
        s=''.join(sorted(s))
        t=''.join(sorted(t))
        if len(s)==len(t) and s==t :
            return True
        return False

        