class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # quick check
        if len(ransomNote) > len(magazine):
            return False
        
        dic = {}
        for letter in magazine:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        for letter in ransomNote:
            if letter not in dic:
                return False
            elif dic[letter] == 1:
                del dic[letter]
            else:
                dic[letter] -= 1
        return True

        # time is O(len(magazine)+len(ransomNote))



