---

# 🔐 Python Penetration Testing Toolkit

A modular, beginner-friendly penetration testing toolkit built in Python — designed to simulate real-world attack surfaces and automate basic security assessments. This project was developed as part of a cybersecurity-focused internship, with modularity, clarity, and usability in mind.

---

## 📁 Project Overview

This toolkit is structured around **four independent modules**, each handling a different category of security tooling:

| Task | Module                              | Description                                                                                                                                            |
| ---- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | File Integrity Checker              | Scans a directory, hashes all files, and detects modifications, deletions, or additions over time.                                                     |
| 2    | Web Vulnerability Scanner           | Scans websites for **basic SQL Injection** and **Cross-Site Scripting (XSS)** vulnerabilities using form payload fuzzing.                              |
| 3    | Python Pentesting Toolkit (Modular) | Combines several sub-tools like a port scanner, login brute forcer, directory scanner, hash cracker, and vulnerability scanner into a menu-driven CLI. |
| 4    | AES-256 File Encryption Tool        | Encrypts or decrypts files using AES-CBC mode with PBKDF2-derived keys and secure padding.                                                             |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/euphoric-habromaniac/File-Integrity-Checker
cd File-Integrity-Checker
```

### 2. Launch the Main Menu

```bash
python main.py
```

You’ll be presented with options to:

* ✅ **Install dependencies**
* 🧪 **Run individual tasks**
* 🔙 **Navigate back and forth easily**

---

## 📦 Dependencies

This project requires Python ≥3.10 and the following libraries:

* `requests`
* `beautifulsoup4`
* `tqdm`
* `cryptography`

All of these are automatically installed when you choose the **Setup Dependencies** option from the main menu.

---

## 🧰 Individual Task Details

### 🔍 Task 1: File Integrity Checker

* Recursively hashes all files in a specified directory.
* Compares against previous records stored in `hashes.json`.
* Detects:

  * 🔄 Modified files
  * ➕ New files
  * ❌ Deleted files

---

### 🛡️ Task 2: Web Vulnerability Scanner

* Extracts HTML forms from a URL.
* Injects payloads for:

  * **SQL Injection** (e.g., `' OR '1'='1`)
  * **XSS** (e.g., `<script>alert(1)</script>`)
* Flags potentially vulnerable forms based on response content.

---

### 🧰 Task 3: Python Penetration Testing Toolkit

Includes 5 independent sub-tools:

| Sub-Tool          | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| Port Scanner      | Scans top 1024 TCP ports for open services.                      |
| Brute Forcer      | Attempts to login using username-password pairs on a login form. |
| Web Vuln Scanner  | Same as Task 2, integrated here.                                 |
| Directory Scanner | Tries common hidden directory paths (from a wordlist).           |
| Hash Cracker      | Cracks MD5 or SHA1 hashes using dictionary attack.               |

All tools are menu-driven and isolated within the `modules/` directory.

---

### 🔐 Task 4: AES Encryption Tool

* Encrypts or decrypts any file using:

  * AES-256 in **CBC mode**
  * PBKDF2-based password derivation
* Prompts user for password and confirms before encrypting
* Ensures proper padding, salt, and IV usage

---

## 🎨 UI/UX Features

* 🧭 **Clear navigation menus** with back options
* 🎨 **Emoji-enhanced CLI** for improved readability
* 📥 **User prompts** for confirmation, errors, and outputs
* 🔁 Loop-based interfaces — no restart needed

---

## 📂 Folder Structure

```
📦 File-Integrity-Checker
├── main.py
├── First Task/
│   └── first_task.py
├── Second Task/
│   └── second_task.py
├── Third Task/
│   ├── third_task.py
│   └── modules/
│       ├── port_scanner.py
│       ├── brute_forcer.py
│       ├── dir_scanner.py
│       ├── web_vuln_scanner.py
│       └── hash_cracker.py
├── Fourth Task/
│   └── fourth_task.py
├── README.md
└── LICENSE
```

---

## 📝 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---
