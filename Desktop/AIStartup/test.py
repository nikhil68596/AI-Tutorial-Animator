def most_frequent_chars(text):
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Count character frequencies
    frequency = {}
    for char in cleaned_text:
        frequency[char] = frequency.get(char, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all characters with the maximum frequency
    most_common = [char for char, freq in frequency.items() if freq == max_freq]
    
    return most_common

print(most_frequent_chars("aaAA7"))

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0


    for num in num_set:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            current_streak = 1


            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1


            longest = max(longest, current_streak)


    return longest
print(longest_consecutive([2,4,7,3,1,0,-1, 100]))

def add_commas(number):
    num_str = str(number)
    parts = num_str.split('.')
    integer_part = parts[0]
    
    result = ''
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            result = ',' + result
        result = digit + result
    
    if len(parts) > 1:
        result += '.' + parts[1]
    
    return result

print(add_commas(-1234567.89))

from collections import deque


def is_palindrome(text):
    # Create a deque of lowercase alphanumeric characters
    char_deque = deque(char.lower() for char in text if char.isalnum())
    
    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))