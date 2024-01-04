import re

a = "python is very interesting, 8590537520,8989898989"

res = re.search('\\d{10}',a)
print(res)
res1 = re.match('\\d{10}',a)
print(res1)
res2 = re.findall('\\d{10}',a)
print(res2)

