"""
Process a JSON file to get the iss spacecraft current position relative to earth.

{
    "message": "success",
    "timestamp": 1757737594,
    "iss_position": {
        "latitude": "-27.1829",
        "longitude": "147.8387"
    }
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

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

def iss_location_finder(file_path: pathlib.Path) -> dict:
    """Get the ISS spacecraft current position (latitude and longitude) from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:
            # Use the json module load() function to read data into a Python dictionary
            data = json.load(file)
            
            # Extract position data
            position = data['iss_position']
            latitude = float(position['latitude'])
            longitude = float(position['longitude'])
            
            # Determine hemispheres
            ns_hemisphere = 'North' if latitude > 0 else 'South'
            ew_hemisphere = 'East' if longitude > 0 else 'West'
            
            # Create analysis results
            analysis = {
                'latitude': latitude,
                'longitude': longitude,
                'ns_hemisphere': ns_hemisphere,
                'ew_hemisphere': ew_hemisphere
            }
            
            return analysis
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, analyze ISS position, and save the result."""

    input_file = pathlib.Path(FETCHED_DATA_DIR, "iss_location.json")
    output_file = pathlib.Path(PROCESSED_DIR, "iss_location_analysis.txt")
    
    # Get ISS position data
    position_data = iss_location_finder(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write("ISS Position Analysis\n")
        file.write("===================\n\n")
        if position_data:
            file.write(f"Latitude: {position_data['latitude']:.4f} ({position_data['ns_hemisphere']})\n")
            file.write(f"Longitude: {position_data['longitude']:.4f} ({position_data['ew_hemisphere']})\n")
        else:
            file.write("Error: Could not retrieve ISS position data\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
