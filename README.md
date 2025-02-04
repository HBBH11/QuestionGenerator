# QuestionGenerator

# PL-300 Certification Quiz Application
Overview
This Streamlit-based web application is a comprehensive quiz tool designed to help students prepare for the Microsoft Power BI Data Analyst (PL-300) certification exam. The application fetches questions from Firebase, randomly samples questions across different categories, and provides an interactive quiz experience with detailed performance analysis.
Key Features

Random question sampling across 4 exam categories
Support for single and multiple-choice questions
Image support for question illustrations
Real-time answer tracking
Comprehensive performance analytics
Category-wise performance breakdown
Interactive visualization of quiz results

# Technologies Used

Streamlit
Firebase
Plotly
Matplotlib
Python

# Categories Covered

Prepare Data (12 questions)
Model Data (10 questions)
Power BI Service (6 questions)
Visualization (12 questions)

# Quiz Mechanics

Total Questions: 40
Passing Threshold: 70%
Randomized question selection
Immediate feedback on submitted answers

# Performance Metrics

Overall correct answer percentage
Pass/Fail indication
Gauge chart showing performance
Detailed category-wise performance histogram
Individual question review (correct/incorrect)

# Setup Requirements

Firebase project
Firestore database with questions
Firebase service account credentials
Streamlit secrets configuration
Python 3.8+
Required Python libraries (see requirements.txt)

# Installation
git clone https://github.com/yourusername/pl300-quiz-app.git
cd pl300-quiz-app
pip install -r requirements.txt
streamlit run app.py

# Contribution
Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request.
