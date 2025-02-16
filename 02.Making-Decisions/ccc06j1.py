# Ressources : 0,136s, 10,12 Mio
# Temps d'exécution maximum d'un seul cas : 0,027s
# Score final : 50/50 (3.0/3 points) 
# Link : "https://dmoj.ca/problem/ccc06j1"

burger_menu = [461, 431, 420, 0]
side_menu = [100, 57, 70, 0]
drink_menu = [130, 160, 118, 0]
dessert_menu = [167, 266, 75, 0]

choice_burger = int(input())
choice_side = int(input())
choice_drink = int(input())
choice_dessert = int(input())

if (choice_burger >= 1 and choice_burger <= 4) and (choice_side >= 1 and choice_side <= 4) and (choice_drink >= 1 and choice_drink <= 4) and (choice_dessert >= 1 and choice_dessert <= 4):
    total_calories = burger_menu[choice_burger - 1] + side_menu[choice_side - 1] + drink_menu[choice_drink - 1] + dessert_menu[choice_dessert - 1]
    print(f"Your total Calorie count is {total_calories}.")
else:
    print("Wrong input!")
