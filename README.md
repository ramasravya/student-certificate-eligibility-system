# Student Certificate Eligibility System

This project automates the process of generating certificate eligibility reports from attendance records. It combines attendance data from multiple sessions, calculates attendance percentages, and determines whether students are eligible for certificates based on a predefined attendance threshold.

## Features

* Combines attendance records from multiple sessions
* Cleans and preprocesses attendance data
* Calculates total attendance duration
* Generates attendance percentages
* Determines certificate eligibility automatically
* Exports the final report as a CSV file

## Technologies Used

* Python
* Pandas
* IPython

## Dataset

The project uses attendance reports exported from online meeting platforms. Multiple attendance files are merged and processed to generate a final certificate eligibility report.

## Working

1. Load attendance CSV files
2. Merge attendance records
3. Remove incomplete entries
4. Calculate total attendance duration for each student
5. Compute attendance percentage
6. Mark students as Eligible or Not Eligible
7. Export the final report to CSV

## Output

The generated report contains:

* Student Name
* Email Address
* Sessions Attended
* Attendance Percentage
* Certificate Status

## Future Enhancements

* Web-based dashboard
* Automated report generation
* Email notification system
* Database integration
