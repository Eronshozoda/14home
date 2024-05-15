list1 = input().split()
list2 = input().split()
cnt=0
for i in list1:
    for j in list2:
        if i==j:
            cnt+=1
if cnt>=1:
    print(True)
else:
    print(False)