import random
import time

teams = ["Aarya", "Avie", "Vihaan", "Papa", "Jai", "Manav S", "Manav P", "Parth", "Pranav", "Garb"]

random.shuffle(teams)

print("FANTASY ORDER")
#time.sleep(3)
for i, v in enumerate(teams):
    print("Pick " + str(i + 1) + ": " + v)
    #time.sleep(3)
