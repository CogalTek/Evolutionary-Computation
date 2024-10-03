import sys
from src.help import displayHelp  # Import the function to display help instructions
from src.process import processStart  # Import the function to start the main process
import time  # Import time module to track execution time

def main():
    """
    Main function that handles command-line arguments and triggers corresponding actions.
    """
    start_time = time.time()  # Record the start time for execution time tracking

    # Check if any arguments were provided
    if len(sys.argv) > 1:
        # Display help if -h, --h, or --help is provided
        if "-h" in sys.argv or "--h" in sys.argv or "--help" in sys.argv:
            displayHelp()
        else:
            processStart()
    else:
        # If no arguments, display help by default
        displayHelp()

    # Calculate and print the elapsed execution time
    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")

# Execute the main function only if the script is run directly
if __name__ == "__main__":
    main()
