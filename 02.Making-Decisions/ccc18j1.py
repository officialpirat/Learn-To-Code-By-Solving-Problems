# Ressources : 0,404s, 10,14 Mio
# Temps d'exécution maximum d'un seul cas : 0,027s
# Score final : 15/15 (3.0/3 points) 
# Link : "https://dmoj.ca/problem/ccc18j1"

digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())

if ((digit1 == 8 or digit1 == 9) and (digit4 == 8 or digit4 == 9)) and (digit2 == digit3):
    print("ignore")
else:
    print("answer")
