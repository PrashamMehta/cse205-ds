class Solution:
    def frequencySort(self, s: str) -> str:
        # Count character frequencies
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Sort characters based on frequencies in decreasing order
        sorted_chars = sorted(char_count, key=lambda char: -char_count[char])
        
        # Create the sorted string
        result = ""
        for char in sorted_chars:
            result += char * char_count[char]
        
        return result
