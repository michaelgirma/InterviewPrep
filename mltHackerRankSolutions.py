#The Coder Friends: Completed
def winner(erica, bob):
    # Write your code here
    eScore = 0
    bScore = 0
    for eNum in erica:
        if eNum == "E":
            eScore += 1
        elif eNum == "M":
            eScore += 3
        elif eNum == "H":
            eScore += 5
      
    
    for bNum in bob:
        if bNum == "E":
            bScore += 1
        elif bNum == "M":
            bScore += 3
        elif bNum == "H":
            bScore += 5
  
    
    if eScore > bScore:
        winnerName = "Erica"
        return winnerName
    elif eScore < bScore:
        winnerName = "Bob"
        return winnerName
    else:
        winnerName = "Tie"
        return winnerName