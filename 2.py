def text_t(txt):
    txt=txt.lower()
    n = "aeiouy"
    new_s = ''
    for i in txt:
        if i not in n:
            new_s+=i+"o"+i
        else:
            new_s+=i
    return new_s

txt = input("Write your text ---> ")
print(text_t(txt))