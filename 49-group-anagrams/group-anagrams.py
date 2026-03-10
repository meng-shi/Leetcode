class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_ana = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic_ana[sorted_word].append(word)

        return list(dic_ana.values())


        