def get_user_input():
    tasks = []
    n = int(input("Enter number of subjects: "))

    for _ in range(n):
        subject = input("Subject: ")
        deadline = int(input("Deadline (days): "))
        difficulty = int(input("Difficulty (1-5): "))
        time = int(input("Study hours required: "))

        tasks.append({
            'subject': subject,
            'deadline': deadline,
            'difficulty': difficulty,
            'time': time
        })

    return tasks
