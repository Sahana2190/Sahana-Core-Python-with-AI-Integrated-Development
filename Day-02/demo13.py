'''
write a program to demonstrate a simple Python script.
1. empty list
2. dispaly no of elements in the list
3. use while loop - limit is 5
a. read a hostname from user input
b. append the hostname to the list
4. siplay no of elements in the list
5. use for loop - terate hrough the list
6. read a hostname from <stdin>
7. test input hostname is existing or not in the list
8. modify the hostname ,                |- add the hostname
9. display the list of hostnames - use for loop
'''
host = []
print(f"Number of elements in the list: {len(host)}")

i = 0
while i < 5:
    hostname = input("Enter a hostname: ")
    host.append(hostname)
    i += 1

print(f"Number of elements in the list: {len(host)}")

for h in host:
    print(h)    


host_name = input("enter a hostname:")
if host_name in host:
    host[-1] = host_name
else:
    host.append(host_name)

print("Updated list of hostnames:")
for h in host:
    print(h)