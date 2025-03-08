import pandas as pd
import matplotlib.pyplot as plt
import datetime

def create_plot():
    try:
        # Read the CSV file
        df = pd.read_csv('data/usd_nzd_rates.csv')
        if df.empty:
            print("No data available yet")
            return
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(df['timestamp'], df['rate'], marker='o')
        plt.title('USD to NZD Exchange Rate Over Time')
        plt.xlabel('Time')
        plt.ylabel('Exchange Rate (NZD per USD)')
        plt.grid(True)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('images/exchange_rate_plot.png')
        plt.close()
        
        # Print statistics
        last_update = df['timestamp'].max()
        last_rate = df['rate'].iloc[-1]
        print(f"\nLast update: {last_update}")
        print(f"Current rate: {last_rate:.4f} NZD per USD")
        
        if len(df) > 1:
            rate_change = df['rate'].iloc[-1] - df['rate'].iloc[-2]
            print(f"Change since last update: {rate_change:+.4f}")
            
        print(f"\nPlot saved as 'exchange_rate_plot.png'")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    create_plot()