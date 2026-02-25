class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        n = len(s)
        num_words = len(words)
        word_length = len(words[0])
        total_length = num_words * word_length

        result = []
        word_counts = {}

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        for i in range(n - total_length +1):
            substring = s[i : i + total_length]
            word_seen = {}
            is_valid = True
            for j in range(0, total_length, word_length):
                word = substring[j : j + word_length]
                if word not in word_counts:
                    is_valid = False
                    break
                word_seen[word] = word_seen.get(word, 0) + 1
                if word_seen[word] > word_counts[word]:
                    is_valid = False
                    break
            if is_valid and word_seen == word_counts:
                result.append(i)
        return result


        
