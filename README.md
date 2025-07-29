
# Energy Efficient Task Scheduler in Cloud ☁️⚡

This is a beginner-friendly Python project that simulates scheduling of cloud tasks using two algorithms:
1. **First Come First Serve (FCFS)**
2. **Min-Min Scheduling**

The project aims to demonstrate how smart task scheduling can help reduce **total power consumption** while ensuring deadlines are met.

---

## 🛠 Technologies Used
- Python 3
- Matplotlib (for graph visualization)
- JSON (for task input data)

---

## 📂 Files Included
- `scheduler.py` - Main code file implementing both scheduling algorithms.
- `tasks.json` - Sample input file with task details.

---

## 🔢 Sample Input (tasks.json)
```json
[
  {"id": 1, "length": 20, "deadline": 30},
  {"id": 2, "length": 10, "deadline": 25},
  {"id": 3, "length": 15, "deadline": 40},
  {"id": 4, "length": 30, "deadline": 60}
]
```

---

## 📊 Output
- For each task: Task ID, Start Time, End Time, Energy Used, Deadline Met
- Total energy consumed (in Watts)
- Energy usage visualization (bar graph)

---

## 🚀 How to Run
```bash
pip install matplotlib
python scheduler.py
```

---

## 📌 Purpose
> Reduce power consumption in cloud environments by smartly scheduling tasks.

---

## 👤 Made by
**Shobhit Shukla**
