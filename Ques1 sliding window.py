
def find_longest_substring_length(input_string):
    window_chars = set()
    left_pointer = 0
    max_length = 0
    for right_pointer in range(len(input_string)):
        new_char = input_string[right_pointer]
        while new_char in window_chars:
            char_at_left = input_string[left_pointer]
            window_chars.remove(char_at_left)
            left_pointer = left_pointer + 1
    
        window_chars.add(new_char)
        current_length = right_pointer - left_pointer + 1
        if current_length > max_length:
            max_length = current_length
    return max_length