#Codelike 7.2 Where's Waldo
import random
print("Where’s Waldo?")
print("Guess the secret location!")

#list of countries
countries = ["Belgium", "Bolivia", "Brazil", "China", "Colombia", "Costa Rica", "Denmark", "France", "Germany", "India", "Italy", "Japan",
             "Norway", "Russia", "Switzerland", "United States", "Zimbabwe"]


print("Countries to choose from: ", countries)

random_number = random.randint(0, 13)
secret_location = countries[random_number] 

guess = input("Where's Waldo: ")

while guess != secret_location:
    print(f'Sorry {guess} is wrong, try again.') 
    guess = input("Where's Waldo: ") 

if guess == secret_location:
    print(f'Correct! He was in {secret_location}')
