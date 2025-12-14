# 🏏 ICC Cricket Rankings Scraper

## 📌 Project Description

This project is a **Selenium-based web scraper** that automatically collects **ICC Cricket Player Rankings** from the official ICC website.

The scraper extracts rankings for:

* **Roles**: Bowling, Batting, All‑Rounder
* **Genders**: Men's and Women's
* **Formats**: Test, ODI, T20I

The scraped data is saved in a **clean, hierarchical folder structure** and exported as **JSON files**, making it easy to use for analytics, dashboards, or further data processing.

---

## 🚀 Features

* 🌐 Dynamic scraping using **Selenium WebDriver**
* 🍪 Automatic cookie banner handling
* 🔄 Handles **Load More** pagination
* 📂 Organized folder structure by **Gender → Format → Role**
* 💾 JSON output (UTF‑8 safe)
* ⚠️ Skips unavailable combinations (e.g., Women's Test rankings)
* 🧱 Scalable loop-based architecture

---

## 📁 Folder Structure

```
icc_rankings/
│
├── mens/
│   ├── test/
│   │   ├── batting.json
│   │   ├── bowling.json
│   │   └── allrounder.json
│   │
│   ├── odi/
│   │   └── *.json
│   │
│   └── t20i/
│       └── *.json
│
└── womens/
    ├── odi/
    │   └── *.json
    └── t20i/
        └── *.json
```

---

## 📦 Output Data Format

Each JSON file contains a list of player objects:

```json
{
    "Position": 1,
    "Player": "Jasprit Bumrah",
    "Team": "India",
    "Rating": "883",
    "Career Best": "888 v Sri Lanka, 2022"
}
```

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Selenium**
* **Google Chrome & ChromeDriver**

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install selenium
```

Ensure **Google Chrome** and the matching **ChromeDriver** are installed and available in your system PATH.

---

### 2️⃣ Run the Scraper

```bash
python icc_rankings_scraper.py
```

The scraper will:

* Open ICC website
* Accept/Reject cookies automatically
* Visit each ranking page
* Load all players
* Save rankings into structured JSON files

---

## 🧠 Logic Highlights

* Uses `WebDriverWait` for stability
* Dynamically clicks **Load More** until all players load
* Skips invalid combinations:

  ```python
  if gender == "womens" and formats == "test":
      continue
  ```

---

## ⚠️ Notes

* Avoid running too frequently to prevent IP blocking
* Headless mode can be enabled for automation
* Website structure changes may require selector updates

---

## 🔮 Future Enhancements

* 📊 CSV / Pandas export
* 🧠 Retry & exception logging
* 🧪 PyTest test cases
* ⚡ Multithreading
* 🐳 Docker support

---

## 👨‍💻 Author

**Praveen Suresh**
Aspiring **Web Scraping Engineer** | Python | Selenium | Data Extraction

---

⭐ If you like this project, give it a star and feel free to extend it!
