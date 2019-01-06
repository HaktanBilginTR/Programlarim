i = 0
k = 0
like = []
like2 = []
like3 = []
while 0 <= i < 73:
    like.append(i)
    i += 4
while 0 <= k < 68:
    like2.append(k)
    k += 5
for l in like:
    if l in like2:
        like3.append(l)
print("A ve B'nin Kesişiminin Sayısı :", len(like3))
for ss in like:
    if ss in like2:
        like2.remove(ss)
print("A ve B'nin Birleşiminin Sayısı :", len(like+like2))