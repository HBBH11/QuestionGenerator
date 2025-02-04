import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import random

# Firebase Initialization
def initialize_firebase():
    if not firebase_admin._apps:  # Check if a Firebase app is already initialized
        cred = credentials.Certificate({
            "type": st.secrets["type"],
            "project_id": st.secrets["project_id"],
            "private_key_id": st.secrets["private_key_id"],
            "private_key": st.secrets["private_key"],
            "client_email": st.secrets["client_email"],
            "client_id": st.secrets["client_id"],
            "auth_uri": st.secrets["auth_uri"],
            "token_uri": st.secrets["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["client_x509_cert_url"],
            "universe_domain": st.secrets["universe_domain"]
        })
        firebase_admin.initialize_app(cred)
    else:
        print("Firebase is already initialized.")

# Fetch all questions
def fetch_all_questions():
    try:
        db = firestore.client()
        questions_ref = db.collection("questions")
        query_snapshot = questions_ref.get()

        questions = []
        for doc in query_snapshot:
            question_data = doc.to_dict()
            questions.append(question_data)

        if not questions:
            st.warning("No questions found in the database.")

        return questions
    except Exception as e:
        st.error(f"Error retrieving questions: {e}")
        return []

def main():
    # Custom CSS for sidebar minimization and back to top button
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] {
            min-width: 1px;
            max-width: 200px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            margin-left: -1px;
        }
        
        /* Style for back to top button */
        .back-to-top {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background-color: #0E1117;
            color: white;
            padding: 10px 15px;
            border-radius: 50%;
            text-decoration: none;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            z-index: 1000;
            transition: background-color 0.3s;
        }
        .back-to-top:hover {
            background-color: #262730;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create an anchor for the top of the page
    st.markdown('<div id="top"></div>', unsafe_allow_html=True)

    # Add back to top button
    st.markdown(
        '''
        <a href="#top" class="back-to-top">
            ⬆️
        </a>
        ''',
        unsafe_allow_html=True
    )

    st.title("PL-300 Certification Quiz")

    # Initialize Firebase
    initialize_firebase()

    # Fetch all questions
    questions = fetch_all_questions()

    # Check if questions are already sampled and stored in session
    if 'sampled_questions' not in st.session_state:
        # Filter questions by category
        prepare_data_questions = [q for q in questions if q.get("Category") == "Prepare the data"]
        model_data_questions = [q for q in questions if q.get("Category") == "Model the data"]
        pbi_service_questions = [q for q in questions if q.get("Category") == "PBI Service"]
        visualization_questions = [q for q in questions if q.get("Category") == "Visualization"]

        # Random sampling of required number of questions for each category
        prepare_data_questions = random.sample(prepare_data_questions, 12)
        model_data_questions = random.sample(model_data_questions, 10)
        visualization_questions = random.sample(visualization_questions, 12)
        pbi_service_questions = random.sample(pbi_service_questions, 6)

        # Combine questions
        st.session_state.sampled_questions = prepare_data_questions + model_data_questions + visualization_questions + pbi_service_questions

    questions = st.session_state.sampled_questions

    # Store user answers in session
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {q["question_text"]: [] for q in questions}

    # Display questions with appropriate input types
    for index, question in enumerate(questions, start=1):
        st.write(f"**Question {index}:** {question['question_text']}")
        
        # Check for image_url and handle multiple images
        if 'image_url' in question and question['image_url']:
            # Split image_url string into individual URLs
            image_urls = [url.strip() for url in question['image_url'].split(',')]
            
            # Create columns for multiple images if needed
            if len(image_urls) > 1:
                cols = st.columns(len(image_urls))
                for idx, url in enumerate(image_urls):
                    if url:  # Check if URL is not empty
                        try:
                            cols[idx].image(url, caption=f'Image {idx + 1}', use_container_width=True)
                        except Exception as e:
                            cols[idx].error(f"Image loading error {idx + 1}: {e}")
            else:  # Single image
                try:
                    st.image(image_urls[0], caption='Question Image', use_container_width=True)
                except Exception as e:
                    st.error(f"Image loading error: {e}")

        # Prepare choices from comma-separated string
        choices = question.get("Choices", "").split(",")
        correct_answers = question.get("answer_text", "").split(",")

        if len(correct_answers) == 1:  # Single answer
            selected_answer = st.radio("Choose your answer:", choices, key=f"radio_{index}")
            if selected_answer:
                st.session_state.user_answers[question["question_text"]] = [selected_answer]
        elif len(correct_answers) > 1:  # Multiple answers
            selected_answers = []
            for choice in choices:
                unique_key = f"checkbox_{index}_{choice.strip()}"
                if st.checkbox(choice.strip(), key=unique_key):
                    selected_answers.append(choice.strip())
            st.session_state.user_answers[question["question_text"]] = selected_answers

    # Submit button to check answers
    if st.button("Submit"):
        correct_count = 0
        category_correct_count = {
            "Prepare the data": 0,
            "Model the data": 0,
            "PBI Service": 0,
            "Visualization": 0
        }

        # Create containers for correct and incorrect answers
        correct_container = st.container()
        incorrect_container = st.container()
        
        with correct_container:
            st.markdown("### ✅ Correct Questions:")
        
        with incorrect_container:
            st.markdown("### ❌ Incorrect Questions:")

        for idx, question in enumerate(questions, 1):
            correct_answers = question.get("answer_text", "").split(",")
            user_answer = st.session_state.user_answers[question["question_text"]]

            # Check if user's answer is correct
            if isinstance(user_answer, list):  # For multiple answers
                if set(user_answer) == set(correct_answers):
                    correct_count += 1
                    category_correct_count[question["Category"]] += 1
                    with correct_container:
                        st.success(f"**Question {idx}:** {question['question_text']}\n\n**Your answer:** {', '.join(user_answer)}")
                else:
                    with incorrect_container:
                        st.error(f"**Question {idx}:** {question['question_text']}\n\n**Your answer:** {', '.join(user_answer)}\n\n**Correct answer(s):** {', '.join(correct_answers)}")
            else:  # For single answer
                if user_answer in correct_answers:
                    correct_count += 1
                    category_correct_count[question["Category"]] += 1
                    with correct_container:
                        st.success(f"**Question {idx}:** {question['question_text']}\n\n**Your answer:** {user_answer}")
                else:
                    with incorrect_container:
                        st.error(f"**Question {idx}:** {question['question_text']}\n\n**Your answer:** {user_answer}\n\n**Correct answer(s):** {', '.join(correct_answers)}")

        total_questions = len(questions)
        correct_percentage = (correct_count / total_questions) * 100

        st.markdown("---")
        st.markdown(f"**You got {correct_count} out of {total_questions} questions correct ({correct_percentage:.2f}%)!**")

        # Congratulations message based on performance
        if correct_percentage >= 70:
            st.success("Congratulations! You passed the quiz! 🎉")
        else:
            st.error("Unfortunately, you did not pass the quiz. You'll have better luck next time!")

        # Gauge chart with 70% target value
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=correct_percentage,
            title={'text': "Percentage of Correct Answers"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "white"},
                'steps': [
                    {'range': [0, 69], 'color': "red"},
                    {'range': [70, 100], 'color': "lightgreen"},
                ],
                'threshold': {
                    'line': {'color': "blue", 'width': 4},
                    'thickness': 0.75,
                    'value': 70
                }
            }
        ))
        
        gauge_fig.add_annotation(
            x=0.5,
            y=0.5,
            text="Target: 70",
            showarrow=False,
            font=dict(size=16, color="blue"),
            bgcolor="white",
            bordercolor="blue",
            borderwidth=2,
            borderpad=4,
            opacity=0.8
        )

        st.plotly_chart(gauge_fig)

        st.markdown(f"**In the 'Prepare Data' category, you got {category_correct_count['Prepare the data']} questions correct out of 12.**")
        st.markdown(f"**In the 'Model Data' category, you got {category_correct_count['Model the data']} questions correct out of 10.**")
        st.markdown(f"**In the 'Power BI Service' category, you got {category_correct_count['PBI Service']} questions correct out of 6.**")
        st.markdown(f"**In the 'Visualization' category, you got {category_correct_count['Visualization']} questions correct out of 12.**")

        # Create histogram
        categories = list(category_correct_count.keys())
        correct_values = list(category_correct_count.values())

        fig, ax = plt.subplots()
        ax.bar(categories, correct_values, color='skyblue')
        ax.set_xlabel('Category')
        ax.set_ylabel('Correct Answers')
        ax.set_title('Correct Answers by Category')
        ax.set_yticks(np.arange(0, max(correct_values) + 1, 1))

        st.pyplot(fig)

        # Create two columns for buttons at the bottom
        col1, col2 = st.columns(2)
        
        # Retry button in the first column
        with col1:
            if st.button("Retry"):
                # Reset session variables
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                # Reload page
                st.experimental_rerun()

if __name__ == "__main__":
    main()