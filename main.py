import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from sklearn import linear_model
from word2number import w2n
import math 


with open('./style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


df = pd.read_csv("./hiring.csv")

df = df.rename(columns={'test_score(out of 10)': 'test_score'})
df = df.rename(columns={'interview_score(out of 10)': 'interview_score'})
df = df.rename(columns={'salary($)': 'salary'})


st.header("Predicting Employee Salary: Using Candidate Analytics")
st.write("Initial data : ")
st.write(df)


df.experience = df.experience.fillna('zero')
test_score_mean = math.floor(df.test_score.mean())
df.test_score = df.test_score.fillna(test_score_mean)
df.experience = df['experience'].apply(w2n.word_to_num)

st.write('After Data Processing : ')
ui.table(df)

reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score','interview_score']], df.salary)
st.write("Regression Coffs.")
st.write(reg.coef_,)

def cal_predictSalary(data):
    return reg.predict(pd.DataFrame(data, columns=['experience','test_score','interview_score']))

def predictSalary(data):
    formated_data =   {
        "experience": data[0],
        "test_score": data[1],
        "interview_score": data[2],
        "Expected Salary":math.floor(cal_predictSalary([data])[0])
    }
    return st.dataframe(formated_data)



st.write("Demo:")
predictSalary([1,9,6])

labels = ["Experience", "Test Score", "Interview Score"]
placeholders = ["Years of Experience ", "Score (out of 10)", "Score (out of 10)"]

user_inputs = []

st.write("Choose Fields : ")   
col1, col2, col3 = st.columns(3)

with col1:
    user_inputs.append(st.number_input(labels[0], min_value=0, placeholder=placeholders[0]))
with col2:
    user_inputs.append(st.number_input(labels[1], min_value=0, max_value=10, placeholder=placeholders[1]))
with col3:
    user_inputs.append(st.number_input(labels[2], min_value=0, max_value=10, placeholder=placeholders[2]))
    
 

if len(user_inputs) > 0:
    experience, test_score, interview_score = user_inputs
    st.subheader("Values :")
    predictSalary(user_inputs)