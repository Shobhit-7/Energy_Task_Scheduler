import json
import matplotlib.pyplot as plt

# Power model (Watts per second)
POWER_PER_SEC = 2

# FCFS Scheduler
def fcfs_schedule(tasks):
    current_time = 0
    total_energy = 0
    schedule = []

    for task in tasks:
        start = current_time
        end = start + task['length']
        energy_used = task['length'] * POWER_PER_SEC

        schedule.append({
            'task_id': task['id'],
            'start_time': start,
            'end_time': end,
            'energy': energy_used,
            'deadline': task['deadline'],
            'met_deadline': end <= task['deadline']
        })

        current_time = end
        total_energy += energy_used

    return schedule, total_energy

# Min-Min Scheduler
def min_min_schedule(tasks):
    remaining_tasks = tasks.copy()
    schedule = []
    current_time = 0
    total_energy = 0

    while remaining_tasks:
        next_task = min(remaining_tasks, key=lambda x: x['length'])

        start = current_time
        end = start + next_task['length']
        energy_used = next_task['length'] * POWER_PER_SEC

        schedule.append({
            'task_id': next_task['id'],
            'start_time': start,
            'end_time': end,
            'energy': energy_used,
            'deadline': next_task['deadline'],
            'met_deadline': end <= next_task['deadline']
        })

        current_time = end
        total_energy += energy_used
        remaining_tasks.remove(next_task)

    return schedule, total_energy

# AI-Based Scheduler
def ai_scheduler(tasks, alpha=0.7, beta=0.3):
    remaining_tasks = tasks.copy()
    schedule = []
    current_time = 0
    total_energy = 0

    while remaining_tasks:
        for task in remaining_tasks:
            deadline_val = task['deadline'] if task['deadline'] > 0 else 1
            task['priority'] = alpha * (1 / deadline_val) + beta * task['length']

        next_task = min(remaining_tasks, key=lambda x: x['priority'])

        start = current_time
        end = start + next_task['length']
        energy_used = next_task['length'] * POWER_PER_SEC

        schedule.append({
            'task_id': next_task['id'],
            'start_time': start,
            'end_time': end,
            'energy': energy_used,
            'deadline': next_task['deadline'],
            'met_deadline': end <= next_task['deadline']
        })

        current_time = end
        total_energy += energy_used
        remaining_tasks.remove(next_task)

    return schedule, total_energy

# Visualize energy usage
def show_energy_graph(schedule, title):
    task_ids = [str(task['task_id']) for task in schedule]
    energies = [task['energy'] for task in schedule]

    plt.bar(task_ids, energies, color='skyblue')
    plt.xlabel("Task ID")
    plt.ylabel("Energy Used (Watts)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Sample task list
tasks = [
    {"id": 1, "length": 20, "deadline": 30},
    {"id": 2, "length": 10, "deadline": 25},
    {"id": 3, "length": 15, "deadline": 40},
    {"id": 4, "length": 30, "deadline": 60}
]

if __name__ == "__main__":
    print("===== FCFS Scheduling =====")
    schedule_fcfs, total_energy_fcfs = fcfs_schedule(tasks)
    for task in schedule_fcfs:
        print(f"Task {task['task_id']} | Start: {task['start_time']} | End: {task['end_time']} | Energy: {task['energy']}W | Deadline Met: {task['met_deadline']}")
    print(f"Total Energy (FCFS): {total_energy_fcfs} Watts\n")
    show_energy_graph(schedule_fcfs, "Energy Usage - FCFS Scheduling")

    print("===== Min-Min Scheduling =====")
    schedule_minmin, total_energy_minmin = min_min_schedule(tasks)
    for task in schedule_minmin:
        print(f"Task {task['task_id']} | Start: {task['start_time']} | End: {task['end_time']} | Energy: {task['energy']}W | Deadline Met: {task['met_deadline']}")
    print(f"Total Energy (Min-Min): {total_energy_minmin} Watts\n")
    show_energy_graph(schedule_minmin, "Energy Usage - Min-Min Scheduling")

    print("===== AI-Based Scheduling =====")
    schedule_ai, total_energy_ai = ai_scheduler(tasks)
    for task in schedule_ai:
        print(f"Task {task['task_id']} | Start: {task['start_time']} | End: {task['end_time']} | Energy: {task['energy']}W | Deadline Met: {task['met_deadline']}")
    print(f"Total Energy (AI-Based): {total_energy_ai} Watts\n")
    show_energy_graph(schedule_ai, "Energy Usage - AI-Based Scheduling")
