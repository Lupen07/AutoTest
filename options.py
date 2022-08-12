name = input('Please ente your name ? :')
age = input('Please ente your age ? :')

age = int(age)
if age >= 18:
    print("You can enter, because your age is 18 or more that 18")
else:
    print("You can't enter, because your age is less")

print("your name :", name, "your age :", str(age));
