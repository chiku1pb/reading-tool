# 🧠 Cognitive Engine
**Frictionless document accessibility for the modern web.**
Built for AU Hackathon 2.0 at Atmiya University.

## The Problem
Standard digital text is fundamentally hostile to neurodivergent readers and individuals with visual processing differences (like Astigmatism or Irlen Syndrome). Highlighting, reformatting, and struggling with visual crowding drains time and energy.

## The Solution
The Cognitive Engine is a zero-database, privacy-first web application that instantly transforms hostile documents into perfectly accessible, highly readable formats.

### ✨ Key Features
* **Cognitive Focus:** Automatically anchors the eye by intelligently calculating word midpoints and applying targeted bolding, allowing the brain to process text faster and with less effort.
* **Optical Harmony Mode:** Instantly shifts the UI to a warm, e-ink tone while programmatically expanding letter-spacing and line-height to eliminate screen glare and visual crowding.
* **Universal Drop Zone:** Seamlessly extracts and processes raw text from `.txt`, `.pdf`, and `.docx` files.
* **Absolute Privacy (Zero-Database):** Sensitive medical, legal, or educational documents are never stored. The engine utilizes an in-memory document stack that vanishes the second the tab is closed.
* **Frictionless Navigation:** A built-in document memory stack allows users to fluidly flip back and forth between uploaded files like pages in a book.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Text Processing:** Regular Expressions (`re`), `math`, `PyPDF2`, `python-docx`
* **Frontend:** Pristine HTML5, CSS3, Vanilla JavaScript (Zero-reload AJAX architecture)

## 🚀 How to Run Locally
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install flask PyPDF2 python-docx


   its good for those who love reading in their type of comfort
   