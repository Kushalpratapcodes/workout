# 1. Function to log a workout (append to workouts.csv)

# 2. Function to view workout history (read from workouts.csv)

# 3. Simple menu loop (ask user: log or view)


def logworkout():
    date = (input("Enter Today's date: "))
    print("Enter the text and hit 'Done' when you are done typing")
    lines = []
    while True:
        line = input()
        if line.upper() == "DONE":
            break
        lines.append(line)
    entry = f"{date}\n" + "\n".join(lines) + "\n\n"
    
    with open("/Users/kushalprataprajawat/Downloads/coding/workout-tracker/workoutlogs.txt", "a") as f:
            f.write(entry)

def viewworkout():
    datetofind = input("Please enter the date you want to find the entry of (For e.g.. 2 September 25): ")    
    with open("/Users/kushalprataprajawat/Downloads/coding/workout-tracker/workoutlogs.txt", "r") as f:
        content = f.read()
    entries = content.strip().split("\n\n")
    for entry in entries:
        if entry.startswith(datetofind):
            print("Entry Starts \n")
            print(entry)
            print("Entry Found")

def showmenu():
    while True:
        print("What Would You like to do?")   
        print("1. Log a Workout ")   
        print("2. View a Workout ")   
        print("3. Exit ")   
        choice = int(input("What Would you like to do: "))

        if choice == 1:
            logworkout()
        elif choice == 2:
            viewworkout()
        elif choice == 3:
            print("Thank you for logging in today. Hope to see you again")
            break


showmenu()