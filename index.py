import streamlit as st
st.title("xyz company")
st.header("Job Description for 10000 coder")
st.write("A job description for a 10000 coder refers to a role for a software development trainee or junior developer who has completed a training program with the organization 10000 Coders. The job description involves writing, modifying, and testing code for web applications and other software, using skills gained from their immersive training in full-stack web development, problem-solving, and practical application building. Responsibilities include creating production-ready applications, working on real-world assignments, and potentially other tasks like working in teams or providing technical support.")
st.subheader("skills requrede: ")
st.divider()
st.markdown("python,sql,html,css,javascript,react,nodejs,express,mongodb,git")
st.header("Enter you detiles:")
name=st.text_input("Enter your name")
email=st.text_input("Enter your email")
phone=st.text_input("Enter your phone number")
CGPA=st.text_input("Enter your CGPA")
COllgename=st.text_input("Enter your college name") 
st.radio("Enter your graduation year",[2023,2024,2025])
st.radio("Select your Gender",["male","female","other"])
st.file_uploader("Upload your resume")     
st.text_area("Why do you want to join xyz comapny")
st.write("By clicking submit, you agree to our terms and conditions.")
st.checkbox("I agree to the terms and conditions")


st.button("Submit")

