# Ressources : 0,219s, 9,98 Mio
# Temps d'exécution maximum d'un seul cas : 0,029s
# Score final : 15/15 (3.0/3 points) 
# Link : "https://dmoj.ca/problem/ccc15j2"

message = input()

happy = ":-)"
sad = ":-("

if len(message) >= 1 and len(message) <= 255:
    if not message.count(happy) and not message.count(sad):
        print("none")
    elif message.count(happy) == message.count(sad):
        print("unsure")
    elif message.count(happy) > message.count(sad):
        print("happy")
    elif message.count(happy) < message.count(sad):
        print("sad")
