#turning a string into something = casting 
#turning things into true and false = boolean 
#how do you decide what is true and what is false?

music = "classical"
shopping_list = []
num = 0
name = ""
my_name = "Allisha"

print(bool(music)) #can convert to either true or false, because it has an inherit value
print(bool(shopping_list))
print(bool(num)) #false because they do not have a value. 
print(bool(name))#true because they have a value 
print(bool(my_name))#useful to see if data exists 

user_name = input("Please enter your chosen user name")

if user_name:
    print(f"Welcome to your new account, {user_name}")
else:
    print("You did not enter anything")