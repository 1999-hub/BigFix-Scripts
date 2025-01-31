import subprocess

def uninstall_vlc():
    """
    Uninstall VLC Media Player using the WMIC command-line utility.

    This script attempts to remove VLC Media Player silently without user interaction. 
    It checks for errors during the uninstallation process and provides appropriate feedback.
    """
    try:
        # Command to uninstall VLC Media Player using wmic
        command = 'wmic product where "name=\'VLC media player\'" call uninstall /nointeractive'
        
        # Execute the command
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print the output based on the process return code
        if process.returncode == 0:
            print("VLC Media Player uninstalled successfully.")
        else:
            print(f"Failed to uninstall VLC Media Player. Error: {process.stderr}")
    
    except subprocess.CalledProcessError as e:
        # Handle known errors during subprocess execution
        print(f"An error occurred while executing the uninstallation command: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")

# Entry point of the script
if __name__ == "__main__":
    """
    Check for script execution directly and call the uninstall_vlc function.
    """
    uninstall_vlc()
