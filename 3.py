def is_not(one, two):
    cnt=0
    for i in range((len(two))):
        if one==two[i]:
            cnt+=1
    if cnt>=1:
        return True
    else:
        return False
        
one = input()
two = input().split()
print(is_not(one,two))