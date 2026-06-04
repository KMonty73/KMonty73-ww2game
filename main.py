from intel_system import show_intelligence

print("WWII COMMAND PLATFORM")
print("=====================")

turn = 1

while True:

    print("\nTURN", turn)
    print("-------------------")
    print("1. Intelligence Report")
    print("2. Launch Recon")
    print("3. Attack Smolensk")
    print("4. End Turn")
    print("5. Quit")

    choice = input("\nChoose: ")

    if choice == "1":

        show_intelligence()

    elif choice == "2":

        print("\nRecon aircraft launched.")
        print("Photos will return next turn.")

    elif choice == "3":

        print("\nGENERAL LEVEL")
        print("Attack ordered on Smolensk.")

        print("\nMAJOR LEVEL")
        print("Urban assault sectors assigned.")

        print("\nCAPTAIN LEVEL")
        print("Infantry and armor advancing.")

        print("\nINDIVIDUAL COMBAT")
        print("Battle begins inside city.")

    elif choice == "4":

        turn += 1
        print("\nNext turn begins.")

    elif choice == "5":

        print("\nExiting WWII COMMAND PLATFORM.")
        break

    else:

        print("\nInvalid choice.")
