# CipherForge - Caesar Cipher Toolkit

## Overview

CipherForge is a Python-based cryptography project that demonstrates the implementation of the Caesar Cipher algorithm along with additional security-related features. The project allows users to encrypt and decrypt text, perform brute-force analysis, process files, generate reports, and maintain operation logs.

This project was developed as part of the Prodigy InfoTech Cyber Security Internship Program.

---

## Features

### Text Encryption

* Encrypt plaintext using a custom shift value.

### Text Decryption

* Decrypt ciphertext using the correct shift value.

### Brute Force Analysis

* Attempts all possible shift values.
* Displays every possible decryption result.
* Suggests the most likely plaintext using keyword-based analysis.

### File Encryption

* Encrypts the contents of a text file.
* Saves the encrypted output into a separate folder.

### File Decryption

* Decrypts encrypted text files.
* Generates decrypted copies automatically.

### ROT13 Encoding

* Supports ROT13 transformation (Shift = 13).

### Activity Logging

* Records all operations with timestamps.
* Maintains an audit trail in a history log.

### Log Search

* Search and filter entries from the history log.

### Security Report Generation

* Generates a report containing:

  * Operation history
  * Total operations performed
  * Operation summary statistics

---

## Technologies Used

* Python
* File Handling
* Basic Cryptography Concepts
* Logging
* Text Processing

---

## Project Structure

```text
CipherForge/
│
├── caesar_cipher.py
├── sample.txt
│
├── encrypted_files/
│   └── encrypted_sample.txt
│
├── decrypted_files/
│   └── decrypted_encrypted_sample.txt
│
└── exports/
    ├── activity_log.txt
    └── security_report.txt
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/manigandanb02/PRODIGY_CS_01.git CipherForge
```

2. Navigate to the project folder

```bash
cd CipherForge
```

3. Run the program

### Windows

```bash
python caesar_cipher.py
```

### Linux (Ubuntu)

```bash
python3 caesar_cipher.py
```

---

## Sample Features Demonstrated

* Encrypt Text
* Decrypt Text
* Brute Force Analysis
* Encrypt File
* Decrypt File
* ROT13 Encoding
* View Logs
* Search Logs
* Export Security Report

---

## Learning Outcomes

Through this project, I learned:

* Classical cryptography concepts
* Caesar Cipher algorithm implementation
* Brute-force attack techniques
* File handling in Python
* Logging and auditing
* Report generation
* Menu-driven application development

---

## Disclaimer

Caesar Cipher is a classical encryption technique and is not secure for modern communication systems. This project is intended for educational and learning purposes only.
