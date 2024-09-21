from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['user_data']
class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_dict(self):
        return {
            'age': self.age,
            'gender': self.gender,
            'total_income': self.total_income,
            **self.expenses
        }

def save_to_csv(data, filename='user_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'age': request.form['age'],
        'gender': request.form['gender'],
        'total_income': request.form['total_income'],
        'expenses': {
            'utilities': request.form.get('utilities', 0),
            'entertainment': request.form.get('entertainment', 0),
            'school_fees': request.form.get('school_fees', 0),
            'shopping': request.form.get('shopping', 0),
            'healthcare': request.form.get('healthcare', 0),
        }
    }
    db.users.insert_one(user_data)
    # Save to CSV
    users = list(db.users.find())
    save_to_csv([User(**data).to_dict() for data in users])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
