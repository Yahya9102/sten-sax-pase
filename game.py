import random

CHOICES = ["sten", "sax", "påse"]

def get_computer_choice() -> str:
    return random.choice(CHOICES)



def get_result(player_choice: str, computer_choice: str) -> str:
    if player_choice == computer_choice:
        return "oavgjort"
    

    if player_choice == "sten" and computer_choice == "sax":
        return "vinst"
    if player_choice == "sax" and computer_choice == "påse":
        return "vinst"
    if player_choice == "påse" and computer_choice == "sten":
        return "vinst"
    
    return "förlust"