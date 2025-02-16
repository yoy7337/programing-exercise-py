'''
反轉字串
使用 forloop
不要使用 string[::-1]
apple -> elppa
database -> esabatab
'''

str = input("Please input string, we will reverse it: ")
reversed_str = ""

for i in range(0, len(str)):
  # print(str[len(str) - i - 1])
  reversed_str = reversed_str + (str[len(str) - i - 1])

print(reversed_str)

