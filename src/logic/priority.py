def calculate_priority(deadline, difficulty):
    # Lower deadline → higher priority
    return (1 / deadline) * difficulty
