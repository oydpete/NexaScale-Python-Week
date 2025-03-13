# Import the necessary libraries

import psutil                                                                       # Import Library for system Info
import time                                                                         # Import Library for delay
from datetime import datetime                                                       # Import Library for get system date

#############################################################################################

#  Function to get CPU and memory usage

def system_usage():                                                                 # System usage Function
                                       
    CPU = psutil.cpu_percent(interval=1)                                            # CPU usage is mesaured as percentage every 1 sec to var CPU
    
    memory_usage = psutil.virtual_memory()                                                # Memory usage is mesaured as percentage every 100 sec to var MEM

    MEM = memory_usage.percent                                                       # Get memory usage as a percentage
    
    return CPU, MEM                                                                 # Return value of CPU and memory usage


#####################################################################################################



# Function to Append to log file and dispaly format


def monitor_system(interval=7, log_file="system_usage.log"):                       # Function to monitor system and save in log file

    try:

        with open(log_file, "a") as file:                                           # Open log file as append
             
            print("System monitoring started, Press Ctrl+C to stop")               # Print start message   

            while True:                                                            # run infinite loop
                    
                     
                    
                    CPU,MEM = system_usage()

                    timefort = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # Time display format
                            
                    log_entry = f"{timefort} | CPU Usage: {CPU}%, Memory Usage: {MEM}%\n" # To display on cmd
                        
                    print(log_entry.strip())                                    # Display the CPU and memory usage on cmd
                            
                    file.write(log_entry)                                       # Write to log file

                    file.flush()                                                # Ensure data is written to the file immediately
                        
                    time.sleep(interval)                                        # Next to check again

    except KeyboardInterrupt:                                                       # If the user presses Ctrl+C, stop the program


        print("\nstopped.")

################################################################################################################


# Main program starts here
    
monitor_system()                                                                    # Start Main Program