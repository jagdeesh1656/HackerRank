def isPalindrome(string):
    half = int((len(string) / 2))
    if string[:half] == string[-half:][::-1]:
        return True
    else:
        return False

t = int(input().strip())
for case in range(t):
    string = input().strip()
    if isPalindrome(string):
        print ("0")
        continue
    half = int((len(string) / 2))
    strlen = len(string) - 1
    first = 0
    count = 0
    while strlen > first:
        if string[first] != string[strlen]:
            count = abs(count) + abs(ord(string[strlen]) - ord(string[first]))
        first = first + 1
        strlen = strlen - 1
    print (abs(count))