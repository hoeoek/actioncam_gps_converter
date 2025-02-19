# ActionCam GPS Converter

This repository contains a Python script to convert GPS log data from Sony Action Cams into CSV format for use with QGIS or other applications.

## Features

- Converts NMEA GPS log data to CSV format.
- Supports Sony GPS log files.
- Outputs CSV with timestamp, latitude, longitude, and speed.


## Requirements

- Python 3.x

## Installation

Clone the repository:

```sh
git clone https://github.com/hoeoek/actioncam_gps_converter.git
```
Navigate to the repository directory:
```sh
cd actioncam_gps_converter
```

## Usage

To convert a Sony GPS log file to a CSV file, use the following command:

```sh
python sony_gps_to_qgis.py <input_file> [-o <output_file>]
```

## Arguments

- `<input_file>`: Path to the input Sony GPS log file.
- `-o, --output`: (Optional) Path to the output CSV file. If not provided, the output file will be named `<input_file>_converted.csv`.

## Example

```sh
python sony_gps_to_qgis.py example_log.txt -o output.csv
```
