def lengthoflongestsubstring(s):
    charset = set()
    a = 0
    res = 0
    for b in range(len(s)):
        while s[b] in charset:
            charset.remove(s[a])
            a += 1
        charset.add(s[b])
        res = max(res, b - a + 1)
    return res

# testing
print(f"Result for 'abcabcabcb': {lengthoflongestsubstring('abcabcabcb')}")
print(f"Result for 'baaab': {lengthoflongestsubstring('baaab')}")
print(f"Result for 'asffdg': {lengthoflongestsubstring('asffdg')}")

 