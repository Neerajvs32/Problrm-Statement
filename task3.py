3.Log Files Analyzer

import re
def analyze_log(log_file):
    # Initialize variables to store analysis results
    total_requests = 0
    error_404_count = 0
    page_requests = {}
    ip_requests = {}

    # Regular expression patterns for parsing log lines
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    page_pattern = r'\"(GET|POST) (.+?) HTTP'

    # Open the log file and analyze each line
    with open(log_file, 'r') as file:
        for line in file:
            total_requests += 1
            match = re.search(ip_pattern, line)
            if match:
                ip = match.group()
                ip_requests[ip] = ip_requests.get(ip, 0) + 1

            if ' 404 ' in line:
                error_404_count += 1

            match = re.search(page_pattern, line)
            if match:
                page = match.group(2)
                page_requests[page] = page_requests.get(page, 0) + 1

    # Generate and print the summary report
    print("Total Requests:", total_requests)
    print("404 Errors:", error_404_count)
    print("\nMost Requested Pages:")
    for page, count in sorted(page_requests.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{page}: {count} requests")
    print("\nIP Addresses with the Most Requests:")
    for ip, count in sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    log_file = "path/to/your/access.log"  # Update with your log file path
    analyze_log(log_file)
