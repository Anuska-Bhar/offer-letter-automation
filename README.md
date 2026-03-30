# offer-letter-automation

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