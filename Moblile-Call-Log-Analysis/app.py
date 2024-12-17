from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import random
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle the CSV file upload
@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Process the uploaded CSV file
        try:
            df = pd.read_csv(filename)
            # Check if required columns exist
            if all(col in df.columns for col in ['User', 'Party', 'Duration', 'Direction', 'Date']):
                user_data = analyze_call_log(df)
                plot_call_duration_over_time(df)
                return jsonify(user_data)
            else:
                return "Invalid CSV format, missing required columns", 400
        except Exception as e:
            return f"Error processing file: {e}", 500
    else:
        return "Invalid file format. Only CSV files are allowed.", 400

# Function to analyze call logs (for pie charts)
def analyze_call_log(df):
    # Group data by User and Party
    grouped = df.groupby(['User', 'Party']).size().reset_index(name='Total_Calls')

    # Prepare data for pie charts
    user_data = {}
    for user in df['User'].unique():
        user_group = grouped[grouped['User'] == user]
        user_data[user] = {
            "labels": user_group['Party'].tolist(),
            "values": user_group['Total_Calls'].tolist()
        }

    return user_data

# Function to plot call duration over time
def plot_call_duration_over_time(df):
    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Calculate call duration in seconds
    df['Duration_seconds'] = df['Duration'].apply(lambda x: sum(int(i) * 60**(1 - idx) for idx, i in enumerate(x.split(':'))))

    # Group by Date and sum the durations
    daily_duration = df.groupby('Date')['Duration_seconds'].sum().reset_index()

    # Filter for September to November
    start_date = datetime(2024, 9, 1)
    end_date = datetime(2024, 11, 30)
    daily_duration = daily_duration[(daily_duration['Date'] >= start_date) & (daily_duration['Date'] <= end_date)]

    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(daily_duration['Date'], daily_duration['Duration_seconds'], marker='o', color='b', linestyle='-', linewidth=1, markersize=5)
    plt.title('Call Duration Analysis Over Time', fontsize=14)
    plt.xlabel('Days (September to November)', fontsize=12)
    plt.ylabel('Duration (sec)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image
    plot_path = os.path.join(app.config['UPLOAD_FOLDER'], 'call_duration_analysis.png')
    plt.savefig(plot_path)
    plt.close()

    # Return the path to the image
    return plot_path

# Route to serve the generated graph
@app.route("/graph")
def graph():
    plot_path = os.path.join(app.config['UPLOAD_FOLDER'], 'call_duration_analysis.png')
    return send_file(plot_path)

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
