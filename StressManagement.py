import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Simulating Real-Time Data Collection
def simulate_heart_rate():
    return random.randint(60, 120)  # Simulated heart rate between 60-120 BPM

def simulate_stress_level():
    return random.uniform(0, 10)  # Simulated stress level (0 to 10)

def get_user_input():
    # Simulate user input for mood
    return random.choice(['Calm', 'Stressed', 'Anxious'])

# Stress Detection Function
def detect_stress_level(heart_rate, stress_score):
    if heart_rate > 100 or stress_score > 7:
        return "High Stress"
    elif heart_rate > 85 or stress_score > 4:
        return "Moderate Stress"
    else:
        return "Low Stress"

# Stress Management Suggestions
def stress_management_suggestions(stress_level):
    if stress_level == "High Stress":
        return "Take deep breaths, meditate, or go for a walk."
    elif stress_level == "Moderate Stress":
        return "Try stretching or listen to calming music."
    else:
        return "Great job! Keep up your balanced routine."

# Real-Time Monitoring Simulation
def real_time_monitoring(duration=60):
    heart_rate_data = []
    stress_score_data = []
    time_data = []

    try:
        for i in range(duration):
            # Simulate data
            heart_rate = simulate_heart_rate()
            stress_score = simulate_stress_level()
            user_mood = get_user_input()

            # Detect stress level
            stress_level = detect_stress_level(heart_rate, stress_score)

            # Get stress management suggestions
            suggestion = stress_management_suggestions(stress_level)

            # Print the results
            print(f"Time: {i+1} minute(s)")
            print(f"Heart Rate: {heart_rate} BPM")
            print(f"Stress Score: {stress_score:.2f}")
            print(f"Detected Stress Level: {stress_level}")
            print(f"User Mood: {user_mood}")
            print(f"Suggestion: {suggestion}\n")
            
            # Store data for visualization
            heart_rate_data.append(heart_rate)
            stress_score_data.append(stress_score)
            time_data.append(i + 1)

            # Wait for 1 minute before the next reading (simulated)
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    
    # Plotting Stress Data (Optional for Hackathon Presentation)
    plt.figure(figsize=(10, 6))
    plt.plot(time_data, heart_rate_data, label="Heart Rate (BPM)", color="blue")
    plt.plot(time_data, stress_score_data, label="Stress Score", color="red", linestyle='dashed')
    plt.xlabel('Time (Minutes)')
    plt.ylabel('Value')
    plt.title('Real-Time Stress Monitoring')
    plt.legend(loc="upper left")
    plt.show()

# Start Real-Time Monitoring (Duration in minutes)
if __name__ == "__main__":
    print("Starting stress monitoring...\n")
    real_time_monitoring(duration=10)  # Simulate 10 minutes of monitoring
