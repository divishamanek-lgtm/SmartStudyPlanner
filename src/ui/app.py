from ui.input_page import get_user_input
from logic.scheduler import schedule_tasks

def run_app():
    tasks = get_user_input()
    plan = schedule_tasks(tasks, 5)

    print("\n Your Study Plan:")
    for p in plan:
        print(p)
