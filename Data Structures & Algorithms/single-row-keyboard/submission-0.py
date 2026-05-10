class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = defaultdict(int)
        c = 0
        prev_idx = keyboard[0]
        for idx, val in enumerate(keyboard):
            hashmap[val] = idx
        for char in word:
            if char in hashmap:
                c = c + abs(hashmap[char] - hashmap[prev_idx])
                prev_idx = char
        return c

        

        