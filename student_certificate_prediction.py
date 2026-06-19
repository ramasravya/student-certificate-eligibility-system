import pandas as pd
from IPython.display import display

# Read attendance files
day1 = pd.read_csv("meetinglistdetails_2026_05_29_2026_05_29.csv")
day2 = pd.read_csv("meetinglistdetails_2026_05_30_2026_05_30.csv")

# Combine both datasets
attendance_data = pd.concat([day1, day2], ignore_index=True)

# Remove rows having missing values
attendance_data = attendance_data.dropna(
    subset=["Name (original name)", "Email"]
)

# Convert duration column into numeric
attendance_data["Duration (minutes).1"] = pd.to_numeric(
    attendance_data["Duration (minutes).1"],
    errors="coerce"
)

attendance_data["Duration (minutes).1"] = attendance_data[
    "Duration (minutes).1"
].fillna(0)

# Create report for each student
student_report = attendance_data.groupby(
    ["Name (original name)", "Email"]
).agg(
    Sessions_Attended=("Duration (minutes).1", "count"),
    Total_Attendance_Minutes=("Duration (minutes).1", "sum")
).reset_index()

# Rename columns
student_report.rename(
    columns={
        "Name (original name)": "Name"
    },
    inplace=True
)

# Calculate attendance percentage
max_minutes = student_report["Total_Attendance_Minutes"].max()

student_report["Attendance_Percentage"] = round(
    (student_report["Total_Attendance_Minutes"] / max_minutes) * 100,
    2
)

# Decide certificate eligibility
student_report["Certificate_Status"] = student_report[
    "Attendance_Percentage"
].apply(
    lambda x: "Eligible" if x >= 75 else "Not Eligible"
)

# Select final columns
final_report = student_report[
    [
        "Name",
        "Email",
        "Sessions_Attended",
        "Attendance_Percentage",
        "Certificate_Status"
    ]
]

# Display complete report
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

print("Total Students:", len(final_report))
display(final_report)

# Save report to csv file
final_report.to_csv(
    "Final_Student_Certificate_Report.csv",
    index=False
)

print("\nFinal report saved successfully.")
