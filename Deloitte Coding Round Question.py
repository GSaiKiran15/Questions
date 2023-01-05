import string


def convert_single(n):
    l = len(str(n))
    while l > 1:
        o = 0
        for i in str(n):
            o += int(i)
        n = o
        l = len(str(n))
    return n


name = input("")
birthYear = int(input())
luckyChar = input()

name_n = 0
year_n = 0
alphabet_n = 0


arr = list(string.ascii_lowercase)
print(arr)

for i in name.lower():
    if i in 'aeiou':
        name_n += 1
name_n = convert_single(name_n)

temp = 0
for i in str(birthYear):
    temp += int(i)
print(temp)
temp = convert_single(temp)

alphabet_n = arr.index(luckyChar.lower())+1
alphabet_n = convert_single(alphabet_n)
print(f"name {name_n}, temp {temp}, alpha {alphabet_n}")
print(str(name_n)+str(temp)+str(alphabet_n))
if alphabet_n == name_n and name_n == temp:
    print(1)
else:
    print(0)
