import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\ankur\Downloads\studentperf.pkl")

# Encoding mappings
gender_mapping = {"Male": 0, "Female": 1}
parental = {"Low": 2, "Medium": 0, "High": 1}
access_to_resources = {"Low": 2, "Medium": 0, "High": 1}
motivational_level = {"Low": 2, "Medium": 0, "High": 1}
family_income = {"Low": 2, "Medium": 0, "High": 1}
teacher_quality = {"Low": 2, "Medium": 0, "High": 1}
extra_activity = {"Yes": 0, "No": 1}
internet = {"Yes": 0, "No": 1}
school_type_encoding = {"Public": 0, "Private": 1}  # Renamed to avoid conflict
peer = {"Positive": 0, "Neutral": 1, "Negative": 2}
disability = {"No": 0, "Yes": 1}
parent_education = {"High School": 0, "College": 1, "Postgraduate": 2}
distance = {"Near": 0, "Moderate": 1, "Far": 2}

# Prediction function
def predict_performance(input_data):
    try:
        prediction = model.predict(input_data)
        return prediction[0]
    except Exception as e:
        st.error(f"⚠️ Error in prediction: {e}")
        return None

# Main function
def main():
    st.title("🎓 Student Performance Prediction")
    st.markdown("Enter the details below to predict the exam score based on various factors.")

    # Inputs
    hours_studied = st.number_input("📚 Hours Studied", min_value=0.0, max_value=50.0, value=5.0)
    attendance = st.slider("📅 Attendance (%)", min_value=0, max_value=100, value=85)
    parental_involvement_input = st.selectbox("👨‍👩‍👦 Parental Involvement", ["Low", "Medium", "High"])
    access_to_resources_input = st.selectbox("📖 Access to Resources", ["Low", "Medium", "High"])
    extracurricular_activities = st.selectbox("🎭 Participation in Extracurricular Activities", ["Yes", "No"])
    sleep_hours = st.number_input("😴 Sleep Hours (per day)", min_value=0.0, max_value=24.0, value=8.0)
    previous_scores = st.number_input("📊 Previous Scores", min_value=0, max_value=100, value=70)
    motivation_level_input = st.selectbox("🔥 Motivation Level", ["Low", "Medium", "High"])
    internet_access = st.selectbox("🌐 Internet Access", ["Yes", "No"])
    tutoring_sessions = st.number_input("📚 Tutoring Sessions (per week)", min_value=0, max_value=20, value=2)
    family_income_input = st.selectbox("💰 Family Income", ["Low", "Medium", "High"])
    teacher_quality_input = st.selectbox("📋 Teacher Quality", ["Low", "Medium", "High"])
    school_type_input = st.selectbox("🏫 School Type", ["Public", "Private"])  
    peer_influence = st.selectbox("👥 Peer Influence", ["Positive", "Neutral", "Negative"])
    physical_activity = st.number_input("🏃 Physical Activity ", min_value=0.0, max_value=30.0, value=5.0)
    learning_disabilities = st.selectbox("🧠 Learning Disabilities", ["Yes", "No"])
    parental_education_level = st.selectbox("🎓 Parental Education Level", ["High School", "College", "Postgraduate"])
    distance_from_home_input = st.selectbox("🚗 Distance from Home", ["Near", "Moderate", "Far"])
    gender = st.selectbox("⚧️ Gender", ["Male", "Female"])

    # Encoding input data
    encoded_data = {
        "Hours_Studied": hours_studied,
        "Attendance": attendance,
        "Parental_Involvement": parental[parental_involvement_input],
        "Access_to_Resources": access_to_resources[access_to_resources_input],
        "Extracurricular_Activities": extra_activity[extracurricular_activities],
        "Sleep_Hours": sleep_hours,
        "Previous_Scores": previous_scores,
        "Motivation_Level": motivational_level[motivation_level_input],
        "Internet_Access": internet[internet_access],
        "Tutoring_Sessions": tutoring_sessions,
        "Family_Income": family_income[family_income_input],
        "Teacher_Quality": teacher_quality[teacher_quality_input],
        "School_Type": school_type_encoding[school_type_input],  # Fixed reference
        "Peer_Influence": peer[peer_influence],
        "Physical_Activity": physical_activity,
        "Learning_Disabilities": disability[learning_disabilities],
        "Parental_Education_Level": parent_education[parental_education_level],
        "Distance_from_Home": distance[distance_from_home_input],
        "Gender": gender_mapping[gender],
    }

    input_df = pd.DataFrame([encoded_data])

    # Predict button
    if st.button("🔮 Predict"):
        predicted_score = predict_performance(input_df)
        if predicted_score is not None:
            st.success(f"📈 Predicted Exam Score: {predicted_score:.2f}")

if __name__ == '__main__':
    main()
