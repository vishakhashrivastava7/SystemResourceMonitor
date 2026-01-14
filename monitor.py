import psutil

cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")
import psutil

# CPU usage (already done)
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# RAM usage
ram = psutil.virtual_memory()
print(f"RAM Usage: {ram.percent}%")
# Disk usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")
import psutil

cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

ram = psutil.virtual_memory()
print(f"RAM Usage: {ram.percent}%")

disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")
import psutil
import argparse

parser = argparse.ArgumentParser(description="System Resource Monitor CLI Tool")
parser.add_argument("--cpu", action="store_true", help="Show CPU usage")
parser.add_argument("--ram", action="store_true", help="Show RAM usage")
parser.add_argument("--disk", action="store_true", help="Show Disk usage")
parser.add_argument("--all", action="store_true", help="Show all metrics")

args = parser.parse_args()

if args.cpu or args.all:
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

if args.ram or args.all:
    ram = psutil.virtual_memory()
    print(f"RAM Usage: {ram.percent}%")

if args.disk or args.all:
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")
import psutil
import argparse
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)  # Colors reset automatically

# CLI Arguments
parser = argparse.ArgumentParser(description="System Resource Monitor CLI Tool")
parser.add_argument("--cpu", action="store_true", help="Show CPU usage")
parser.add_argument("--ram", action="store_true", help="Show RAM usage")
parser.add_argument("--disk", action="store_true", help="Show Disk usage")
parser.add_argument("--all", action="store_true", help="Show all metrics")
args = parser.parse_args()

# Data collection
data = []

if args.cpu or args.all:
    cpu_percent = psutil.cpu_percent(interval=1)
    data.append([Fore.CYAN + "CPU", f"{cpu_percent}%"])

if args.ram or args.all:
    ram = psutil.virtual_memory()
    data.append([Fore.GREEN + "RAM", f"{ram.percent}%"])

if args.disk or args.all:
    disk = psutil.disk_usage('/')
    data.append([Fore.MAGENTA + "Disk", f"{disk.percent}%"])

# Display table
if data:
    print(tabulate(data, headers=[Fore.YELLOW + "Resource", Fore.YELLOW + "Usage"], tablefmt="fancy_grid"))
else:
    print(Fore.RED + "No metric selected. Use --cpu, --ram, --disk or --all")
# Logging
with open("system_log.txt", "a") as f:
    for row in data:
        # Remove color codes for logging
        f.write(f"{row[0].replace(Fore.CYAN,'').replace(Fore.GREEN,'').replace(Fore.MAGENTA,'')}: {row[1]}\n")
    f.write("\n")
alerts = []
for row in data:
    resource = row[0].replace(Fore.CYAN,'').replace(Fore.GREEN,'').replace(Fore.MAGENTA,'')
    usage = float(row[1].replace('%',''))
    if (resource == "CPU" and usage > 80) or \
       (resource == "RAM" and usage > 75) or \
       (resource == "Disk" and usage > 85):
        alerts.append(Fore.RED + f"High {resource} usage: {usage}%")

for alert in alerts:
    print(alert)
