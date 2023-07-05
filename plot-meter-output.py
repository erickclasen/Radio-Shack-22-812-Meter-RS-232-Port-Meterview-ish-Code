import matplotlib.pyplot as plt

filename = 'output.log'
readings = []
timestamps = []

with open(filename, 'r') as file:
    for line in file:
        parts = line.strip().split()
        reading_str = parts[2].lstrip('(\'').rstrip('\'')  # Remove the opening parenthesis and single quotation mark

        try:
            reading = float(reading_str)
            readings.append(reading)
            timestamps.append(' '.join(parts[:2]))  # Combine date and time strings
        except ValueError:
            # Ignore values that cannot be converted to float
            continue

plt.plot(range(len(readings)), readings)
plt.xlabel('Time')
plt.ylabel('Reading')
plt.title('Meter Readings')
plt.xticks(range(len(timestamps)), timestamps, rotation=45, fontsize=8)  # Set X-axis tick labels to timestamps

# Adjust the subplot parameters to add more whitespace below the X-axis labels
plt.subplots_adjust(bottom=0.35)

plt.show()
