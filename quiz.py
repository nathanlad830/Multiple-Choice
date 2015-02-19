print("You find a £20 note on the ground do you...")
print("A - Spend it on sweets?")
print("B - Give it to a homeless man?")
print("C - Keep it and say nothing?")
print("Do you choose A, B or C")
choice = raw_input("\n")

if choice == "a":
    print("You picked A!\n")
    print("You need to stop eating sweets! Greedy\n")
elif choice == "b":
        print("You picked B\n!")
elif choice == "c":
        print("You piced C!\n")
else:
    print("ERROR\n")
    print("Use Lower Case Only!\n")
    print("a, b and c are only allowed!\n")
