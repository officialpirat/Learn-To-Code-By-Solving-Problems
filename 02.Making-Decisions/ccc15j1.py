# Ressources : 0,242s, 10,15 Mio
# Score final : 13/15 (2.6/3 points) 
# Link : "https://dmoj.ca/problem/ccc15j1"

month = int(input())
day = int(input())


if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):  
    month = month
    day = day    

before = month <= 2 and day < 18
special = month == 2 and day == 18


if month and day and special:
    print("Special")
elif month and day and before:
    print("Before")
else:
    print("After")
