"""
Process a CSV file on airline-safety.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys
import pandas as pd

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "requested_data"
PROCESSED_DIR: str = "data_processed"

#####################################
# Define Functions
#####################################

def analyze_safety(file_path: pathlib.Path) -> dict:
    """geting the safety data from the csv file and analyzing the airline sefety"""
    try:
        airplane_data = pd.read_csv(file_path)  
        # Extract the 'safety_metric' column
        airplane_data['safety_metric'] = airplane_data['fatal_accidents_85_99'] + airplane_data['fatal_accidents_00_14'] + airplane_data['fatalities_85_99'] + airplane_data['fatalities_00_14']
        
        ranked_airlines = airplane_data.sort_values(by='safety_metric', ascending=True)
        safest_airlines = ranked_airlines[ranked_airlines['safety_metric'] == ranked_airlines['safety_metric'].min()]
        least_safe_airlines = ranked_airlines[ranked_airlines['safety_metric'] == ranked_airlines['safety_metric'].max()]

        # Calculate statistics
        top_5_safest = ranked_airlines.head(5)
        top_5_least_safe = ranked_airlines.tail(5)

        safest_worst_airlines_dict = {
            "safest_5": top_5_safest[['airline', 'safety_metric']].to_dict('records'),
            "least_safe_5": top_5_least_safe[['airline', 'safety_metric']].to_dict('records')
        }
        
        return safest_worst_airlines_dict
    
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "airline_safety.csv")
    
    output_file = pathlib.Path(PROCESSED_DIR, "airline_safety_stats.txt")
    
    stats = analyze_safety(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:    
        file.write("Safest 5 Airlines:\n")
        file.write(stats['safest_5'].__str__())
        file.write("=================\n")
        file.write("Least Safe 5 Airlines:\n")
        file.write(stats['least_safe_5'].__str__())
        file.write("=================\n")
            
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
