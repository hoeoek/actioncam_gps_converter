import csv
import argparse
from datetime import datetime

# Function to convert NMEA coordinates from DDDMM.MMMM format to decimal degrees
def nmea_to_decimal(degrees, direction):
    d = float(degrees[:2])
    m = float(degrees[2:]) / 60
    decimal = d + m
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def parse_gprmc_line(line):
    parts = line.split(',')
    return {
        'time': parts[1],
        'latitude': nmea_to_decimal(parts[3], parts[4]),
        'longitude': nmea_to_decimal(parts[5], parts[6]),
        'speed': parts[7],
        'date': parts[9]
    }

def convert_sony_log_to_csv(input_file, output_file):
    with open(input_file, "r") as file:
        log_content = file.readlines()

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Latitude', 'Longitude', 'Speed (knots)'])

        for line in log_content:
            if line.startswith('$GPRMC'):
                data = parse_gprmc_line(line)
                timestamp = datetime.strptime(f"{data['date']} {data['time']}", "%d%m%y %H%M%S.%f")
                writer.writerow([
                    timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    data['latitude'],
                    data['longitude'],
                    data['speed']
                ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Sony GPS log to CSV')
    parser.add_argument('input_file', help='Input Sony GPS log file')
    parser.add_argument('-o', '--output', help='Output CSV file (default: <input_file>_converted.csv)')
    args = parser.parse_args()

    input_sony_log = args.input_file
    if args.output:
        output_csv_path = args.output
    else:
        output_csv_path = f"{input_sony_log.rsplit('.', 1)[0]}_converted.csv"

    convert_sony_log_to_csv(input_sony_log, output_csv_path)
    print(f"Conversion complete. Output file: {output_csv_path}")
