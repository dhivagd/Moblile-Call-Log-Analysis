# Moblile-Call-Log-Analysis
This project allows users to analyze their mobile call log data in various ways, including tracking the call duration, call frequency, and distribution of calls between different contacts or parties. The analysis is visualized using pie charts for call distribution and line graphs for call duration trends over time. The application is built with Flask for the backend, HTML/CSS for the frontend, and Python for data processing and visualization.


Table of Contents

    Project Overview
    Features
    Technologies Used
    Setup and Installation
    How to Use
    File Format
    Contributing
    License

Project Overview

The Mobile Call Log Analysis project helps analyze call logs in the form of a CSV file. It uses Python libraries such as Pandas and Matplotlib to process and visualize the data. The main features include:

    Call Duration Analysis: A time-series plot showing total call duration over a specified period (e.g., September to November).
    Call Distribution Analysis: Pie charts representing the distribution of calls between the user and different parties, based on the number of calls made.

Features

    CSV Upload: Allows users to upload their call log CSV file.
    Call Duration Analysis: Visualizes call duration over time (with a line graph).
    Call Distribution by Party: Displays a pie chart showing the number of calls made to each party.
    Frontend: Responsive web interface built using HTML/CSS and JavaScript (Chart.js).
    Backend: Python Flask framework to handle file upload, data processing, and visualization generation.

Technologies Used

    Backend: Flask (Python)
    Frontend: HTML, CSS, JavaScript (Chart.js)
    Data Processing: Pandas, Numpy
    Data Visualization: Matplotlib
    File Format: CSV

Setup and Installation
Prerequisites

    Python 3.x installed
    Pip (Python package manager)

Steps to Set Up

    Clone the repository:

git clone https://github.com/yourusername/Mobile-Call-Log-Analysis.git
cd Mobile-Call-Log-Analysis

Install dependencies:

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # For Windows, use 'venv\Scripts\activate'

Install the required Python libraries:

pip install -r requirements.txt

Run the Flask app:

After installing dependencies, run the Flask app:

python app.py

The app will start running locally at http://127.0.0.1:5000/.

Access the App:

Open a browser and go to http://127.0.0.1:5000/ to access the call log analysis tool.
