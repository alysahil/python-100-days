'''

this is multiple comment multiline comment takes multiple 
line .
python is eating the world

#data types
#1-number 
# integer, float,complex
#string
'sahil'
'finland'
'python'
'i love learning'
'i hope you are enjoying the first day of 100 daysofpython challenge'
#booleans
true # is the light on? if it is on , then the value is true
false #is the light on? if it is off, then the value is false 
#list 
[0,1,2,3,4,5] # all are the same data types - a list of numbers
['Banana','orange ','mango','avacado'] # all the same data types - a list of strings (fruits)
['finland','estonia','sweden','norway'] # all the same data types - a list of countries
['banana','10','false',9.81] # all the different data types in the list - string ,integer, boolean,float

#dictionary --- a python distionary object is an unordered collection of data in a key value pair format

{
    'first_name':'sahil',
    'last_name':'ali',
    'country':'india',
    'age':22,
    'is_married':False,
    'skills':['Js','react','node','python']
}

#tuple -- it is an ordered collection of different data types like list but tuples can not be modified once they are created . they are immutable
('Sahil','Rahman','nazif','maaz','gibrail') # Names 
('Earth','jupiter','neptune','mars','venus','saturn','uranus','mercury')# planets

#Sets --- a setr is collection of data types similar to list and tuple. unlike list and tuple ,set is not an ordered collection of items .like in mathematics , set in python stores only unique items.
{2,3,4,5,6,7,8,9}
{3.14, 9.81, 2.7} # order is not important in set
'''
# Day 1 - 100 daysofpython challenge

print(2+3)            #addition(+)
print(5-3)            # subtraction(-)
print(2*3)            # multiplication(*)
print(10/5)           # division(/)
print(3**2)           #exponential(**)
print(3 % 2 )        # modulus (%)
print(6//4)           #floor division

# checking data types 
print(type(10))                   #int
print(type(3.14))                #float 
print(type(1+3j))               #complex
print(type('sahil'))              #string
print(type([1,2,3]))               #list
print(type({'name':'sahil'}))     #dictionary
print(({9.8, 3.14, 2.7}))           #set 
print(type((9.8, 3.14, 2.7)))    #tuple


