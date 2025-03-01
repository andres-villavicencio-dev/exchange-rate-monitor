# Exchange Rate Monitor

A collection of scripts to monitor and visualize USD to NZD exchange rates in real-time. This project includes tools for data collection, visualization, and automated monitoring of exchange rates.

## Features

- Automated exchange rate data collection every 20 minutes
- CSV-based data storage for easy analysis
- Real-time plot generation
- Support for both GUI and headless environments

## Components

### 1. Data Collection (`fetch_exchange_rate.sh`)

A bash script that:
- Fetches USD to NZD exchange rates from ExchangeRate-API
- Stores data in CSV format with timestamps
- Runs continuously with 20-minute intervals
- Handles network errors gracefully

Usage:
```bash
# Start the data collection in the background
./fetch_exchange_rate.sh > script.log 2>&1 &

# View the log
tail -f script.log

# Stop the script
pkill -f fetch_exchange_rate.sh
```

### 2. GUI Visualization (`exchange_rate_viewer.py`)

A tkinter-based GUI application that:
- Displays real-time exchange rate plots
- Auto-refreshes every 60 seconds
- Shows current rate and rate changes
- Includes manual refresh option

Usage:
```bash
python3 exchange_rate_viewer.py
```

Note: Requires a display server (X11/Wayland) to run.

### 3. Headless Plotting (`plot_exchange_rates.py`)

A script for environments without display servers that:
- Generates PNG plot files
- Updates automatically every minute
- Shows statistics in the console
- Maintains plot history

Usage:
```bash
# Run in background
python3 plot_exchange_rates.py > plot.log 2>&1 &

# View statistics
tail -f plot.log

# Stop the script
pkill -f plot_exchange_rates.py
```

## Data Format

The exchange rate data is stored in `usd_nzd_rates.csv` with the following format:
```csv
timestamp,rate
2025-03-01 07:45:10,1.786947
```

## Requirements

- Python 3.x
- Required Python packages:
  - pandas
  - matplotlib
  - tkinter (for GUI version)
- Bash environment
- Internet connection for data fetching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/andres-villavicencio-dev/exchange-rate-monitor.git
cd exchange-rate-monitor
```

2. Install Python dependencies:
```bash
pip install pandas matplotlib
```

3. Make the bash script executable:
```bash
chmod +x fetch_exchange_rate.sh
```

## Usage Examples

### Basic Monitoring Setup

1. Start data collection:
```bash
./fetch_exchange_rate.sh > script.log 2>&1 &
```

2. Start plot generation:
```bash
python3 plot_exchange_rates.py > plot.log 2>&1 &
```

3. Monitor the results:
```bash
# View the latest exchange rates
cat usd_nzd_rates.csv

# Check the plot file
ls -l exchange_rate_plot.png
```

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.