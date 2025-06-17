# Multivariable Linear Regression

This project demonstrates a simple implementation of **Multiple Linear Regression** using Python and NumPy. The model predicts salaries based on multiple features like experience, test score, and interview score.

## 📁 Files

- `hiring.csv`  
  Dataset containing the input features and corresponding salaries.

- `multi_variable.py`  
  Python script that:
  - Reads the dataset
  - Handles missing data
  - Builds a multivariable linear regression model
  - Makes salary predictions for new candidates

## 🔧 Requirements

```bash
pip install numpy pandas

▶️ How to Run

python multi_variable.py

🧠 Concepts Covered
Multivariable input handling
Basic data preprocessing (NaN handling)
Linear regression using the Normal Equation
Salary prediction using learned weights

📌 Notes
This is a beginner-friendly example for understanding multivariable regression without external ML libraries.
For a full ML pipeline (splitting, scaling, evaluating), consider using scikit-learn.