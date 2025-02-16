# Ressources : 0,299s, 10,11 Mio
# Temps d'exécution maximum d'un seul cas : 0,029s
# Score final : 100/100 (3.0/3 points) 
# Link : "https://dmoj.ca/problem/dmopc16c1p0"

W = int(input())
C = int(input())

w = W >= 1 and W <= 3
c = C >= 0 and C <= 100

if w and c and (W == 3 and C >= 95):
    M = "absolutely"
elif w and c and (W == 1 and C <= 50):
    M = "fairly"
else:
    M = "very"

satisfaction = f"C.C. is {M} satisfied with her pizza."
print(satisfaction)
