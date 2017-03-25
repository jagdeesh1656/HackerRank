t = input().strip()
for i in range(int(t)):
    funny = 0
    s = input().strip();
    r = s[::-1]
    for i in range(1,len(s),1):
        if abs(ord(s[i]) - ord(s[i-1])) == abs(ord(r[i]) - ord(r[i-1])):
            funny = 1
        else:
            funny = 0
            break
    if funny:
        print ("Funny")
    else:
        print ("Not Funny")
    