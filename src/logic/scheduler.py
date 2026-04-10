from logic.priority import calculate_priority

def schedule_tasks(tasks, hours_per_day):
    for task in tasks:
        task['priority'] = calculate_priority(task['deadline'], task['difficulty'])

    tasks.sort(key=lambda x: x['priority'], reverse=True)

    schedule = []
    for task in tasks:
        schedule.append(f"Study {task['subject']} for {task['time']} hrs")

    return schedule
