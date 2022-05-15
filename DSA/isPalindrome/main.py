def isPalindrome(s):
    word = ''.join(ch for ch in s if ch.isalnum()).lower()
    length = len(word)
    last = length - 1
    first = 0


    while first < last:
        if word[first] != word[last]:
            return False
        else:
            first += 1
            last -= 1
    return "found"


s = "A man, a plan, a canal: Panama"
isPalindrome(s)