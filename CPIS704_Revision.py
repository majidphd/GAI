import streamlit as st
import random

def ask_question(question_number, question, options, correct_answer, image_url):
    # Display the question number and question
    st.write(f"Question {question_number}: {question}")
    if image_url:
        st.image(image_url)

    # Create a radio button group for the options
    answer_option = st.radio(":blue[**Select the best answer:**]", options)

    # Store the user's answer
    user_answer = answer_option.lower()

    # Check if the user's answer is correct
    is_correct = user_answer == correct_answer.lower()

    return user_answer, is_correct

def evaluate_quiz(user_answers):
    correct_answers = 0
    for answer in user_answers:
        if answer[1]:
            correct_answers += 1
    return correct_answers, len(user_answers)

def display_results(correct_answers, total_questions):
    score_percentage = int((correct_answers / total_questions) * 100)
    st.write(f"You answered {correct_answers} out of {total_questions} correctly ({score_percentage}%).")

    # Provide additional feedback based on the score
    if score_percentage >= 80:
        st.write("Excellent work! You have a strong understanding of the topics covered in this quiz.")
    elif score_percentage >= 60:
        st.write("Good job! You have a good grasp of the material but there is still room for improvement.")
    else:
        st.write("Keep practicing! You can improve your score by reviewing the topics covered in this quiz.")

def handle_quiz_completion(user_answers):
    correct_answers, total_questions = evaluate_quiz(user_answers)

    if correct_answers == total_questions:
        st.success("Congratulations! You answered all questions correctly.")
    else:
        st.warning("Please choose the right answer to move to the next question, **OR** :red[review the topics covered in this quiz and try again.]")

#    display_results(correct_answers, total_questions)

if __name__ == "__main__":
    """
    # :orange[***CPIS704 - Revision***]
    ### This is an example of a simple :blue[***Chatbot Generative AI***]. According to **(Andrew Ng)** one of the tasks that LLMs can carry out is **chatting**. Hope you enjoy it :blush:
    ##### :orange[Please answer the following questions to the best of your ability:]
    """
    st.markdown("**_____________________________________________________________________________**")
    #st.markdown("A generative AI chatbot is a type of conversational AI system that uses deep learning and natural language processing (NLP) techniques to generate human-like text responses in real-time.")
    #st.title("***CPIS704 - Revision***")
    #st.markdown("**Please answer the following questions to the best of your ability.**")

    # Define the quiz questions with image URLs
    questions = [
        {
            "question": ":green[We have studied Microsoft ***Excel functions***, did you understand it?]",
            "options": [":red[Answer 1]","Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q1.png"
        },
        {
            "question": ":green[According to the previous question, the use ***VLOOKUP*** function is when you need to find things in a table or ......?]",
            "options": [":red[Answer 2]","a range by row", "a range by column", "one row", "one column"],
            "correct_answer": "a range by row",
            "image_url": "image/q2.png"
        },
        {
            "question": ":green[We have studied ***Power Query*** for cleaning the data, did you understand it?]",
            "options": [":red[Answer 3]","Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q3.png"
        },
        {
            "question": ":green[According to the previous question, in order to change ***rows into column*** in Power Query we use:]",
            "options": [":red[Answer 4]","unpivot", "transpose", "reverse ", "replace"],
            "correct_answer": "transpose",
            "image_url": "image/q4.png"
        },
        {
            "question": ":green[We have studied ***Power-BI*** to visulize the data, did you understand it?]",
            "options": [":red[Answer 5]", "Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q5.png"
        },
        {
            "question": ":green[According to the previous question, the Power BI's ***Publish to Web*** option allows you to embed visualizations within:]",
            "options": [":red[Answer 6]","blog posts", "email messages", "web sites", "All of above"],
            "correct_answer": "All of above",
            "image_url": "image/q6.png"
        },
        {
            "question": ":green[We have studied the ***Context-Aware***, did you understand it?]",
            "options": [":red[Answer 7]", "Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q7.png"
        },
        {
            "question": ":green[According to the previous question, ***iHCI*** stands for:]",
            "options": [":red[Answer 8]", "Implicit High–Computer Interaction", "Interaction Human–Computer Implicit", "Implicit Human–Computer Interaction","Implicit Human–Computing Interaction"],
            "correct_answer": "Implicit Human–Computer Interaction",
            "image_url": "image/q8.png"
        },
        {
            "question": ":green[We have studied word analysis ***LIWC-22***, did you understand it?]",
            "options": [":red[Answer 9]", "Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q9.png"
        },
        {
            "question": ":green[According to the previous question, LIWC-22 comes with how many built-in ***dictionaries***?]",
            "options": [":red[Answer 10]", "over 10", "over 25", "over 50", "over 100"],
            "correct_answer": "over 100",
            "image_url": "image/q10.png"
        },
        {
            "question": ":green[We have studied ***Ambient Intelligence AmI***, did you understand it?]",
            "options": [":red[Answer 11]", "Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q11.png"
        },
        {
            "question": ":green[According to the previous question, the key features of ambient intelligence are to be:]",
            "options": [":red[Answer 12]", "embedded and context-aware.", "personalised and adaptive.", "anticipatory.","All of above"],
            "correct_answer": "All of above",
            "image_url": "image/q12.png"
        },
        {
            "question": ":green[We have studied ***Streamlit*** to deploy apps, did you understand it?]",
            "options": [":red[Answer 13]", "Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q13.png"
        },
        {
            "question": ":green[According to the previous question, Streamlit is an open source app framework in what language?]",
            "options": [":red[Answer 14]", "C++", "JAVA", "Python", "None of above"],
            "correct_answer": "Python",
            "image_url": "image/q14.png"
        },
        {
            "question": ":green[We have studied ***Generative AI***, did you understand it?]",
            "options": [":red[Answer 15]", "Yes", "No"],
            "correct_answer": "Yes",
            "image_url": "image/q15.png"
        },
        {
            "question": ":green[According to the previous question, the tasks that LLMs can carry out:]",
            "options": [":red[Answer 16]", "Writing", "Reading", "Chatting", "All of above"],
            "correct_answer": "All of above",
            "image_url": "image/q16.png"
        },
    ]

    user_answers = []
    question_number = 1

    for question in questions:
        user_answer, is_correct = ask_question(question_number, question["question"], question["options"], question["correct_answer"], question["image_url"])
        user_answers.append((user_answer, is_correct))

        if not is_correct:
            handle_quiz_completion(user_answers)
            break

        question_number += 1

    if question_number == len(questions) + 1:
        handle_quiz_completion(user_answers)
