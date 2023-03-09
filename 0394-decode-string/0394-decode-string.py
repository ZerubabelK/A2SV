class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i, string):
            if string[i] == ']':
                return [current_string, i]
            j = i
            current_string = []
            while j < len(string):
                if string[j] == '[':
                    returned_string, end_index = decode(j+1, string)
                    if current_string and current_string[-1].isdigit():
                        number = []
                        while current_string and current_string[-1].isdigit():
                            number.append(current_string.pop())
                        returned_string = returned_string * int(''.join(number[::-1]))
                    current_string.append(returned_string)
                    j = end_index + 1
                elif string[j] == ']':
                    return [''.join(current_string), j]
                else:
                    current_string.append(string[j])
                    j += 1
            while current_string and current_string[-1].isdigit():
                current_string.pop()
            return ''.join(current_string)
        return decode(0, s)