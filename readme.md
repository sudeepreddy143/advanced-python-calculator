# Advanced Python Calculator #

**Software Engineering Graduate Course Midterm Project**

## Overview

This project presents an **Advanced Python Calculator** featuring:

- **Command-Line Interface (REPL):** Interactive environment for executing arithmetic operations and managing calculation history.
- **Dynamic Plugin System:** Seamless integration of new commands without altering core functionality.
- **Calculation History Management:** Utilizing Pandas for efficient data handling.
- **Structured Logging:** Configurable logging to monitor application behavior.
- **Design Patterns:** Implementation of Command, Factory Method, and Facade patterns.
- **Docker Support:** Containerization for consistent deployment.
- **Continuous Integration:** Automated testing and linting via GitHub Actions.

## 📌 GitHub Repository

[🔗 GitHub Repository](https://github.com/sudeepreddy143/advanced-python-calculator)

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Available Commands](#available-commands)
4. [Calculation History Management](#calculation-history-management)
5. [Logging Configuration](#logging-configuration)
6. [Design Patterns Implemented](#design-patterns-implemented)
7. [Testing](#testing)
8. [Continuous Integration](#continuous-integration)
9. [Docker Deployment](#docker-deployment)
10. [Environment Variables](#environment-variables)
11. [Exception Handling](#exception-handling)
12. [Contributing](#contributing)
13. [License](#license)
14. [Project Submission](#project-submission)

## 🚀 Installation

### Clone the Repository

```sh
git clone https://github.com/sudeepreddy143/advanced-python-calculator.git
cd advanced-python-calculator
```

### Set Up Virtual Environment 

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Run the Application

```sh
python -m app.repl
```

---

## 🔢 Available Commands

### Basic Operations
- **Addition**: `add <num1> <num2>`
- **Subtraction**: `sub <num1> <num2>`
- **Multiplication**: `mul <num1> <num2>`
- **Division**: `div <num1> <num2>`

### Plugin Commands
- **Power**: `power <base> <exponent>`
- **Square Root**: `square <number>`

### Utility Commands
- **Menu**: `menu` – Displays all available commands.
- **History**: `history` – Shows the last 10 calculations.
- **Exit**: `exit` – Exits the application.

---

## 📊 Calculation History Management

The application uses Pandas to manage calculation history, enabling:

- **Viewing History**: `history`
- **Saving History to CSV**: Integrated to directly save to CSV
- **Loading History from CSV**: `history`
- **Delete the last entry**: `delete_last`
- **Clearing History**: `clear_history`

---

## 📦 Running in Docker

### 🛠 Build & Run

```sh
docker build -t advanced-python-calculator .
docker run -it --rm advanced-python-calculator
```

---

## 🧪 Running Tests

```sh
pytest tests/
pylint app test
```

---

## ⚙️ Exception Handling

### Strategies Used:
- **LBYL (Look Before You Leap)**
- **EAFP (Easier to Ask for Forgiveness than Permission)**

#### Example:

```python
try:
    result = 10 / user_input
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

---

## 📜 Design Patterns Implemented

- **Command Pattern**
- **Factory Method**
- **Facade Pattern**

📌 [🔗 Link to Implementation](📌 [🔗 Link to Implementation](https://github.com/sudeepreddy143/advanced-python-calculator/tree/main/app/)
)

---

## 🌍 Environment Variables

The project uses environment variables for configuration. 
we should create one for INFO | WARNING | ERROR

📌 [🔗 Link to Implementation](https://github.com/sudeepreddy143/advanced-python-calculator/blob/main/app/.env)

---

## 📜 Logging Implementation

Structured logging is configured for monitoring application behavior.

📌 [🔗 Link to Logging Implementation](https://github.com/sudeepreddy143/advanced-python-calculator/blob/main/app/logging_config.py)


---
## DockerFile | compose file

Devops (containers)

📌 [🔗 Link to Logging Implementation](https://github.com/sudeepreddy143/advanced-python-calculator/blob/main/docker-compose.yaml)

##plugins

📌 [🔗 Link to Logging Implementation](https://github.com/sudeepreddy143/advanced-python-calculator/blob/main/app/plugins)


## Video 

This project Analysis.

---

📌 [🔗 Drive Link](https://github.com/sudeepreddy143/advanced-python-calculator)
