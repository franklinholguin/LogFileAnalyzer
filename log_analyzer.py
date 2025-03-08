import re
from collections import Counter

def analyze_logs(log_file):
    failed_attempts = Counter()
    with open(log_file, "r") as f:
        for line in f:
            if "Failed password" in line:
                ip = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if ip:
                    failed_attempts[ip.group(1)] += 1
    
    print("Failed Login Attempts by IP:")
    for ip, count in failed_attempts.items():
        if count > 5:
            print(f"{ip}: {count} attempts (SUSPICIOUS)")
        else:
            print(f"{ip}: {count} attempts")

if __name__ == "__main__":
    analyze_logs("sample_log.txt")