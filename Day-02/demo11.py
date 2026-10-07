'''
s = '123456789'
Given string s,
Write a python program calculate sum of the digits.
use: for loop.
'''
s = '123456789'
total = 0
for var in s:
    total = total + int(var) #print(var,type(var))

print(f"Sum of the digits in string s is:{total}")

#example2 - iterate over a list of IP addresses and simulate pinging each one
ip_addresses = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]

for ip in ip_addresses:
    print(f"Pinging {ip}...")