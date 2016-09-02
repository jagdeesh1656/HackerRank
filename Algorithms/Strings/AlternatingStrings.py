n = input().strip();
for i in range(int(n)):
    dell = 0
    s = input().strip()
    for j in range(len(s) - 1):
        if s[j] == s[j+1]:
            dell = dell + 1

    print (dell)