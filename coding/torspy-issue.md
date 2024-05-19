# Torspy: Issues and Solutions

## Common Issues and Their Solutions

### 1. Tor Connection Issue
**Error:** "Tor is not running or not properly configured. Please start Tor and try again."

**Solution:** 
- Ensure Tor is installed and running on your system.
- Restart the Tor service by using the command `sudo service tor restart` or the equivalent command for your system.
- Disconnect and reconnect to Tor, then wait a few minutes before trying again.

### 2. Timeout Error
**Error:** "Error fetching the page: ReadTimeout."

**Solution:**
- Check your internet connection.
- Restart Tor and try again.

### 3. Invalid URL Format
**Error:** "Invalid .onion URL provided."

**Solution:**
- Verify that the .onion URL is correctly formatted and valid.
- Ensure the URL uses the correct domain (e.g., ends with .onion).

### 4. Missing Module Error
**Error:** "ModuleNotFoundError: No module named 'torspy.scraper.XXX'."

**Solution:**
- Ensure all necessary modules are installed correctly. Reinstall torspy using `pip install torspy`.
- Verify the correct file structure and check if the required files are in the appropriate directories.

### 5. Permission Denied
**Error:** "PermissionError: [Errno 13] Permission denied: 'filename'"

**Solution:**
- Ensure you have the necessary permissions to read/write files in the specified directory.
- Run the command with elevated privileges (e.g., using `sudo` if on a Unix-like system).

### 6. File Not Found
**Error:** "FileNotFoundError: [Errno 2] No such file or directory: 'filename'"

**Solution:**
- Verify the file path and name are correct.
- Ensure the file exists in the specified directory.

### 7. Saving File Error
**Error:** "File not saved: 'filename'"

**Solution:**
- Ensure the directory where you want to save the file exists.
- Verify you have write permissions to the directory.
- Specify the correct path and filename for saving the file.

### 8. Unrecognized Arguments
**Error:** "torspy: error: unrecognized arguments: 'argument'"

**Solution:**
- Check the syntax and options you are using with the torspy command.
- Refer to the help section (`torspy -h`) for the correct usage and available arguments.

### 9. HTTP Error
**Error:** "HTTPError: HTTP Error 403: Forbidden."

**Solution:**
- Ensure the .onion site you are trying to access is up and reachable.
- Verify the URL and try accessing it again after some time.

#### Issues 

- Report an issue : <a href="https://github.com/mr-fidal/torspy/issues">Click</a>
