'''
Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
Here are some example of valid variable names:
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2


'''
'''
# variables in python 
first_name = 'sahil'
last_name = 'ali'
country = 'india'
city = 'greater noida '
age= '22'
is_married = False
skills =['html','css','js','react','python']
person_info={
    'first_name':'sahil',
    'lastname':'ali',
    'country':'india',
    'city':'greater noida'
}

#examples
print('hello, world')
print('hello',',',  'world','!')
print(len('hello, world!'))

#examples

print('First name:', first_name)
print('First name length:', len(first_name))
print('last name:', last_name)
print('country:', country)
print('city:', city)
print('age:',age)
print('married:', is_married)
print('skills:', skills)
print('person information:', person_info)
# examples

first_name, last_name, country, age, is_married = 'sahil', 'ali','greater noida', 22,False
print('First anme:', first_name)
print('last name:', last_name)
print('country:',country)
print('age:', age)
print('married:', is_married)

#examples
first_name= input('what is your name: ')
age = input('how old are you?')
print(first_name)
print(age)


# type casting 
#int to float 
num_int =10
print('num_int', num_int)         #10
num_float = float(num_int)
print('num_float:', num_float)   #10
 
 #float to int
gravity = 9.81
print(int(gravity))
 
 #int to str
num_int= 10
print(num_int)
num_str = str(num_int)
print(num_str)              

#str to int or float
num_str ='10.6'
print ('num_int', int(num_str))
print('num_float', float(num_str))

#str to list
first_name ='sahil'
print(first_name)
first_name_to_list =list(first_name)
print(first_name_to_list)

'''

#day-2 of 30-days-of-python
'''
first_name ='sahil'
last_name='ali'
full_name=first_name+last_name
country= 'india'
city='greater noida '
age=22
year=2024
is_married=False
is_true=True
is_light_on= False
my_name,ur_name,my_coll,ur_coll='ali','aly','gniot','glb'
print(first_name)
'''
num_one=5
num_two=4
total= num_one +num_two 
diff=num_one-num_two
product=num_two*num_one
div=num_one/num_two
rem=num_two%num_one
exp=num_two**num_one
fldiv=num_one//num_two
username=input('enter your username:')
password=input('enter your password :')
if username=="sahil" and password=='sahil786':
           print('valid response')
else :
        print('invalid response')