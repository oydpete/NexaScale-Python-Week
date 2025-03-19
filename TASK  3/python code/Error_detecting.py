# Log File Error Scanner with Filtering

###############################################################################
# Function
def count_errors(log_file, severity= "all", month= "all"):


    filtered = []   
                                                                                                        # List to store filtered lines


    try:
        
        with open(log_file, "r") as file:                                                                               # Open the log file in read mode

            for line in file:                                                                                           # Scan all lines
                
                if (severity != "all" and severity not in line) or (month != "all" and month not in line):                                # Look for "severity" and "month"  in lines
                    continue

                filtered.append(line.strip())

        num_lines = len(filtered)                                                                                  # Add the found lines and append to  list

        return filtered , num_lines                                                                                                # Return the filtered logs

    except FileNotFoundError:                                                                                                       
        print(f"Error: The file '{log_file}' does not exist.")                                                          # what to display file doesnt exist
        return []                                                                                                       # Return what you got
    
    
    except Exception as e:                                                                  
        print(f"An unexpected error occurred: {e}")                                                                     # For other errors
        return []


########################################################################


# User Input        
log_file = input("Enter the log file name: ").strip()                                                                             # Get file_name


#######################################################


# Loop 

while True:
    severity = input("Enter severity level to filter (INFO, WARNING, ERROR) or press Enter to skip: ").strip().upper()            # input severity you want too see
    severity = severity if severity else "all"                                                                                     # if there is no severity then equate to none

    month = input("Enter month to filter (e.g October) or press Enter to skip: ").strip()                                        # Input the month you want to see
    month = month if month else "all"

    # Call the function inside the loop
    filtered, num_lines= count_errors(log_file, severity, month)                                                                            # Call the function with the filitered inside

    # Print the filtered logs
    print(f"\nThe {severity}(s) in {month} found in {log_file} are {num_lines} is/are:")                                                                     # Print the value

    print("\n".join(filtered) if filtered else "No matching logs found.")                                                         # Print the filtered log also

    # Ask the user if they want to continue
    check = input("\nDo you want to filter again? (y/n): ").strip().lower()                                                       # Ask to continue
    if check != "y":
        break                                                                                                                     # Exit the loop  
