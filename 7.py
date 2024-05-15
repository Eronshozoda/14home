def is_ascending(my_list):
    if len(my_list)==int(1):
        return True
    else:
        for i in range(1,len(my_list)):
            if int(my_list[i-1])<int(my_list[i]):
                pass
            else:
                return False
    return True
my_list = input().split()
print(is_ascending(my_list))