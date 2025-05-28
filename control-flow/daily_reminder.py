task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_msg = "is a high priority task"
    case "medium":
        priority_msg = "is a medium priority task"
    case "low":
        priority_msg = "is a low priority task"
    case _:
        priority_msg = "has an unknown priority"

if time_bound == "yes":
    print(f"Reminder: '{task}' {priority_msg} that requires immediate attention today!")
else:
    print(f"Note: '{task}' {priority_msg}. Consider completing it when you have free time.")

