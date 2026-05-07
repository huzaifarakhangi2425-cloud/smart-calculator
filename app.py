from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure key

DATABASE = 'expense_tracker.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create database and tables if they don't exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date DATE NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']

    if not date:
        date = datetime.now().date()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)",
        (description, float(amount), category, date)
    )
    conn.commit()
    cursor.close()
    conn.close()

    flash('Expense added successfully!')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Expense deleted successfully!')
    return redirect(url_for('index'))

@app.route('/chart')
def chart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if not data:
        return "<p>No data available for chart</p>"

    # Create a simple HTML bar chart
    chart_html = '''
    <div style="width: 100%; max-width: 600px; margin: 0 auto;">
        <h3>Expenses by Category</h3>
        <div style="display: flex; flex-direction: column; gap: 10px;">
    '''
    
    max_total = max(float(row['total']) for row in data) if data else 1
    
    for row in data:
        category = row['category']
        total = float(row['total'])
        percentage = (total / max_total) * 100 if max_total > 0 else 0
        
        chart_html += f'''
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 120px; font-weight: bold;">{category}</div>
            <div style="flex: 1; background: #f0f0f0; height: 30px; border-radius: 5px; overflow: hidden;">
                <div style="width: {percentage}%; background: #007bff; height: 100%; border-radius: 5px; display: flex; align-items: center; padding-left: 10px; color: white; font-weight: bold;">
                    ${total:.2f}
                </div>
            </div>
        </div>
        '''
    
    chart_html += '''
        </div>
    </div>
    '''
    
    return chart_html

if __name__ == '__main__':
    app.run(debug=True)