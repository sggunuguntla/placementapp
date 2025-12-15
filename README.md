Placement Eligibility Streamlit Application
Project Overview
The Placement Eligibility Streamlit Application is an interactive EdTech dashboard developed using Python and Streamlit.
It enables placement teams to filter and shortlist eligible students based on programming performance, soft skills, and placement readiness.
The application provides real-time results using a simple and intuitive UI without requiring any frontend technologies such as HTML, CSS, or JavaScript.

Problem Statement
In EdTech platforms, placement teams often manage hundreds of students.
Manually checking eligibility based on multiple criteria is time-consuming and inefficient.

This project automates the eligibility filtering process, allowing placement teams to make quick and accurate decisions using an interactive dashboard.

Technologies Used
Python
Streamlit – Interactive dashboard development
Pandas – Data loading, merging, and filtering
CSV Files – Structured data storage

Project Folder Structure
placementapp/
1.app.py                  # Main Streamlit application
2.placementapp.ipynb      # Data preparation & testing notebook
3.students.csv            # Student master data
4.programming.csv         # Programming performance data
5.soft_skills.csv         # Soft skills evaluation data
6.placements.csv          # Placement readiness data
7.Placement_Eligibility_Streamlit_Application_Documentation_Final.docx

Dataset Description

1.students.csv
Contains basic student information:
Student name
Age and gender
Contact details
Enrollment year and batch
Graduation year

2.programming.csv
Stores programming performance metrics:
Programming language
Problems solved
Assessments completed
Mini projects
Certifications earned
Latest project score

3.soft_skills.csv
Contains soft skill evaluation scores (out of 100):
Communication
Teamwork
Presentation
Leadership
Critical thinking
Interpersonal skills

4️.placements.csv
Stores placement readiness and outcome details:
Mock interview score
Internships completed
Placement status (Ready / Not Ready / Placed)
Company name
Placement package
Placement date

All datasets are linked using a common key: student_id

Application Workflow
CSV files are loaded using Pandas
All datasets are merged using student_id
User selects eligibility criteria from the Streamlit sidebar
Data is filtered dynamically based on inputs

Eligible students are displayed instantly

Key Features

Interactive Streamlit dashboard

Sidebar-based eligibility filters

Real-time student eligibility results

Clean and user-friendly UI

Fast prototyping using CSV datasets

How to Run the Application
Step 1: Install dependencies
pip install streamlit pandas

Step 2: Navigate to the project folder
cd placementapp

Step 3: Run the Streamlit application
python -m streamlit run app.py

Step 4: Open in browser
http://localhost:8501

Eligibility Criteria (Sample)

Minimum number of problems solved

Minimum communication score

Placement status (Ready / Placed)

Students meeting the selected criteria are displayed as eligible.

Learning Outcomes

Built an interactive dashboard using Streamlit

Worked with multiple datasets using Pandas

Applied real-world eligibility filtering logic

Understood EdTech placement workflows

Improved project structuring and documentation skills

Challenges Faced & Solutions

Streamlit command not recognized
→ Resolved using python -m streamlit

Environment mismatch issues
→ Installed dependencies in the correct Python environment

Notebook vs script confusion
→ Separated .ipynb and .py files properly
Future Enhancements
Add charts and KPI visualizations
Export eligible students list to CSV

Integrate SQLite or MySQL database

Deploy the application on Streamlit Cloud
Conclusion

The Placement Eligibility Streamlit Application demonstrates how Python, Pandas, and Streamlit can be combined to build a practical, real-world EdTech solution for placement eligibility analysis with dynamic filtering and real-time insights.
