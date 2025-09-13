"""
File: teja_run_all.py

To run all data get and process scripts

Author: Venkat Teja Nallamothu 
Date: 2025-09-12
"""

#####################################
# Import Modules
#####################################

# Import the main() functions from each "get" script
from teja_get_csv import main as get_csv_main
from teja_get_excel import main as get_excel_main
from teja_get_json import main as get_json_main
from teja_get_text import main as get_text_main

# Import the process functions from each "process" script
from teja_process_csv import process_csv_file
from teja_process_excel import process_excel_file
from teja_process_json import process_json_file
from teja_process_text import process_text_file

#####################################
# Run All Scripts
#####################################

if __name__ == "__main__":
    """Run all get scripts, then all process scripts."""
    print("=== Running all data fetching scripts ===")
    get_csv_main()
    get_excel_main()
    get_json_main()
    get_text_main()

    print("=== Running all data processing scripts ===")
    process_csv_file()
    process_excel_file()
    process_json_file()
    process_text_file()
    print("=== All scripts completed ===")