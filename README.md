# Moblile-Call-Log-Analysis
This project allows users to analyze their mobile call log data in various ways, including tracking the call duration, call frequency, and distribution of calls between different contacts or parties. The analysis is visualized using pie charts for call distribution and line graphs for call duration trends over time. The application is built with Flask for the backend, HTML/CSS for the frontend, and Python for data processing and visualization.


Table of Contents:-

    Project Overview
    Features
    Technologies Used
    Installation
    How to Use
    File Format
    Sample Output

Project Overview:-

The Mobile Call Log Analysis project helps analyze call logs in the form of a CSV file. It uses Python libraries such as Pandas and Matplotlib to process and visualize the data. The main features include:

    Call Duration Analysis: A time-series plot showing total call duration over a specified period (e.g., September to November).
    Call Distribution Analysis: Pie charts representing the distribution of calls between the user and different parties, based on the number of calls made.

Features:-

    CSV Upload: Allows users to upload their call log CSV file.
    Call Duration Analysis: Visualizes call duration over time (with a line graph).
    Call Distribution by Party: Displays a pie chart showing the number of calls made to each party.
    Frontend: Responsive web interface built using HTML/CSS and JavaScript (Chart.js).
    Backend: Python Flask framework to handle file upload, data processing, and visualization generation.

Technologies Used:-

    Backend: Flask (Python)
    Frontend: HTML, CSS, JavaScript (Chart.js)
    Data Processing: Pandas, Numpy
    Data Visualization: Matplotlib
    File Format: CSV

Installation:-
Prerequisites:-

    Python 3.x installed
    Pip (Python package manager)

How to Use:-

    Upload Your Call Log CSV:
        On the homepage of the app, you will find an option to upload your call log file. The file must be in CSV format.
        The CSV file should contain the following columns: User, Party, Duration, Direction, and Date.

    Analyze the Data:
        After uploading the file, the backend will process the data and generate:
            A pie chart showing the distribution of calls between the user and various parties.
            A line graph displaying the total call duration over time for a specified date range (e.g., from September to November).

    Visualize the Results:
        The pie charts will show how many calls the user made to each party.
        The line graph will show the daily total call duration, helping you analyze trends in your call activity.

File Format:-

Your CSV file should have the following columns:
Column	Description
User	The name or ID of the user whose calls are being logged (e.g., "User1").
Party	The name or ID of the party that the user called (e.g., "Party1").
Duration	The duration of the call in minutes and seconds (e.g., "5:30" for 5 minutes and 30 seconds).
Direction	The direction of the call: 0 for incoming calls, 1 for outgoing calls.
Date	The date the call occurred, in the format YYYY-MM-DD (e.g., "2024-09-01").

Sample Output:-

![WhatsApp Image 2024-12-17 at 19 14 12_09eafcf5](https://github.com/user-attachments/assets/4817480e-72c9-4800-a3de-24638499ba5b)


  

