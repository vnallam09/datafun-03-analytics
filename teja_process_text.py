"""
Process a text file to count occurrences of the word "Dracula" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys
import re

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

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r', encoding='utf-8') as file:
            content: str = file.read()
            # Use word boundaries to match complete words only
            word_pattern = r'\b' + re.escape(word.lower()) + r'\b'
            matches = re.findall(word_pattern, content.lower())
            return len(matches)
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'Dracula', and save the result."""
 
    input_file = pathlib.Path(FETCHED_DATA_DIR, "dracula.txt")

    output_file = pathlib.Path(PROCESSED_DIR, "text_dracula_word_count.txt")

    word_to_count: str = "Dracula"

    word_count: int = count_word_occurrences(input_file, word_to_count)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write the results to the output file
    with output_file.open('w', encoding='utf-8') as file:
        file.write(f"Occurrences of '{word_to_count}': {word_count}\n")
    
    # Log the processing of the TEXT file
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")
