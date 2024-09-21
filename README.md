Survey Flask Application
Overview
This is a Flask-based survey application that collects participant data on income and expenses. It stores the data in MongoDB and allows the user to export the data to CSV. The application is hosted on AWS using Elastic Beanstalk.

Features
Collects user data (age, gender, income, expenses).
Stores data in MongoDB.
Exports data to CSV format.
Deployed on AWS Elastic Beanstalk.
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7+
Flask
MongoDB
AWS CLI
Elastic Beanstalk CLI
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/survey-flask-app.git
cd survey-flask-app
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies: Use pip to install the required Python packages.

bash
Copy code
pip install -r requirements.txt
Configuring AWS
AWS Elastic Beanstalk Setup: Make sure you have the AWS CLI and Elastic Beanstalk CLI set up. Run the following command to configure Elastic Beanstalk:

bash
Copy code
eb init
Follow the prompts to configure your application for AWS.

Deploying to AWS Elastic Beanstalk: After configuring Elastic Beanstalk, deploy the application:

bash
Copy code
eb create
eb deploy
Setting AWS Environment Variables: Set your AWS credentials, MongoDB connection string, and other environment variables via the AWS Elastic Beanstalk Console or via the following command:

bash
Copy code
eb setenv MONGODB_URI=your-mongo-uri
Running the Application Locally
To run the application on your local machine:

bash
Copy code
python application.py
The app will be available at http://127.0.0.1:5000.

Directory Structure
bash
Copy code
survey-flask-app/
│
├── application.py          # Main Flask application file
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
├── user_data.csv           # Exported data (optional)
└── templates/              # HTML templates
    └── index.html          # Main page
Usage
Access the web application to enter user details like age, gender, income, and expenses.
The data is stored in MongoDB, and you can export the data to a CSV file.
