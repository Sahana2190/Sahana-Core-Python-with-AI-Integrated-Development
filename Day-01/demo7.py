'''
Write a python program:
|-> read a port number from <STDIN>

|-> test - input port number range is 5001-5999
           ------------------------------------
		|-> initialize app name is Flask

	   |->initialize app name is Django

|-> Display - App name and Running port number
'''

n = int(input("Enter a number: "))
if n>= 5001 and n<=5999:
    app_name = "Flask"
else:
    app_name = "Django"
print(f'App Name: {app_name} and running port number: {n}')