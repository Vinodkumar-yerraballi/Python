# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr=set(arr)
#     arr.remove(max(arr))
#     print(max(arr))

def runerup_score(score):
    winer_score=-99999
    runer_score=-99999
    for i in score:
        if (i>winer_score):
            winer_score,runer_score=i,winer_score
        elif (i < winer_score and i > runer_score):
            runer_score =i
    return runer_score
score=[1,4,5,8,9,7]
print(runerup_score(score))
ms=[]
sc=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ms.append([name,score])
        sc.append(score)
sc=list(set(sc))
sc.sort()
sc=[str(x) for x in sc]
for i in range(len(ms)):
    for j in range(len(ms[i])):
        ms[i][j]=str(ms[i][j])
fi=[]
for i in list(ms):
    if i[1]==sc[1]:
        fi.append(i[0])
fi.sort()
for i in fi:
    print(i)
