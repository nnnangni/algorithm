# 5개 중에 3개 고르기
# for i in range(1,6)
fivelist = [1,2,3,4,5]
for idxi,vali in enumerate(fivelist):
    for idxj, valj in enumerate(fivelist):
        if idxi!=idxj:
            for idxk, valk in enumerate(fivelist):
                if idxi!=idxk and idxj!=idxk:
                    print(vali, valj, valk)