# ML_salary_prediction
# Predicting Employee Salary Using Candidate Analytics

This Streamlit application leverages a linear regression model to estimate employee salaries based on their experience (in years), test scores (out of 10), and interview scores (out of 10). It's designed to assist in analyzing candidate data for recruitment purposes.

## Key Features

* Reads and processes employee data from a CSV file.
* Displays both raw and preprocessed data.
* Handles missing values strategically.
* Trains a linear regression model for salary prediction.
* Provides a user interface for entering candidate information.
* Presents the predicted salary in a clear and concise format.

## Libraries Used

* streamlit: Streamlit for building interactive web apps.
* streamlit_shadcn_ui: Streamlit component for enhanced tables.
* pandas: Data manipulation and analysis library.
* sklearn: Machine learning library, specifically linear_model for regression.
* math: Used for mathematical operations like flooring (rounding down).

## Instructions

1. **Install Dependencies:**

```bash
pip install streamlit streamlit-shadcn-ui pandas sklearn
```

2. Run the App

```bash
streamlit run main.py
```
