import re


strings = input()
result = []
is_lower = re.compile("[a-z]")
is_upper = re.compile("[A-Z]")
for i in strings:
    if is_lower.findall(i):
        num = ord(i)
        num += 13
        if num>122:
            num = 97 + (num-123)
        result.append(chr(num))
    elif is_upper.findall(i):
        num = ord(i)
        num += 13
        if num>90:
            num = 65 + (num-91)
        result.append(chr(num))
    else:
        result.append(i)
# a b c d e f g h i j k l m n o p q r s t u v w x y z
print("".join(result))