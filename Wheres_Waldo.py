#Where's Waldo
import random
print("Where’s Waldo?")
print("Guess the secret location!")

#list of countries
countries = ["Belgium", "Bolivia", "Brazil", "China", "Colombia", "Costa Rica", "Denmark", "France", "Germany", "India", "Italy", "Japan",
             "Norway", "Russia", "Switzerland", "United States", "Zimbabwe"]


print("Countries to choose from: ", countries)
#Random number generator linked to countries through list
random_number = random.randint(0, 13)
secret_location = countries[random_number] 
#User guess, run until they guess correctly
guess = input("Where's Waldo: ")

while guess != secret_location:
    print(f'Sorry {guess} is wrong, try again.') 
    guess = input("Where's Waldo: ") 

if guess == secret_location:
    print(f'Correct! He was in {secret_location}')
