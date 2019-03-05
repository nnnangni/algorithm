word = str(input())
alp = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in alp:
    if i in word:
        word = word.replace(i,"_")
print(len(word))
