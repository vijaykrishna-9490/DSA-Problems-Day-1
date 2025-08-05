n = input()
new_str = ""
for i in n:
    if i.isupper():
        new_str+=i.lower()
    else:new_str+=i.upper()
print(new_str)