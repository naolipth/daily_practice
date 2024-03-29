from typing import List


def maximumOddBinaryNumber(s: str) -> str:
    sorted_string = ''.join(sorted(s, key = str.lower, reverse = True))
    one = '1'
    to_change = sorted_string.rfind(one)
    length = len(sorted_string)- 1
    char_list = list(sorted_string)
    char_list[length], char_list[to_change] = char_list[to_change], char_list[length]
    result = "".join(char_list)
    return result


def sortedSquares(nums: List[int]) -> List[int]:
    result = sorted([x**2 for x in nums])
    return result


def bagOfTokensScore(tokens: List[int], power: int) -> int:
        tokens.sort() 
        current_score = 0                  
        maximum_score = 0               
        left_end, right_end = 0, len(tokens) - 1 
        stay_in_loop = True
        
        # Iterate through the tokens using a two-pointer approach
        while left_end <= right_end and stay_in_loop:
            if power >= tokens[left_end]:   
                power -= tokens[left_end]
                current_score += 1
                left_end += 1
                maximum_score = max(maximum_score, current_score)
            elif current_score > 0:             
                power += tokens[right_end]  
                current_score -= 1 
                right_end -= 1               
            else:
                stay_in_loop = False

        return maximum_score

def minimumLength(s: str) -> int:
    left, right = 0, len(s) - 1
    
    while left < right and s[left] == s[right]:
        char = s[left]
        while left <= right and s[left] == char:
            left += 1
        while right >= left and s[right] == char:
            right -= 1
    
    return right - left + 1