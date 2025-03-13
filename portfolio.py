#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Title and Introduction
st.title("🚀 PANCHANGAM RAMYA SHRUTHI - Data Science Portfolio")

st.write("""
✉️ ramyashruthi2001@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ramya-shruthi)  
🔗 [GitHub](https://github.com/Ramya-Shruthi)  
""")

# Summary
st.header("💡 Summary")
st.write(
"""
🎯 **Aspiring Data Scientist | Passionate About Data & AI**  

I am a highly motivated **Data Science enthusiast** with a strong foundation in **Python, SQL, and Machine Learning**.  
I love working with data—analyzing it, uncovering insights, and building models to solve **real-world challenges**.  

Currently, I am enhancing my skills through **hands-on projects** in **data analysis, visualization, and predictive modeling**.  
My goal is to **leverage data-driven solutions** to create meaningful impact in the industry.""")

# Skills
st.header("🛠️ Skills")
skills = [
    "Python (Pandas, NumPy, Scikit-Learn)",
    "SQL (MySQL)",
    "EDA & Feature Engineering",
    "Regression & Classification",
    "Data Visualization (Tableau, Power BI, Matplotlib, Seaborn)",
    "Development Tools: Jupyter Notebook, Google Colab, VS Code",
    "Soft Skills: Problem-Solving, Team Collaboration, Attention to Detail"
]
st.write(" | ".join(skills))

# Education
st.header("🎓 Education")
st.write("""
- **Great Lakes Institute of Management** (2024-2025)  
  *PGP in Data Science and Engineering*  
- **DRK Institute of Science and Technology** (2019-2023)  
  *Bachelor of Technology in Computer Science*  
""")

# Projects Section
st.header("📊 Projects")

st.subheader("1️Predictive Analytics for Health Camp Engagement")
st.write("""
- **Tools:** Python, Pandas, SQL, Gradient Boosting  
- **Overview:** Built a data processing pipeline and predictive model to improve patient participation.  

""")

st.subheader(" Food Demand Forecasting")
st.write("""
- **Tools:** Python, SQL, Random Forest  
- **Overview:** Developed a forecasting model for meal demand, automating preprocessing and improving accuracy.  
- **GitHub:** [View Code](https://github.com/Ramya-Shruthi/Food-Demand-Forecasting)
""")

st.subheader(" BigMart Sales Prediction")
st.write("""
- **Tools:** Python, XGBoost, Feature Engineering  
- **Overview:** Forecasted store sales using historical data with engineered features for better accuracy.  
- **GitHub:** [View Code](https://github.com/Ramya-Shruthi/BigMart-Sales)
""")

# Certifications
st.header("📜 Certifications")
certifications = [
    "📌 Microsoft Power BI Data Analyst (PL-300) - Pursuing",
    "📌 SQL (HackerRank Certified - Intermediate Level) - Oct 2024",
    "📌 Introduction to Artificial Intelligence - Dec 2024"
]
st.write("\n".join(certifications))

# Languages
st.header("🌎 Languages")
st.write("**English | Hindi | Telugu**")

# Contact Section
st.header("📬 Contact Me")
st.write(""" 
✉️ **Email:** ramyashruthi2001@gmail.com  
🔗 **LinkedIn:** [Connect with me](https://www.linkedin.com/in/ramya-shruthi)  
🔗 **GitHub:** [Check my projects](https://github.com/Ramya-Shruthi) 
🔗 [LeetCode](https://leetcode.com/u/Ramya_Shruthi/) 
""")

