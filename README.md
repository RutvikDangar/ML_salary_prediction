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

3. Interact with the App
   
* Enter years of experience, test score (out of 10), and interview score (out of 10) in the designated fields.
* Table will Display the entered inputs and estimated salary.

## Code Structure

The code is organized into three main sections:

1. Data Loading and Cleaning

  * Loads employee data from "hiring.csv" located in the "Predicting_Salary" directory.
  * Renames data columns for clarity.
  * Replaces "zero" in the experience column with 0 (years).
  * Handles missing test scores by imputing the average score.
    
2. Model Training

  * Trains a linear regression model using experience (years), test score, and interview score as features to predict salary.
  * Displays the model's regression coefficients for insights.
    
3. Prediction and User Interface

  * Defines functions for predicting salary based on user input.
  * Creates a user-friendly interface with Streamlit components to enter candidate information.
  * Presents the predicted salary along with experience, test score, and interview score in a formatted table.

## Additional Notes

  * Custom CSS styling is included in a separate file "style.css" for visual enhancements.

```I hope this is helpful!```

