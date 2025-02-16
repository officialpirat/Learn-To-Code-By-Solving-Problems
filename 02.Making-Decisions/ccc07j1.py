# Ressources : 0,135s, 10,16 Mio
# Temps d'exécution maximum d'un seul cas : 0,027s
# Score final : 50/50 (3.0/3 points) 
# Link : "https://dmoj.ca/problem/ccc07j1"

bowl_one = int(input())
bowl_two = int(input())
bowl_three = int(input())

if 0 < bowl_one and bowl_two and bowl_three < 100:
    if (bowl_two < bowl_one < bowl_three) or (bowl_three < bowl_one < bowl_two):
        mama_bears_bowl = bowl_one
    elif (bowl_one < bowl_two < bowl_three) or (bowl_three < bowl_two < bowl_one):
        mama_bears_bowl = bowl_two
    else:
        mama_bears_bowl = bowl_three
        
print(mama_bears_bowl)
