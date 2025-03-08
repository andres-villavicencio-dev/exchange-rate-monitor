#!/bin/bash

# Create CSV file with header if it doesn't exist
CSV_FILE="data/usd_nzd_rates.csv"
if [ ! -f "$CSV_FILE" ]; then
    echo "timestamp,rate" > "$CSV_FILE"
fi

while true; do
    # Get current timestamp
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Fetch exchange rate from ExchangeRate-API
    RATE=$(curl -s "https://open.er-api.com/v6/latest/USD" | grep -o '"NZD":[0-9.]*' | cut -d':' -f2)
    
    # Log the result if rate was found
    if [ ! -z "$RATE" ]; then
        echo "$TIMESTAMP,$RATE" >> "$CSV_FILE"
        echo "Logged rate: $RATE at $TIMESTAMP"
    else
        echo "Failed to fetch rate at $TIMESTAMP"
    fi
    
    # Wait 20 minutes
    sleep 30
done