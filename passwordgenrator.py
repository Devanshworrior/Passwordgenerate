import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}()*@;/,\._-'"
all = lower + upper + number + symbols
length = 25
password = "".join(random.sample(all,length))
print (password)
# PassWord Genrator Created Succefuuly