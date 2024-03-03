def maximumOddBinaryNumber(self, s: str) -> str:
    sorted_string = ''.join(sorted(s, key = str.lower, reverse = True))
    one = '1'
    to_change = sorted_string.rfind(one)
    length = len(sorted_string)- 1
    char_list = list(sorted_string)
    char_list[length], char_list[to_change] = char_list[to_change], char_list[length]
    result = "".join(char_list)
    return result