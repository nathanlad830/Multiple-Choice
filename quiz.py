score = 0
print("You find a Â£20 note on the ground do you...")
print("A - Spend it on sweets?")
print("B - Give it to a homeless man?")
print("C - Keep it and say nothing?")
print("Do you choose A, B or C")
choice = input("\n")

if choice == "a" or choice == "A":
    print("You picked A!\n")
    print("You need to stop eating sweets! Greedy\n")
elif choice == "b" or choice == "B":
        print("You picked B!\n")
        score =+ 1
elif choice == "c" or choice == "C":
        print("Oh no, thats awful!\n")
else:
    print("Make up your mind!")
print("Score = ",score)



