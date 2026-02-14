# 🚗 Task 3: Car Price Prediction using Machine Learning

**OIBSIP – Task 2**

# 📌 Problem Statement

Accurately predicting the selling price of used cars is crucial for sellers, buyers, and dealerships. The objective of this task is to build and validate regression models that can predict the resale value of cars based on features such as present price, car age, fuel type, transmission type, ownership history, and kilometers driven.

The goal is to identify the most stable, accurate, and interpretable model for predicting car selling prices.

---

# 🎯 Objective

- Build multiple regression models for price prediction.

- Compare performance using evaluation metrics (MAE, RMSE, R²).

- Apply log transformation to handle skewness in the target variable.

- Perform model validation using:

     - *Cross-validation*

     - *Train vs Test comparison*

     - *Residual analysis*

- Select the best-performing and most interpretable final model.

---

# 📊 Project Overview

During experimentation, the following models were evaluated:

*Linear Regression*

*Ridge Regression*

*Lasso Regression*

(Tree-based models were initially tested but removed due to overfitting)

After analysis, it was observed that the target variable (Selling Price) was positively skewed. Applying a log transformation significantly improved model performance and stability.

Therefore, validation focused primarily on **log-transformed models**.

---

# 🔄 Workflow

1️⃣ Data Preprocessing

- Handled categorical variables using encoding.

- Scaled numerical features.

- Split dataset into training and testing sets.

- Applied log transformation to the target variable.

2️⃣ Model Training

Trained:

*Log Linear Regression*

*Log Ridge Regression*

*Log Lasso Regression*

3️⃣ Model Validation

✅ Cross-Validation

- Compared mean R² and standard deviation across folds.

- Ensured model stability and consistency.

✅ Train vs Test Comparison

- Checked for overfitting.

- Verified bias-variance balance.

✅ Evaluation Metrics

Measured:

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

- R² Score

✅ Diagnostic Analysis

- Actual vs Predicted plot

- Residual plot analysis

- Coefficient interpretation (feature importance)

---

# 📈 Results

🔹 *Best Performing Model*

# Log-Transformed Linear Regression

🔹 **Performance Metrics (Test Set)**

- R² ≈ 0.93

- Lowest RMSE

- Lowest MAE

Train R² ≈ Test R² → No overfitting

🔹 **Residual Analysis**

- Residuals centered around zero

- No clear non-linear pattern

- Mostly constant variance

- Minor underprediction for extreme high-value cars

🔹 **Key Feature Insights**

- Present Price → Strongest positive predictor

- Selling Type (Individual) → Significant negative impact

- Car Age → Depreciates resale value

- Diesel fuel type slightly increases value

- Manual transmission slightly reduces price

- Driven kilometers and number of owners have smaller effects

---

# 🏆 Conclusion

After evaluating multiple regression models, the Log-Transformed Linear Regression model was selected as the final model due to:

- Highest predictive performance (R² ≈ 0.93)

- Strong generalization ability

- No evidence of overfitting

- Clean residual behavior

- High interpretability

The log transformation improved linearity and corrected skewness in the target variable, allowing a simple linear model to outperform more complex alternatives.

This model provides both strong predictive accuracy and meaningful business insights, making it suitable for real-world resale price estimation.

---

# 📌 Final Takeaway

Sometimes, a properly transformed simple model can outperform complex models.
Model selection should balance performance, stability, and interpretability.

---

# 🛠️ Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 🙌 Acknowledgements
This project was completed as part of the **OIBSIP Internship Program**, with a focus on practical machine learning workflows and reproducible research.