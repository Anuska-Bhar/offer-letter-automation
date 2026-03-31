# offer-letter-automation

## 🚀 Quick Start (1 Click Setup)

### Step 1: Install Docker
https://www.docker.com/products/docker-desktop/

---

### Step 2: Run System

```bash
docker-compose up

---

### Step 3: Open n8n(Automation Interface)

Open your browser:

http://localhost:5678

#### First-Time Setup:
- Enter your email  
- Create a password  
- Click **Sign Up**  

(This account is only for your local system)

---

### Step 4 — Import Workflow

- Click **Import** in n8n after + worflow  
- Upload file: `n8n/workflow.json`  

---

### Step 5 — Connect Google Account

Required for:
- Google Sheets node 
- Google Drive node

Steps:
- Open a Google Sheets node  
- Click **Create Credential** and eenter client id and secret key from your web application in google cloud
- Sign in with your Google account  
- Grant permissions  

Repeat for Google Drive node.

---

### Step 6 — Create Input Sheet

Create a Google Sheet named:

`Employee Details`

Columns:
name | position | annual_salary_pa | variable_pay_pa | joining_date | renumeration_sal | renumeration_vp | responsibilities

---

### Step 7 — Create Output Sheet

Create another sheet:

`Employee Sheet`

Headers:
template_key | name | position | annual_salary_pa | variable_pay_pa | joining_date | renumeration_sal | renumeration_vp | responsibilities | status | file_url | error
(Leave empty initially)

---

### Step 8 — Configure Sheets in n8n

- Open Google Sheets nodes  
- Set:
  - Input → **Employee Details**  
  - Output → **Employee Sheet**

---

### Step 9 — Run Automation

Click:

▶ **Execute Workflow**

---

## Features
- Google Sheets input
- Automated document generation
- Role-based templates
- Google Drive integration
- Error handling
- Docker deployment

## Tech Stack
- FastAPI
- n8n
- Google Sheets API
- Google Drive API
- Python

## Setup
1. Clone repo
2. Run docker-compose up
3. Setup n8n workflow
4. Add Google Sheet

## Flow
Sheets → n8n → FastAPI → DOCX → Drive → Update Sheet