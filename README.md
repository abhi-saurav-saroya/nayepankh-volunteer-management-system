<h1 align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=ffffff&center=true&vCenter=true&width=750&lines=NayePankh+Volunteer+Management+System"
    alt="Volunteer Management System"
  />
</h1>

<p align="center"><i>Manage volunteers efficiently. Empower communities.</i></p>

---

Volunteer Management System is a **command-line volunteer management application built in Python**, designed to help organizations efficiently manage volunteer records through a clean, modular, and menu-driven interface powered by **SQLite**.

The project focuses on **Python fundamentals, object-oriented programming, modular software architecture, SQLite database integration, CRUD operations, input validation, data processing, reporting, CSV export, and practical CLI application development**, while using Python's standard library.

> Note: This project was developed as a submission for the Python Developer Internship Task at NayePankh Foundation, with a focus on clean architecture, modularity, database management, and practical CLI application development.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Category-Management_System-22c55e?style=for-the-badge" alt="Management System"/>
  <img src="https://img.shields.io/badge/Type-CLI_Application-f97316?style=for-the-badge" alt="CLI"/>
  <img src="https://img.shields.io/badge/Domain-Volunteer_Management-6366f1?style=for-the-badge" alt="Volunteer Management"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="MIT License"/>
</p>

## Features

1. ### Volunteer Management (CRUD)

   * Add new volunteers
   * View all volunteers
   * Update volunteer information
   * Delete volunteer records

2. ### Search & Filtering

   * Search volunteers by name, city, or skill
   * Filter volunteers by city
   * Filter volunteers by skill
   * Filter volunteers by availability

3. ### Reports

   * Total volunteer count
   * Available and unavailable volunteer statistics
   * Volunteers grouped by city
   * Volunteers grouped by skill

4. ### CSV Export

   * Export volunteer records to CSV
   * Excel-compatible output
   * Custom filename support

5. ### User Experience

   * Interactive menu-driven interface
   * Input validation
   * Clean tabular output
   * Modular project architecture

## Project Architecture

<p align="center">
  <img src="assets/dir-structure.png" alt="Project Structure" width="320">
</p>

## Application Workflow

```text
User
   ↓
CLI Menu
   ↓
Volunteer / Report / Export Services
   ↓
SQLite Database
   ↓
Formatted Output / CSV Export
```

## Tech Stack

<div align="center">

| Component        | Technology   |
| ---------------- | ------------ |
| Language         | Python 3     |
| Database         | SQLite3      |
| CSV Export       | csv          |
| Input Validation | re           |
| Version Control  | Git + GitHub |

</div>

## Build & Run Instructions

### Requirements

* Python 3.10 or higher
* Git (for cloning the repository)

### Clone the Repository

```bash
git clone https://github.com/abhi-saurav-saroya/nayepankh-volunteer-management-system.git
cd nayepankh-volunteer-management-system
```

### Run the Application

```bash
python main.py
```

or

```bash
python3 main.py
```

### Usage

1. Launch the application.
2. Select an option from the main menu.
3. Manage volunteer records using CRUD operations.
4. Search or filter volunteers.
5. Generate volunteer reports.
6. Export volunteer data to CSV whenever required.

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer"/>

<i>Built to learn, designed to organize, engineered one volunteer at a time. 🤝</i>

<i>Manage volunteers efficiently. Empower communities.</i>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

**© 2026 Open Source Project | Volunteer Management System | MIT License**

</div>
