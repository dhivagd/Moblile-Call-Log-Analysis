import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random call log data
def generate_call_log_data(num_rows=200, file_name="call_log_sample.csv"):
    users = ["User1", "User2", "User3", "User4", "User5"]
    parties = ["Party1", "Party2", "Party3", "Party4", "Party5"]
    directions = [0, 1]  # 0 for incoming, 1 for outgoing
    start_date = datetime(2024, 9, 1)
    end_date = datetime(2024, 11, 30)
    
    call_logs = []

    for _ in range(num_rows):
        user = random.choice(users)
        party = random.choice(parties)
        direction = random.choice(directions)
        
        # Random call duration between 1 minute and 15 minutes
        minutes = random.randint(1, 15)
        duration = f"{minutes}:00"
        
        # Random date within the range (September-November 2024)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        date_str = random_date.strftime("%Y-%m-%d")
        
        call_logs.append([user, party, duration, direction, date_str])

    # Create DataFrame and save to CSV
    df = pd.DataFrame(call_logs, columns=["User", "Party", "Duration", "Direction", "Date"])
    df.to_csv(file_name, index=False)
    print(f"Sample CSV file {file_name} generated successfully!")

# Generate 3 different CSV files with different data
generate_call_log_data(200, "call_log_sample_1.csv")
generate_call_log_data(200, "call_log_sample_2.csv")
generate_call_log_data(200, "call_log_sample_3.csv")
