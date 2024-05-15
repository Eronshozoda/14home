def list_len(my_list,number):
    for i in range(len(my_list)):
        if len(my_list[i])>=number:
            print(my_list[i],end=" ")
list1 = input().split()
n = int(input())
list_len(list1,n)