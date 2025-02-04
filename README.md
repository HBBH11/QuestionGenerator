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

# Overall correct answer percentage

# Pass/Fail indication

![image](https://github.com/user-attachments/assets/b5f64df3-28d1-4734-9742-f8d9970c3393)

# Gauge chart showing performance

![image](https://github.com/user-attachments/assets/24994842-681e-4883-8945-cf4f0a208964)

# Detailed category-wise performance histogram

![image](https://github.com/user-attachments/assets/003f36e3-87c7-4c0c-8863-181c06b8c4f9)

# Individual question review (correct/incorrect)

![image](https://github.com/user-attachments/assets/68d2d936-69ad-4cf3-aa45-15cffce5c477)

![image](https://github.com/user-attachments/assets/25482398-6c31-4dd3-b163-d61f95ab83b1)


# Setup Requirements

Firebase project

Firestore database with questions

Firebase service account credentials

Streamlit secrets configuration

Python 3.8+

Required Python libraries (see requirements.txt)


# Installation

git clone https://github.com/HBBH11/QuestionGenerator.git

cd QuestionGenerator

pip install -r requirements.txt

streamlit run QuestionGenerator.py


# Contribution
Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request.

# PS : 
You have to add "type, project_id, private_key_id, private_key, client_email, client_id, auth_uri, token_uri & auth_provider_x509_cert_url " from your firebase, like this one :

type = "service_account"

project_id = "datailab-c93d6"

private_key_id = "3280024b0*****************0e2f0"

private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5Hncjq/rqIlIe\nA31ZrwRNnDtUhwkVKw1Ee5w4farg9zreC89T8VzgoNdZV7+tStxgiykx8EhFLHaW\nbcfiwkFKRd3ZZMOkuM+jdUAwMFZsI6lT3h5Htw/lRmi/OVoQfP/jiH7CAEG4+zat\ngEeIFTg+K1fHtUb9jlu1xIVk***********************************************MV1EQvKe0tCjSdu4=\n-----END PRIVATE KEY-----\n"

client_email = "firebase-adminsdk-mp0av@datailab-c93d6.iam.gserviceaccount.com"

client_id = "112765279431227463150"

auth_uri = "https://accounts.google.com/o/oauth2/auth"

token_uri = "https://oauth2.googleapis.com/token"

auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"

client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mp0av%40datailab-c93d6.iam.gserviceaccount.com"

universe_domain = "googleapis.com"
