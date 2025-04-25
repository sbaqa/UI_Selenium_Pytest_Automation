# 🧪 UI Selenium Pytest Automation

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Framework](https://img.shields.io/badge/Framework-Pytest-yellow.svg)

A robust UI test automation framework using **Selenium WebDriver**, **Python**, and **Pytest**, following best practices like **Page Object Model (POM)**, reusable fixtures, and modular structure.  
Perfect for scalable, maintainable, and parallel UI test execution for web applications.

---

## 🚀 Features

- ✅ Page Object Model (POM) structure
- ✅ Selenium WebDriver for browser automation
- ✅ Pytest for test execution and reporting
- ✅ Allure Reports integration
- ✅ Parallel execution support (`pytest-xdist`)
- ✅ Configurable test environments (local/grid)
- ✅ Email reporting support (optional)
- ✅ Easy to scale and customize

---

## 📁 Project Structure

<pre lang="markdown"> ```text UI_Selenium_Pytest_Automation/ ├── configs/ # Environment and base configs ├── pages/ # Page object models ├── reports/ # Allure or HTML reports ├── tests/ # Test cases ├── utils/ # Utility functions and wrappers ├── conftest.py # Pytest fixtures and hooks ├── requirements.txt # Project dependencies └── README.md # Project documentation ``` </pre>

---

## ⚙️ Prerequisites

- Python 3.8 or higher
- Google Chrome or any supported browser
- pip (Python package manager)

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/sbaqa/UI_Selenium_Pytest_Automation.git
cd UI_Selenium_Pytest_Automation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
brew install allure
```
## ▶️ Running Tests

### Run a specific module with tests: 
``` pytest tests/test_login.py ```

### Run Tests in Parallel (4 threads): 
``` pytest -n 4 ```

### Generate Allure Report Results: 
``` pytest --alluredir=reports/allure-results ```

### Open Allure Report in Browser:
``` allure serve reports/allure-results ```


