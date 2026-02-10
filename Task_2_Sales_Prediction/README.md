# 📊 Sales Prediction Using Machine Learning (Linear Regression)
**OIBSIP – Task 2**

## 🧩 Problem Statement
Businesses invest heavily in advertising across multiple platforms such as **TV, Radio, and Newspapers**, but understanding how these investments translate into actual sales is critical for decision-making.  
The challenge is to **predict product sales** based on advertising expenditure and identify which channels contribute most to sales performance.

---

## 🎯 Objective
- Build a **machine learning model** to predict sales using advertising data  
- Understand the relationship between advertising spend and sales  
- Evaluate model performance using standard regression metrics  
- Interpret feature importance to support business decisions  

---

## 🗂️ Project Overview
This project uses a **Linear Regression model** to predict sales based on spending on:
- TV advertising
- Radio advertising
- Newspaper advertising  

The dataset contains historical advertising budgets and corresponding sales figures.  
The model learns patterns from this data to estimate future sales.

---

## 🔄 Workflow
1. **Exploratory Data Analysis (EDA)**
   - Checked dataset structure and summary statistics
   - Analyzed relationships between advertising channels and sales

2. **Data Preprocessing**
   - Removed unnecessary columns
   - Performed train–test split
   - Applied feature scaling where appropriate

3. **Model Training**
   - Trained a **Linear Regression** model on the training data

4. **Model Evaluation**
   - Evaluated performance using:
     - Mean Absolute Error (MAE)
     - Root Mean Squared Error (RMSE)
     - R² Score

5. **Visualization**
   - Plotted **Actual vs Predicted Sales** to assess model fit

---

## 📈 Results
| Metric | Value |
|------|------|
| MAE | 1.46 |
| RMSE | 1.78 |
| R² Score | 0.89 |

### Feature Importance
| Feature | Coefficient |
|-------|-------------|
| TV | High impact |
| Radio | Moderate impact |
| Newspaper | Very low impact |

- **TV advertising** has the strongest influence on sales  
- **Radio advertising** also contributes significantly  
- **Newspaper advertising** has minimal effect  

---

## ✅ Conclusion
The Linear Regression model achieved **strong predictive performance**, explaining nearly **89% of the variance** in sales.  
The analysis shows that focusing advertising budgets on **TV and Radio** is more effective than Newspaper advertising.

This project demonstrates:
- End-to-end regression modeling
- Business-driven interpretation of ML results
- Clear evaluation and visualization of model performance  

---

## 🛠️ Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 🚀 Future Improvements
- Try **Multiple Linear Regression diagnostics**
- Experiment with **Ridge and Lasso regression**
- Add **cross-validation**
- Extend to **non-linear models**

## 🙌 Acknowledgements
This project was completed as part of the **OIBSIP Internship Program**, with a focus on practical machine learning workflows and reproducible research.