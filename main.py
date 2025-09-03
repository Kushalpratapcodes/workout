# ------------------------
# Function: logworkout()
# ------------------------
def logworkout():
    # Ask for the date once (string, not int, so "2 September 2025" works)
    date = input("Enter Today's date: ")

    print("Enter the workout details (type DONE when finished):")

    # Collect all workout lines in a list
    lines = []
    while True:
        line = input()   # get one line at a time
        if line.upper() == "DONE":   # stop if user types DONE
            break
        lines.append(line)

    # Join all lines into a single block of text for the entry
    # Add two newlines at the end to separate entries in the file
    entry = f"{date}\n" + "\n".join(lines) + "\n\n"

    # Open the file in append mode → add entry without deleting old ones
    with open("/Users/kushalprataprajawat/Downloads/coding/workout-tracker/workoutlogs.txt", "a") as f:
        f.write(entry)

    print("Workout logged successfully!")


# ------------------------
# Function: viewworkout()
# ------------------------

def viewworkout():
    # Ask user which date to search
    datetofind = input("Please enter the date you want to find the entry of (e.g. 2 September 2025): ")

    # Read the whole file as one string
    with open("/Users/kushalprataprajawat/Downloads/coding/workout-tracker/workoutlogs.txt", "r") as f:
        content = f.read()

    # Remove extra newlines from edges, then split by blank lines between entries
    entries = content.strip().split("\n\n")

    found = False  # flag to check if entry is found
    for entry in entries:
        # Each entry starts with its date → check if it matches the date typed
        if entry.startswith(datetofind):
            print("\n=== Entry Found ===")
            print(entry)
            print("===================")
            found = True
            break  # ✅ stop after the first match (as you wanted)

    if not found:
        print(f"No entry found for {datetofind}")


# ------------------------
# Function: showmenu()
# ------------------------
def showmenu():
    while True:
        # Print the menu
        print("\nWhat Would You like to do?")
        print("1. Log a Workout")
        print("2. View a Workout by Date")
        print("3. Exit")

        # Take choice as a string (so user can just type "1")
        choice = input("Your choice: ")

        if choice == "1":
            logworkout()
        elif choice == "2":
            viewworkout()
        elif choice == "3":
            print("Thank you for logging in today. Hope to see you again")
            break   # exits the while loop → program ends
        else:
            print("Invalid choice, please try again.")


# ------------------------
# Run the program
# ------------------------
showmenu()