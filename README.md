# 📚 Study Planner (CLI App)

A simple and efficient **Command Line Interface (CLI) Study Planner** built using Python.
This tool helps students manage their study tasks, track deadlines, and stay organized.

---

## 🚀 Features

* ✅ Add new study tasks
* 📖 View all tasks in a structured format
* ✔️ Mark tasks as completed
* ❌ Delete tasks
* 💾 Persistent storage using JSON file
* 🧠 Simple and beginner-friendly design

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Storage:** JSON (acts as a lightweight database)
* **Interface:** CLI (Command Line Interface)

---

## 📂 Project Structure

```
Study-Planner/
│── main.py        # Main application logic
│── data.json      # Stores all tasks
│── README.md      # Project documentation
```

---

## ⚙️ How It Works

* Tasks are stored in a `data.json` file as a list of dictionaries.
* Each task contains:
  * Task name
  * Subject
  * Deadline
  * Status (Pending / Completed)

---

## 🧪 Installation & Setup

1. Clone the repository:

```
git clone https://github.com/coderUttaran/Study-Planner.git
```

2. Navigate to the folder:

```
cd Study-Planner
```

3. Run the program:

```
python main.py
```

---

## 🖥️ Usage

After running the program, you’ll see:

```
Student Study Planner
1. Add task
2. View tasks
3. Mark Complete
4. Delete task
5. Exit
```

### Example Flow

* Add a task → Enter details
* View tasks → See all tasks
* Mark complete → Update status
* Delete task → Remove unwanted tasks

---

## 📸 Example Task Format

```json
{
    "task": "Complete Trigonometry",
    "subject": "Math",
    "deadline": "2026-05-15",
    "status": "Pending"
}
```

---

## ⚠️ Error Handling

The app handles:

* Invalid inputs (non-numeric choices)
* Out-of-range task numbers
* Empty task list cases

---

## 🔮 Future Improvements

* 🔍 Search tasks by subject or deadline
* 📅 Auto date validation
* 🖥️ GUI version using Tkinter / PyQt
* 🌐 Web version (Flask / Django)
* 📊 Task priority system

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and free to use.

---

## 🙌 Author

**Uttaran**

* 💻 Beginner Python Developer
* 🎯 Focused on building real-life CLI tools

---

## ⭐ Support

If you like this project:

* Give it a ⭐ on GitHub
* Share with your friends

---

> “Small tools like this build big discipline.” 🚀
>
