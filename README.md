# Student Performance Prediction

A Streamlit app that predicts a student's exam score from study habits and background factors, using a Support Vector Regression model.

## Inputs

The model uses 19 factors, including:

- **Study habits:** hours studied, attendance, tutoring sessions, previous scores
- **Wellbeing:** sleep hours, physical activity, motivation level
- **Environment:** parental involvement, access to resources, internet access, family income, teacher quality, school type, peer influence, distance from home
- **Background:** parental education level, learning disabilities, gender

## Model

- Support Vector Regression (RBF kernel) from scikit-learn, with hyperparameters chosen by grid search with 5-fold cross-validation.
- Trained on the Student Performance Factors dataset (`StudentPerformanceFactors.csv`).
- Training code is in `student-performance-using-svm.ipynb`; the trained model is saved as `studentperf.pkl`.

## Tech stack

Python, scikit-learn, pandas, Streamlit, joblib

## Run locally

```bash
git clone https://github.com/Ankur377823/studentperformance.git
cd studentperformance
pip install -r requirements.txt
streamlit run studentop.py
```

## Project structure

| File | Purpose |
|---|---|
| `studentop.py` | Streamlit interface, input encoding and prediction |
| `student-performance-using-svm.ipynb` | Data preparation and model training |
| `StudentPerformanceFactors.csv` | Dataset |
| `studentperf.pkl` | Trained model |
| `requirements.txt` | Python dependencies |
