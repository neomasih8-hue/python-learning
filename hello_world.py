My 2nd course of the subject is python which im going to learn and showcase my progress in here
1) drawing shapes
i have drawn a triangle
print("    / | ")
print("   /  |")
print("  /   |")
print(" /____|")
output:
    / | 
   /  |
  /   |
 /____|
you can certainly close the gap if you want to make it more better. 
you can draw any shape you want.
----------------------------------------------------------------------------------------------------------------------------------------------
2) Variables and data types
.) variables (contain to store data values)
im going to write a story a short one ofc
print("Hey arren, how are you?")
print("Oh...its you again.")
print("you're right..its always gonna be me again.")
print("its been 2years yet..you couldnt disappear..")
now if i wanted to change the name "arren" into "arron" i could do it manually for short story but if its long paragraph
you gotta make variable names
character_name = "arron"
memorial_years = "7years"


print("Hey "+ character_name + " how are you?" )
print("Oh...its you again.")
print("you're right..its always gonna be me again.")
print("its been "+ memorial_years + " yet..you couldnt disappear..")
Output:
Hey arron how are you?
Oh...its you again.
you're right..its always gonna be me again.
its been 7years yet..you couldnt disappear..
Note# make sure to use space and do not copy and paste what u learn from yt use ur own brain u can put the variable name u had created anywhere just make sure its right and sensable
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  New story---------------
character_name = "erebus"
character_age = "19"
print("there once was a man name "+character_name+",")
print("He was "+character_age+" years old")

character_name = "Elaria"
character_age = "20"
print("there once was a woman name "+character_name+"")
print("She was "+character_age+" years old")
working with stringes-----------------------------------------------------------------------------------------------------------------------------------------------------------------
character_name = "erebus"
character_age = 19.91
is_male = True
print("there once was a man name "+character_name+",")
print("He was "+str(character_age)+" years old")

character_name = "Elaria"
character_age = 20.02
is_female = True
print("there once was a woman name "+character_name+"")
print("She was "+str(character_age)+" years old")

Chara = "Arren"
print(Chara + " is cool")
output:
Arren is cool
This is called Concatenation where we add another string to one string
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To modify our strings we use function
1) Lower/upper case
Chara = "Arren"
print(Chara.lower())/print(Chara.upper())
output: 
arren, ARREN
.) to check whether it is true or false and also to modify along checking if its true or false
Chara = "Arren"
print(Chara.upper().isupper())/ .lower().islower())
Output: ARREN/arren
True/False
Note# we cannot do isupper or checking if its true or not first since it let just say i gave you 10 pencil and i told you i gave you 10 pencil so u wouldnt check first if i gave u 10 pencil again since its already in ur hand.
.) Len() a function which tell how many letters present in a word 
Chara = "Arren"
print(len(Chara))
Output: 5
.) To figure out a speific character in a string we use
"[]"
Chara = "Arren"
print(Chara[0])
Output: A 
Note# the counting starts with 0 bez computer is lazy
text{Memory Address of Letter} = text{Starting Address} + text{Index} 
1 string of index starts with 0
Now the opposite of it called index function basically locate the specific character inside our string
Chara = "Arren"
print(Chara.index("e")) and if its "A"
Output:
3, 0
To replace an existing character to something you want inside the string we use .replace("name of existing character", "to new character"))
Elaria = "Arren"
print(Elaria.replace("Arren", "erebus"))
Output = erebus
----------------------------------------------------------------------------------------------------------------------------------------------
working with numbers
print(1) or 
print(0.1) or 
print (-1.2) or print(-1)
we can also do basic arthmetics
print(any number + - / * any number)
print(1+2*3)
output = 9
But if we want to add first then multiply we have to seperate them using paranthesis
print((1+2)*3)
output = 12
modulus operator
print (10 % 3) 
output = 1
to add stringes in variables
num = 7
print("my fav number is " + str(num))
output: 
my fav number is 7
Abs aka absolute value of any number
by using this paranthesis
num = -71.1
print(abs(num))
output = 71.1
Now there are many maths function some needs a specific python math to get the access of those function
.)Normal math function
1) POW
basically 3^2 
print(pow(3, 2)) (the power of the number you wanted to do, the amount of number dividing itself)
output: 
3
2) MAX
give max number if print(3, 2) it would give bigger number
output:
3
3) MIN opposite of it if print (3, 2) it would give smaller number
output:
2
4)Round
basically rounding off
print(round(3.2)) or print(round(3.7))
output:
3, 4
Now for the python math which we can get access to specific math functions
from math import *
1) floor: it chopped or remove decimal
print(floor(3.1))
output:
3
2) ciel: basically roundoff
print(ciel(3.1))
output:
3
3)sqrt: square root of a number
print(sqrt(2))
output: 
4
-----------------------------------------------------------------------------------------------------------------------------------------------
Getting input from users
basically an intro before the gameplay 
for example ur math teacher asked u whats 2+5 is 
and you being a brilliant prodigy says its 7
and congrats this is it.
variable name = input("any sentence:")
print("yo wsp" + variable name + "bruh")
output:
any sentence: heyy wspp
yo wsp bruh
-------------------------------------------------------------------------------------------------------------------------------------------------
