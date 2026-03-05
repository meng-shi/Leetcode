class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        #print(words)
        if len(words) != len(pattern):
            return False

        dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if words[i] in dic.values():
                    return False
                dic[pattern[i]]=words[i]
            else:
                if dic[pattern[i]] != words[i]:
                    return False
        return True
