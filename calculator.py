import streamlit as st

def get_gpa(marks, grading_scale):
    for grade_range, gpa in grading_scale.items():
        if marks in grade_range:
            return gpa
    return 0.0  # Default GPA for failing marks

def main():
    st.title("GPA Calculator")
    
    st.write("### Enter your marks for each subject")
    
    # Define grading scales
    theory_grading = {
        range(86, 101): 4.00, range(80, 86): 3.66, range(75, 80): 3.33,
        range(70, 75): 3.00, range(67, 70): 2.66, range(63, 67): 2.33,
        range(60, 63): 2.00, range(57, 60): 1.66, range(54, 57): 1.30,
        range(50, 54): 1.00, range(0, 50): 0.00
    }
    
    lab_grading = {
        range(43, 51): 4.00, range(40, 43): 3.66, range(38, 40): 3.33,
        range(35, 38): 3.00, range(33, 35): 2.66, range(31, 33): 2.33,
        range(30, 31): 2.00, range(28, 30): 1.66, range(26, 28): 1.30,
        range(25, 26): 1.00, range(0, 25): 0.00
    }
    
    # Subject list with credit hours
    subjects = {
        "AICT Theory": (st.number_input("AICT Theory Marks", min_value=0, max_value=100, value=0), 2, theory_grading),
        "AICT Lab": (st.number_input("AICT Lab Marks", min_value=0, max_value=50, value=0), 1, lab_grading),
        "PF Theory": (st.number_input("PF Theory Marks", min_value=0, max_value=100, value=0), 2, theory_grading),
        "PF Lab": (st.number_input("PF Lab Marks", min_value=0, max_value=50, value=0), 1, lab_grading),
        "Linear Algebra": (st.number_input("Linear Algebra Marks", min_value=0, max_value=100, value=0), 3, theory_grading),
        "Discrete Maths": (st.number_input("Discrete Maths Marks", min_value=0, max_value=100, value=0), 3, theory_grading),
        "Functional English": (st.number_input("Functional English Marks", min_value=0, max_value=100, value=0), 3, theory_grading),
        "Pak Studies": (st.number_input("Pak Studies Marks", min_value=0, max_value=100, value=0), 2, theory_grading),
    }
    
    total_gpa = 0
    total_credits = 0
    
    for subject, (marks, credits, grading_scale) in subjects.items():
        subject_gpa = get_gpa(marks, grading_scale)
        total_gpa += subject_gpa * credits
        total_credits += credits
    
    if total_credits > 0:
        gpa = total_gpa / total_credits
        st.write(f"### Your GPA: {gpa:.2f}")
    else:
        st.write("### Please enter valid marks to calculate GPA.")

if __name__ == "__main__":
    main()
