class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = {}
        
        # Count the occurrences of each character in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        sorted_string = ""
        
        # Build the sorted string based on the order
        for char in order:
            if char in char_count:
                sorted_string += char * char_count[char]
                del char_count[char]
        
        # Add any remaining characters not in order
        for char in char_count:
            sorted_string += char * char_count[char]
        
        return sorted_string
