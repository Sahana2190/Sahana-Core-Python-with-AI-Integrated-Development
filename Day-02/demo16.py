'''Write a python program:
1. create an empty dict
2. display no.of items - use len()
3. use - while loop - limit is 5
     - read hostname from <STDIN> (ex: host01)
     - read IP from <STDIN>    (ex: 10.20.30.40)
     - add input details(hostname,IP) to an existing dict
       dictName[New_Key] = Value

4. display no.of items
|
5. use for loop 
    - display hostname and IP
|
6. read a hostname from <STDIN>
7. test - input hostname is exists -> update IP 127.0.0.1
                |
                not
                |
                create a new hosts - 127.0.0.1 
|
8. display updated dict details.'''

dict={}
print("Number of items:", len(dict))
i=0
while i < 5:
    hostname = input("Enter hostname: ")
    ip = input("Enter IP: ")
    dict[hostname] = ip
    i += 1

print("Number of items:", len(dict))

for var in dict:
    print("Hostname:", var, "IP:", dict[var])

h=input("Enter hostname: ")
if h in dict:
    dict[h] = "127.0.0.1"
else:
    print("Hostname not found")
    dict[h] = "127.0.0.1"

print("Updated dictionary details:")
for var in dict:
    print("Hostname:", var, "IP:", dict[var])
    