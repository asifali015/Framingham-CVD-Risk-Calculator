import math
# Framingham CVD Risk Calculator
print("Welcome to the Framingham CVD Risk Calculator")
print("Please answer the following questions to calculate your 10-year risk score. \n")
# Get user input
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")
smoker = input("Do you smoke? (yes/no): ")
diabetes = input("Do you have diabetes? (yes/no): ")
blood_pressure = int(input("Enter your systolic blood pressure (mmHg): "))
cholesterol = int(input("Enter your total cholesterol level (mg/dL): "))
hdl_cholesterol = int(input("What is your HDL cholesterol level? "))
# Framingham risk score calculator formula for men
def calculate_risk_score_men(age, total_cholesterol, hdl_cholesterol, systolic_bp, smoker):
 age_coef = 3.06117
 chol_coef = 1.12370
 hdl_coef = -0.93263
 bp_coef = 1.93303
 smoker_coef = 0.65451
 intercept = -30.7095
 log_age = math.log(age)
 log_cholesterol = math.log(total_cholesterol)
 log_hdl = math.log(hdl_cholesterol)
 risk_score = math.exp(intercept + (age_coef * log_age) + (chol_coef * log_cholesterol) +
(hdl_coef * log_hdl) + (bp_coef * math.log(systolic_bp)) + (smoker_coef * smoker))
 return round(100 * (1 - (0.9533 ** risk_score)), 2)
# Framingham risk score calculator formula for women
def calculate_risk_score_women(age, total_cholesterol, hdl_cholesterol, systolic_bp, smoker):
 age_coef = 2.32888
 chol_coef = 1.20904
 hdl_coef = -0.70833
 bp_coef = 2.76157
 smoker_coef = 0.52873
 intercept = -29.1866
 log_age = math.log(age)
 log_cholesterol = math.log(total_cholesterol)
 log_hdl = math.log(hdl_cholesterol)
 risk_score = math.exp(intercept + (age_coef * log_age) + (chol_coef * log_cholesterol) +
(hdl_coef * log_hdl) + (bp_coef * math.log(systolic_bp)) + (smoker_coef * smoker))
 return round(100 * (1 - (0.966 ** risk_score)), 2)
# Calculate the risk score based on the individual risk factors
if gender == "male":
 risk_score = calculate_risk_score_men(age, cholesterol, hdl_cholesterol, blood_pressure,
smoker == "yes")
else:
 risk_score = calculate_risk_score_women(age, cholesterol, hdl_cholesterol, blood_pressure,
smoker == "yes")
# Interpret the risk score and provide recommendations
print("Your 10-year risk of having a heart attack or stroke is:", risk_score, "%")
if risk_score < 10:
 print("Your risk is low. Continue to maintain a healthy lifestyle and regular check-ups with your doctor.")
elif risk_score >= 10 and risk_score < 20:
 print("Your risk is moderate. Consult with your doctor to develop a plan to manage your risk factors")
else:
 print("Your risk is high. Consult with your doctor immediately to develop a plan to manage your risk factors, which may include lifestyle changes and/or medication.")



