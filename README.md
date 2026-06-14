# QA Automation Lab

Built using Python + Playwright + Pytest . This project focuses on building a simple UI test framework using Project Object Model (POM).

## Tech Stack
- Python
- Playwright (sync API)
- Pytest
- Python logging

## What this repo does
Runs basic UI tests on a demo e-commerce site (SauceDemo)

### Covers:
- Login automation
- Adding items to cart
- Cart validation
- Logging test steps
- Screenshot capture on test failure

---

## Project Structure

```text
qa-automation-lab/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── README.md
├── .gitignore
└── screenshots/
```

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 2. Install Playwright browsers
```bash
playwright install
```

---

### 3. Run tests
```bash
pytest
```
