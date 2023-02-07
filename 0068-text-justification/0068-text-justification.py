class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        i = 0
        result = []
        while i < n:
            line = []
            char_count = 0
            line_app = line.append  
            while i < n and char_count + (len(line)) + len(words[i]) <= maxWidth:
                line_app(words[i]) 
                char_count += len(words[i])  
                i += 1  
            if len(line) > 1:
                space = (maxWidth - char_count) // (len(line) - 1)
                
                space_rem = (maxWidth - char_count) % (len(line) - 1)
            else: 
                space = 0
                space_rem = 0
            if i == n:  # last line
                line_string = " ".join(line)
            else: 
                line_string = [line[0]]
                line_str_app = line_string.append 
                for j in range(1, len(line)):
                    if space_rem:
                        line_str_app(" " * (space + 1))
                        space_rem -= 1
                    else:
                        line_str_app(" " * space)
                    line_str_app(line[j])
                line_string = "".join(line_string)
            line_string += (" " * (maxWidth - len(line_string)))

            result.append(line_string)
        return result