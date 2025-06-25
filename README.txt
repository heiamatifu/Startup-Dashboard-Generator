Startup Dashboard Generator

This is a full-stack mini dashboard application for startup founders.
Frontend: HTML + CSS + JavaScript (with Chart.js)
Backend: Python (Flask API)

Features:
- Enter startup name, revenue, users, growth %
- Dynamic bar chart visualization
- AI-style summary from backend (via Flask)
- Download summary as a .txt file

How to Run Backend:
1. Install Python and Flask: pip install flask flask-cors
2. Run: python generate_summary_api.py
3. Frontend will call: http://localhost:5000/api/summary
