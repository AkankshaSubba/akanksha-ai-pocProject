# rfp_automation

Automating RFP generation using AI agents.

NOTE: SQL ODBC Driver 18 is required for anyone attempting to run with the connection string I have provided

## Getting started

### Backend

Navigate to /backend.

Run `pip3 install -r requirements.txt` to install backend dependencies.

Add cover_page.pptx to /app/templates.

Now run `python3 main.py` in /backend to run the backend.

### Frontend

Navigate to /frontend.

Run `npm install` to install frontend dependencies.

Now run `npm run dev` to run the frontend.

pip uninstall fitz

python3 create_db.py