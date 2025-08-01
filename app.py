import streamlit as st
import mysql.connector
import pandas as pd
 
# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="S@nthosh107",
    database="placement_app_db"
)
 
 
# Streamlit UI
st.title("🎓 Placement Eligibility Checker")
 
# Sidebar filters
st.sidebar.header("Eligibility Criteria")
min_problems = st.sidebar.slider("Minimum Problems Solved", 0, 1000, 240)
min_communication = st.sidebar.slider("Minimum Communication Score", 0, 100, 75)
 
# SQL query
query = f"""
SELECT s.student_id, s.name, p.problems_solved, ss.communication, pl.placement_status
FROM students s
JOIN programming p ON s.student_id = p.student_id
JOIN soft_skills ss ON s.student_id = ss.student_id
JOIN placements pl ON s.student_id = pl.student_id
WHERE p.problems_solved >= {min_problems}
AND ss.communication >= {min_communication}
"""
 
df = pd.read_sql(query, connection)
 
# Display eligible students
st.subheader("📋 Eligible Students")
st.dataframe(df)
st.header("📄 Full Student Profiles")
st.header("📄 Full Student Profiles")
 
query = """
SELECT 
    s.student_id,
    s.name,
    s.age,
    s.gender,
    s.email,
    s.phone,
    s.enrollment_year,
    s.course_batch,
    s.city,
    s.graduation_year,
 
    p.language,
    p.problems_solved,
    p.assessments_completed,
    p.mini_projects,
    p.certifications_earned,
    p.latest_project_score,
 
    ss.communication,
    ss.teamwork,
    ss.presentation,
    ss.leadership,
    ss.critical_thinking,
    ss.interpersonal_skills,
 
    pl.mock_interview_score,
    pl.internships_completed,
    pl.placement_status,
    pl.company_name,
    pl.placement_package,
    pl.interview_rounds_cleared,
    pl.placement_date
 
FROM students s
LEFT JOIN programming p ON s.student_id = p.student_id
LEFT JOIN soft_skills ss ON s.student_id = ss.student_id
LEFT JOIN placements pl ON s.student_id = pl.student_id
"""
 
 
df_full = pd.read_sql(query, connection)
st.dataframe(df_full)
 
 
#  SQL-Based Insights Section
 
st.header(" SQL-Based Insights")
 
# 1. Count how many students are there
query1 = "SELECT COUNT(*) AS count FROM students"
result1 = pd.read_sql(query1, connection)
st.write(" Total students:", int(result1['count'][0]))
 
# 2. Count how many placement records are there
query2 = "SELECT COUNT(*) AS count FROM placements"
result2 = pd.read_sql(query2, connection)
st.write(" Total placement records:", int(result2['count'][0]))
 
# 3. Count how many programming records are there
query3 = "SELECT COUNT(*) AS count FROM programming"
result3 = pd.read_sql(query3, connection)
st.write(" Total programming records:", int(result3['count'][0]))
 
# 4. Show cities of students
query4 = "SELECT city FROM students LIMIT 5"
result4 = pd.read_sql(query4, connection)
st.write(" Example student cities:")
st.table(result4)
 
# 5. List student names and emails
query5 = "SELECT name, email FROM students LIMIT 5"
result5 = pd.read_sql(query5, connection)
st.write(" First 5 student names and emails:")
st.table(result5)
 
# 6. List student names and phone numbers
query6 = "SELECT name, phone FROM students LIMIT 5"
result6 = pd.read_sql(query6, connection)
st.write(" Student Names and Phones:")
st.table(result6)
 
# 7. Show names of students who are placed (limit 5)
query7 = "SELECT student_id, company_name FROM placements WHERE placement_status = 'Placed' LIMIT 5"
result7 = pd.read_sql(query7, connection)
st.write(" Placed Students (sample):")
st.table(result7)
 
# 8. Show a few programming languages students used
query8 = "SELECT DISTINCT language FROM programming LIMIT 5"
result8 = pd.read_sql(query8, connection)
st.write(" Programming Languages Used:")
st.table(result8)
 
# 9. Show student names and graduation years
query9 = "SELECT name, graduation_year FROM students LIMIT 5"
result9 = pd.read_sql(query9, connection)
st.write(" Graduation Years of Students:")
st.table(result9)
 
# 10. Show student names and number of problems solved
query10 = "SELECT s.name, p.problems_solved FROM students s JOIN programming p ON s.student_id = p.student_id LIMIT 5"
result10 = pd.read_sql(query10, connection)
st.write(" Problems Solved by Students (sample):")
st.table(result10)