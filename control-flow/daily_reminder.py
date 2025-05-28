task= input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")


if (time_bound == "yes"):
    time_bound = "requires immediate attention today"
else: 
    time_bound = "Consider completing it when you have free time"
match priority:
    case "high": 
        priority = "is a high priority task "
    case "medium": 
        priority = "is a meduim priority task"
    case "low": 
        priority = "is a low priority task"
print(f"{task}{priority}{time_bound}")
