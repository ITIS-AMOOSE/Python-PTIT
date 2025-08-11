P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    line = input()
    if line[0] == '0': break
    k_str, S = line.split()  

    k = int(k_str)

    ans = ""
    for i in S:
        indx = P.index(i)
        ans += P[(indx + k) % 28]

    print(ans[::-1])