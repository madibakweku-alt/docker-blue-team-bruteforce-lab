# 🔵 Docker Blue Team Brute-Force Detection Lab

A lightweight, beginner-friendly blue-team cybersecurity lab built with Docker. This project simulates a **simple brute-force attack** using Hydra and teaches you how to detect it by analysing authentication logs. Perfect for cybersecurity students and blue-team beginners who want a hands-on project for their GitHub portfolio.

---

## 📌 Overview

This project contains two Docker containers:

1. **Victim container** – A small Flask web application with a basic login form and logging enabled.
2. **Attacker container** – Runs Hydra to brute-force the Flask login endpoint.

The purpose of this lab is to help you:

* Understand brute-force attack patterns.
* Generate realistic logs.
* Practise log analysis.
* Recognise abnormal authentication behaviour.
* Strengthen your defensive investigation skills.

---

## 🚀 Features

* Fully containerised (no need to install Python or Hydra locally).
* Realistic brute-force output.
* Authentication logs stored inside the victim container.
* Easy to extend into SIEM/ELK in future projects.
* Designed for cybersecurity blue-team learning.

---

## 🧱 Project Structure

```
docker-blue-team-bruteforce-lab/
│
├── attacker/
│   └── attack.sh
│
├── victim/
│   ├── Dockerfile
│   └── app.py
│
├── docker-compose.yml
└── README.md
```

---

## 🛠 Requirements

* Docker
* Docker Compose

Run this project on macOS, Windows, or Linux.

---

## 🐳 Setup & Run Instructions

### 1. Clone the Repository

```
git clone https://github.com/YOURUSERNAME/docker-blue-team-bruteforce-lab.git
cd docker-blue-team-bruteforce-lab
```

### 2. Start the Lab

```
docker compose up --build
```

### 3. Watch the Attack Happen

You will see:

* Flask server running on `http://localhost:5000/login`
* Hydra attacking with multiple password attempts

---

## 📄 Victim Authentication Logs

Inside the `victim` container, logs are stored at:

```
auth.log
```

Each failed attempt is recorded as:

```
FAILED LOGIN: user=admin, password=guess123
```

Each success appears as:

```
SUCCESSFUL LOGIN: user=admin
```

---

## 🧠 Blue Team Analysis Guide

After the attack finishes, your job is to analyse the logs.

### 1. Identify Indicators of Brute-Force Attack

Look for patterns like:

* Many failed logins in a short time
* Same username attempted repeatedly
* Sequential or dictionary-style password guesses
* Attempts coming from one source (the attacker container)

### 2. Key Questions to Ask

* How many failed logins occurred?
* How many attempts per minute?
* Was there a successful attempt after many failures?
* Do the timestamps show constant, repetitive activity?

These questions mimic real SOC investigation thinking.

---

## 🛡 Defensive Improvements (Future Enhancements)

This project is intentionally simple, but you can extend it:

### 🔒 Authentication Hardening

* Add lockout after X failed attempts
* Add rate limiting
* Add CAPTCHA
* Use hashed passwords instead of plain strings

### 📊 Log Analysis Improvements

* Connect to Elasticsearch + Kibana
* Add a Python log parser
* Add alerts for suspicious login patterns

### 🧪 More Realistic Attack Paths

* SSH brute-force
* FTP brute-force
* Wordlist expansions
* Multiple attacker containers

---

## 🧪 Example: Manual Log Review

Example suspicious pattern:

```
2025-01-15 10:03:22 - FAILED LOGIN: user=admin, password=pass1
2025-01-15 10:03:23 - FAILED LOGIN: user=admin, password=pass2
2025-01-15 10:03:23 - FAILED LOGIN: user=admin, password=pass3
2025-01-15 10:03:24 - FAILED LOGIN: user=admin, password=pass4
```

This shows:

* High frequency (1 attempt per second)
* Sequential guessing pattern
* Same user targeted repeatedly

Conclusion: **classic brute-force behaviour**.

---

## 💡 Future Lab Ideas

This project can grow into a full blue-team portfolio series:

* 🔐 Password spraying lab
* 🕵️ SIEM detection lab (Elastic or Wazuh)
* 📦 Container escape monitoring
* 🌐 Network traffic monitoring with Suricata
* 📊 SOC alert tuning walkthrough

If you want, you can ask for Version 2 and I can expand this lab for you.

---

## 📝 License

This project uses the **MIT License**, allowing anyone to use or modify it freely while protecting you from liability.

---

## 👤 Author

Created by **Madiba Klutsey**.
Cybersecurity student specialising in blue-team defensive projects.

---

If you want visual diagrams, GIFs of the terminal, or a professional banner for the top of this README, I can generate that too.
