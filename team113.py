#Liam Reed
import random
strategy_name = "secret strat l"
def move(my_history, their_history):
    if len(my_history) <= 2:
        pick = random.choice(["r", "p", "s"])
    else:
        if their_history[-1] == "r":
            if their_history[-2] == "s" and their_history[-3] == "r":
                pick = "r"
            elif my_history[-1] == "p":
                pick = "r"
            elif my_history[-1] == "s":
                pick = "p"
            elif my_history[-1] == "r":
                if their_history[-2] == "r":
                    pick = "p"
                else: pick = "s"
            else:
                pick = "r"
        elif their_history[-1] == "p":
            if their_history[-2] == "s":
                pick = "r"
            elif my_history[-1] == "r":
                pick = "s"
            elif my_history[-1] == "s":                
                pick = "p"
            elif my_history[-1] == "p":                
                pick = "r"                
            else:
                pick = "p"        
        elif their_history[-1] == "s":
            if their_history[-2] == "p":
                pick = "r"
            elif my_history[-1] == "p":
                pick = "s"
            elif my_history[-1] == "s":
                pick = "p"
            elif my_history[-1] == "r":            
                pick = "s"
            else:
                pick = "s"
    return pick