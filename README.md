# Subdomain Enumeration Tool - GreenSubEnum

![Banner](https://github.com/greencatcommunity/GreenSubEnum/blob/main/assets/deleteit.JPG)

## Description
A simple Python-based subdomain enumeration tool with threading support. This tool allows you to enumerate subdomains for a given domain by making HTTP requests to potential subdomains and checking their status codes. It supports both HTTP (port 80) and HTTPS (port 443) requests to determine if the subdomains exist.

## Usage
1. Clone this repository to your local machine.
2. Ensure you have Python and the required dependencies installed. You can install the required packages using:
   ```
   pip install -r requirements.txt
   ```
3. Run the script using the following command:
   ```
   python main.py
   ```
4. Enter the domain name when prompted. Make sure to enter a valid domain (e.g., example.com).
5. Enter the number of threads you want to use for the enumeration. The more threads, the faster the enumeration, but avoid using excessive threads to prevent performance issues.
6. The script will read the wordlist from the `wordlist.txt` file and start enumerating subdomains using the specified number of threads.
7. If a subdomain is found to be accessible via HTTP (port 80) or HTTPS (port 443), it will be displayed in the console.

## Disclaimer
This tool is meant for educational and informational purposes only. Please use it responsibly and ensure you have the necessary permissions before scanning any domain.

## Contributions
Contributions to improve and enhance this tool are welcome. Feel free to submit issues, suggestions, or pull requests to make it better.

