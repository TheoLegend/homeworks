
print("Welcome to the Judging Quiz!")
print("Answer honestly... your fate will be decided.\n")

score = 0


answer = input("Do you prefer mornings or nights? (morning/night): ").strip().lower()
if answer == "morning":
    score += 1
elif answer == "night":
    score += 2


answer = input("What's your favorite snack? (chips/fruit/candy): ").strip().lower()
if answer == "fruit":
    score += 1
elif answer == "chips":
    score += 2
elif answer == "candy":
    score += 3


answer = input("Do you like animals? (yes/no): ").strip().lower()
if answer == "yes":
    score += 1
elif answer == "no":
    score += 3


print("\nCalculating your fate...\n")

if score <= 4:
    print("You are the calm, peaceful type. 🌸")
elif score <= 6:
    print("You’re a little adventurous — watch out, world! 🌍")
else:
    print("You’re pure chaos... but in a fun way. 🔥")
