import streamlit as st
from datetime import datetime, timedelta


# Function to display a reminder for the next period
def display_reminder(current_day, current_time, timetable):
    # Logic to find the next period
    # You need to adjust this based on your timetable structure
    next_period = find_next_period(current_day, current_time, timetable)

    # Display reminder message
    if next_period:
        st.info(f"Next period: {next_period} will start soon. Be prepared!")


# Function to find the next period based on current day and time
def find_next_period(current_day, current_time, timetable):

 def main():
    st.title("College Timetable App")

    # Get user input for the number of subjects
    num_subjects = st.number_input("Enter the number of subjects:", min_value=1, value=5)

    # Initialize timetable
    timetable = {day: {} for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

    # Input subjects and hours for each day
    for day in timetable:
        st.header(f"{day}'s timetable")
        for i in range(1, num_subjects + 1):
            subject_name = st.text_input(f"Subject {i}:", f"Subject {i}")
            hours = st.number_input(f"Hours for {subject_name} on {day}:", min_value=1, value=1)

            timetable[day][subject_name] = hours

    # Get current day and time
    current_day = datetime.now().strftime("%A")
    current_time = st.time_input("Current time:", value=datetime.now().time())

    # Display reminder for the next period
    display_reminder(current_day, current_time, timetable)


