# Data Analytics Project

This project demonstrates data analytics capabilities by fetching and processing different types of data files (CSV, JSON, Excel, and Text). It includes modules for both fetching data from various sources and processing them to generate meaningful insights.

## Project Structure

```
├── requested_data/        # Directory for storing fetched data files
├── data_processed/        # Directory for storing analysis results
├── logs/                  # Directory for log files
├── teja_get_*.py          # Data fetching modules
├── teja_process_*.py      # Data processing modules
├── utils_logger.py        # Logging utility
└── teja_run_all.py        # Script to run all operations
```

## Features

- **CSV Data Analysis**: Processes Airline Safety Report data
- **JSON Data Analysis**: Tracks ISS (International Space Station) location
- **Excel Data Analysis**: Processes 'LLC' count in data
- **Text Data Analysis**: Analyzes text content 
- **Logging**: Comprehensive logging system for tracking operations
- **Modular Design**: Separate modules for fetching and processing each data type

## Requirements

```pip
pandas
plotly
palmerpenguins
ipydatagrid
requests
openpyxl
loguru
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vnallam09/datafun-03-analytics.git
   cd datafun-03-analytics
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

### Individual Module Execution

1. Fetch data:
   ```bash
   python teja_get_csv.py     # Fetch CSV data
   python teja_get_json.py    # Fetch ISS location data
   python teja_get_excel.py   # Fetch Excel data
   python teja_get_text.py    # Fetch text data
   ```

2. Process data:
   ```bash
   python teja_process_csv.py     # Analyze happiness data
   python teja_process_json.py    # Analyze ISS position
   python teja_process_excel.py   # Process Excel data
   python teja_process_text.py    # Analyze text content
   ```

### Run All Operations

To fetch and process all data types at once:
```bash
python teja_run_all.py
```

## Output

- Processed results are stored in the `data_processed/` directory
- Log files are stored in the `logs/` directory
- Each processing module generates specific insights:
  - CSV: Statistics on world happiness scores
  - JSON: ISS position coordinates and hemisphere location
  - Excel: Feedback data analysis
  - Text: Text content analysis

## Author
vnallam09
09/13/2025