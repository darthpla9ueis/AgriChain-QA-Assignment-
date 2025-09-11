
def check_if_unique(substring):
    chars_seen = []
    for char in substring:
        if char in chars_seen:
            return False
        chars_seen.append(char)
    return True
def find_longest_substring_brute_force(s):
    n = len(s)
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            current_substring = s[i:j+1]
            if check_if_unique(current_substring):
                if len(current_substring) > max_length:
                    max_length = len(current_substring)
    return max_length