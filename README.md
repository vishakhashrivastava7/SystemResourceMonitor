# System Resource Monitor CLI Tool

## Description
This is a command-line tool to monitor system resources such as CPU, RAM, and Disk usage. 
It provides:

- Individual metrics (`--cpu`, `--ram`, `--disk`) or all at once (`--all`)
- Logs resource usage to a file (`system_log.txt`)
- Alerts when usage exceeds predefined thresholds
- Colorful and tabular output for better readability
- Fully compatible with Linux and Windows

## Features
- CPU, RAM, and Disk usage monitoring
- CLI argument support for selective metrics
- Logging usage history
- Alerts for high usage thresholds
- Table format with colors for terminal display

## Installation
Install required Python libraries:

```bash
pip install psutil tabulate colorama
