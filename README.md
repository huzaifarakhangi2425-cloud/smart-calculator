# Expense Tracker

A simple web-based expense tracker application built with Flask and SQLite.

## Features

- Add expenses with description, amount, category, and date
- View all expenses in a list
- Delete expenses
- Visualize expenses by category with a bar chart
- Responsive web interface using Bootstrap

## Installation

1. Clone or download the project files
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```
2. Open your web browser and go to `http://localhost:5000`
3. Add expenses using the form
4. View your expense history and chart

## Database

The application uses SQLite database (`expense_tracker.db`) which is created automatically when you first run the app.

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Charts**: Custom HTML/CSS bar charts

## Project Structure

```
expense-tracker/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Main web page template
├── static/                # Static files (CSS, JS, images)
├── expense_tracker.db     # SQLite database (created automatically)
└── requirements.txt       # Python dependencies
```