import os
import pickle
import streamlit as st
import random
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Cardiabetes Insight",
                   layout="wide",
                   page_icon="🫀 🩺")

# Set custom CSS for sidebar background color
st.markdown("""
    <style>
    <style>
:root {
    --primary-color:#016b6f;}
    .sidebar .sidebar-content {
        background-color: #008080;
        color: white;
    }
    .sidebar .sidebar-content .sidebar-section .sidebar-section-content {
        color: white;
    }
    .menu .nav-item .nav-link.active[data-v-5af006b8] {
    background-color: teal;
}
    .st-emotion-cache-10trblm {
    position: relative;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    color: teal;
    align-items: cennter;
    display: flex;
    align-content: center;
    justify-content: space-around;
}
    .st-emotion-cache-6qob1r {
    position: relative;
    height: 100%;
    width: 100%;
    overflow: overlay;
    background-color: darkcyan;
}
    .st-emotion-cache-10trblm {
    position: relative;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    color: teal;
}
    .menu .nav-item .nav-link.active[data-v-5af006b8] {
    background-color: #016b6f;
}
    .st-emotion-cache-7ym5gk {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 38.4px;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(255, 255, 255);
    border: 2px solid rgb(0 87 91 / 75%);
    color: teal;
    padding: 11px;
}
    .st-emotion-cache-183lzff {
    font-family: "Source Code Pro", monospace;
    white-space: pre;
    font-size: 19px;
    overflow-x: auto;
    font-style: italic;
    font-weight: bold;
}
    </style>
    """, unsafe_allow_html=True)

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_disease_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Cardiabetes Insights',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                           ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Define tips for each condition
diabetic_tips = [
    "Monitor your blood sugar regularly.",
    "Maintain a balanced diet rich in fiber and low in simple carbs.",
    "Stay hydrated by drinking plenty of water.",
    "Exercise regularly, aiming for at least 150 minutes of moderate activity per week.",
    "Take your medications as prescribed by your healthcare provider.",
    "Manage stress through relaxation techniques like meditation or yoga.",
    "Get regular check-ups and screenings for diabetes-related complications.",
    "Practice good foot care by inspecting your feet daily and keeping them clean and dry.",
    "Stay informed about diabetes and consider joining a support group.",
    "Always carry a source of fast-acting sugar in case of hypoglycemia.",
    "Wear a medical ID bracelet indicating you have diabetes."
]

heart_disease_tips = [
    "Eat a healthy diet rich in fruits, vegetables, and whole grains.",
    "Limit saturated fats, trans fats, cholesterol, and sodium in your diet.",
    "Exercise regularly, aiming for at least 150 minutes of moderate activity per week.",
    "Maintain a healthy weight.",
    "Avoid smoking and limit alcohol consumption.",
    "Manage stress through relaxation techniques like meditation or yoga.",
    "Get regular check-ups and screenings for heart health.",
    "Monitor your blood pressure and cholesterol levels.",
    "Take your medications as prescribed by your healthcare provider.",
    "Stay informed about heart health and consider joining a support group."
]



# Functions to generate random tips
def generate_random_diabetes_tip():
    return random.choice(diabetic_tips)

def generate_random_heart_disease_tip():
    return random.choice(heart_disease_tips)



# Diabetes Prediction Page
st.title('Cardiabetes Insight')
st.subheader('Insights for Cardiovascular Health and Diabetic Well-being.')
if selected == 'Diabetes Prediction':
   

    st.title('Diabetes Prediction using ML')
    random_tip = generate_random_diabetes_tip()
    if st.button('Generate Diabetes Tip'):
        random_tip = generate_random_diabetes_tip()
    st.text(f'💡 Tip: {random_tip}')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    random_tip = generate_random_heart_disease_tip()
    if st.button('Generate Heart Disease Tip'):
        random_tip = generate_random_heart_disease_tip()
    st.text(f'💡 Tip: {random_tip}')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    st.success(heart_diagnosis)

