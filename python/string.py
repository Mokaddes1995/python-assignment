a = "Hello World!"

#String Array

a = "Hello World!"

print(a[1])

#Use len Function

a = "Hello World!"

print(len(a)) #Length of a.

#Check String

a = "Hello World!"

print("World" in a) #Return True
print("World" not in a) #Return False

print("No" in a) #Return False
print("No" not in a) #Return True

#Use If for Check

if 'H' in a:
    print("Yes")
else:
    print("No")


if "K" in a:
    print("Yes, K in a.")
else:
    print("No, K not in a.")
    

if "e" not in a:
    print("No, e not in a.")
else:
    print("Yes, e in a.")
    

#Loop in String

for ltr in "Banana":
    print(ltr, end=",")

print()

#Slicing String

a = "This is a String"

print(len(a))

print(a)

print(a[2])

print(a[1:5])

print(a[:4])

#Negative Indexing

print(a[-1:])

print(a[-16:])

print(a[-10:-4])

print(len("s a St"))

print(a[len(a)-1])

#Reversed Word

print(a[::-1])

print(a[-5])

print(a[-9::-1])

print(a[-10:-16:-1])

print(a[-16:10:1])
print(a[5:1:-1])

#String Method


#কেস পরিবর্তন সম্পর্কিত মেথড

a = "Mokaddes Hossain"

#Upper Method

b = a.upper()
print(b)    #MOKADDES HOSSAIN

#Lower Method

b = a.lower()
print(b)    #mokaddes hossain

#Title Method

a = 'mokaddes hossain'

b = a.title()
print(b)    #Mokaddes Hossain

#Capitalize Method

b = a.capitalize()
print(b)    #Mokaddes hossain

#Swapcase Method

a = "MoKaDdEs HoSsAiN"

b = a.swapcase()
print(b)    #mOkAdDeS hOsSaIn

#Casefold Method

a = "This Is a Wonderful Day."

b = a.casefold() #All are Lowercase.
print(b) #this is a wonderful day.


# স্পেস ও স্ট্রিপিং সম্পর্কিত মেথড

#Strip Method

a = ' Hello World! '

print(a)

b = a.strip() #Remove Whitespace
print(b)    #Hello World!

b = a.lstrip() #Remove Left Whitespace
print(b) #Hello World! .

b = a.rstrip() #Remove Right Whitespace
print(b) # Hello World!

#Replace Method

a = 'Hello World'

b = a.replace("He", "Ja")
print(b) #Jallo World

#খোঁজা ও ইনডেক্স সম্পর্কিত মেথড

#Find Method

a = "Hello World"

b = a.find("l")
print(b) #Return 2

b = a.find("l", 5, 10) #find 5 to 10
print(b) #9 no character and return one index which first if not find return -1 value

b = a.find("q")
print(b) #Return -1

#Index Method

a = "Hello World"

b = a.index("l")
print(b) #Return 2

b = a.index("o",0,10) #Range
print(b) #Return 4 

# b = a.index("q")
# print(b) #Return Error

#Rfind Method

a = "Hello World"

b = a.rfind("l")
print(b) #Return 9

#Count Method

a = "This is a String"

b = a.count('T')
print(b) #Return 1

b = a.count('i')
print(b) #Return 3

b = a.count("i", 10, 16) #Range
print(b) #Return 1

#Startswith Method

a = 'Mokaddes Hossain'

b = a.startswith('Mo')
print(b) #Return True

b = a.startswith('Ho')
print(b) #Return False

#Endwith Method

a = 'Mokaddes Hossain'

b = a.endswith('es')
print(b) #Return False

b = a.endswith("in")
print(b) #Return True

#স্প্লিট ও জয়েন সম্পর্কিত মেথড


#Split Method

a = "Hello World"

b = a.split()
print(b) #Return a List with 2 Elements

a = 'Hello World, Hello World, Mango'

b = a.split(',')
print(b) #Return a List with 3 Element separate by ','.

b = a.split(' ')
print(b)

#Task 1 for Split 

#একটি ইমেইল ঠিকানা দেওয়া আছে। split() মেথড ব্যবহার করে ইউজারনেম এবং ডোমেইন নাম আলাদা করুন।
    
email = "john.doe@gmail.com"

# আউটপুট হবে:
# Username: john.doe
# Domain: gmail.com

a = email.split('@')

username = a[0]
domain = a[1]

print(f'Username: {username}')
print(f'Domain: {domain}')

#টাস্ক ২: একটি বাক্য থেকে শব্দগুলোর তালিকা তৈরি করা এবং প্রতিটি শব্দের দৈর্ঘ্য বের করা

sentence = "Python is a powerful programming language"

s_sentence = sentence.split(' ')

print(s_sentence)

for i in s_sentence:
    lenth = len(i)
    print(f"{i}:{lenth}")
    

#Join Method

a = "MOKADDES"

b = [char for char in a]
print(b)

c = ",".join(b)
print(c)

c = "".join(b)
print(c)