# Free Day Off

A simple, cross-platform Python CLI tool that tells you the **next US federal holiday** that falls on a **Monday–Friday work week**, and how many days away it is.

---

## 📸 Features

✅ Lists only federal holidays that actually fall on weekdays  
✅ Always up-to-date for the current year  
✅ Supports macOS, Windows, and Linux  
✅ No internet needed, 100% offline  
✅ Pure Python 3 standard library

---

## ⚙️ Prerequisites

- Python 3 installed

Check with:

```bash
python3 --version
```

If you don't have it installed:

- **macOS:**  
  ```bash
  brew install python
  ```
- **Linux:**  
  ```bash
  sudo apt install python3
  ```
- **Windows:**  
  - Download from [python.org](https://www.python.org/downloads/)
  - Make sure to **Add to PATH** during install.

---

## 🚀 How to Use

Save the script `freedayoff.py` locally.  

Then run:

### ✅ macOS / Linux
```bash
python3 freedayoff.py
```

### ✅ Windows
```powershell
python freedayoff.py
```

---

## 💻 Example Output

```
===============================
Name: Independence Day
Date: 2025-07-04 (Friday)
Days Until: 2
===============================
```

---

## 🗂️ How It Works

- Calculates official US federal holidays for the current year.
- Applies the rules for holidays that move (e.g. Thanksgiving, Memorial Day).  
- Filters out any dates that fall on weekends.  
- Displays the **next** upcoming workday holiday from today.  

If no holidays remain this year, it automatically checks next year's first holiday.

---

## 🤝 Contributing

- Fork this repo
- Make improvements
- Submit a pull request

Suggestions welcome!

---

## 📄 License

MIT License. Free to use and share.