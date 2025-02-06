# ✨ QuestionGenerator - PL-300 Certification Quiz

A comprehensive quiz application designed to help students prepare for the Microsoft Power BI Data Analyst (PL-300) certification exam.

## 🎯 Overview

This Streamlit-based web application provides an interactive quiz experience with detailed performance analysis, pulling questions from Firebase and offering real-time feedback.

![Performance Overview](https://github.com/user-attachments/assets/b5f64df3-28d1-4734-9742-f8d9970c3393)

## ⭐ Key Features

- 🎲 Random question sampling across 4 exam categories
- ✅ Support for single and multiple-choice questions
- 🖼️ Image support for question illustrations
- ⚡ Real-time answer tracking
- 📊 Comprehensive performance analytics
- 📈 Category-wise performance breakdown
- 📉 Interactive visualization of quiz results

## 🛠️ Technologies Used

- 🌐 **Streamlit**: Web interface
- 🔥 **Firebase**: Database
- 📊 **Plotly**: Data visualization
- 📈 **Matplotlib**: Charting
- 🐍 **Python**: Core logic

## 📚 Categories Covered

- 📝 Prepare Data (12 questions)
- 🔄 Model Data (10 questions)
- ☁️ Power BI Service (6 questions)
- 📊 Visualization (12 questions)

## ⚙️ Quiz Mechanics

- 📋 Total Questions: 40
- 🎯 Passing Threshold: 70%
- 🎲 Randomized question selection
- ⚡ Immediate feedback

## 📊 Performance Metrics

### 📈 Performance Visualization
![Gauge Chart](https://github.com/user-attachments/assets/24994842-681e-4883-8945-cf4f0a208964)

### 📊 Category Performance
![Category Performance](https://github.com/user-attachments/assets/003f36e3-87c7-4c0c-8863-181c06b8c4f9)

### ✅ Question Review
![Review 1](https://github.com/user-attachments/assets/68d2d936-69ad-4cf3-aa45-15cffce5c477)
![Review 2](https://github.com/user-attachments/assets/25482398-6c31-4dd3-b163-d61f95ab83b1)

## 🚀 Setup Requirements

- 🔥 Firebase project
- 📚 Firestore database with questions
- 🔑 Firebase service account credentials
- ⚙️ Streamlit secrets configuration
- 🐍 Python 3.8+
- 📦 Required Python libraries

## 📥 Installation

```bash
git clone https://github.com/HBBH11/QuestionGenerator.git
cd QuestionGenerator
pip install -r requirements.txt
streamlit run QuestionGenerator.py
```

## 🔐 Firebase Configuration

Add the following credentials from your Firebase project:

```python
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "your-private-key"
client_email = "your-client-email"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
universe_domain = "googleapis.com"
```

## 💾 Database Structure

Firebase collection: `questions`
Schema:
- 📑 category
- 📝 choices
- ✅ answer_text
- ❓ question_text
- 🖼️ image_url (optional)

## 🔄 Application Flow

![Quiz Generator Workflow](path-to-your-workflow-svg)

## 🤝 Contributing

Contributions welcome! Please feel free to:
- 🐛 Report bugs
- 💡 Request features
- 🔧 Submit pull requests

## 📝 Notes

- 🖼️ `image_url` field is optional for questions without images
- 🔒 Keep your Firebase credentials secure
- ⚠️ Don't commit sensitive information to version control

