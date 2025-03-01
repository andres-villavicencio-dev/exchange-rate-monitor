import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime

class ExchangeRateViewer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("USD to NZD Exchange Rate Viewer")
        self.geometry("800x600")

        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Create matplotlib figure
        self.fig = Figure(figsize=(10, 6))
        self.ax = self.fig.add_subplot(111)
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Create control frame
        self.control_frame = ttk.Frame(self)
        self.control_frame.pack(fill=tk.X, padx=10, pady=5)

        # Add refresh button
        self.refresh_btn = ttk.Button(self.control_frame, text="Refresh", command=self.update_plot)
        self.refresh_btn.pack(side=tk.LEFT, padx=5)

        # Add auto-refresh checkbox
        self.auto_refresh_var = tk.BooleanVar(value=True)
        self.auto_refresh_cb = ttk.Checkbutton(
            self.control_frame,
            text="Auto-refresh (60s)",
            variable=self.auto_refresh_var,
            command=self.toggle_auto_refresh
        )
        self.auto_refresh_cb.pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_label = ttk.Label(self.control_frame, text="")
        self.status_label.pack(side=tk.RIGHT, padx=5)

        # Initialize plot
        self.update_plot()
        
        # Start auto-refresh
        self.toggle_auto_refresh()

    def load_data(self):
        try:
            df = pd.read_csv('usd_nzd_rates.csv')
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            return df
        except Exception as e:
            self.status_label.config(text=f"Error loading data: {str(e)}")
            return None

    def update_plot(self):
        df = self.load_data()
        if df is not None and not df.empty:
            self.ax.clear()
            self.ax.plot(df['timestamp'], df['rate'], marker='o')
            self.ax.set_title('USD to NZD Exchange Rate Over Time')
            self.ax.set_xlabel('Time')
            self.ax.set_ylabel('Exchange Rate (NZD per USD)')
            self.ax.grid(True)
            
            # Rotate x-axis labels for better readability
            self.fig.autofmt_xdate()
            
            # Update the plot
            self.canvas.draw()
            
            # Update status
            last_update = df['timestamp'].max().strftime('%Y-%m-%d %H:%M:%S')
            last_rate = df['rate'].iloc[-1]
            self.status_label.config(
                text=f"Last update: {last_update} | Rate: {last_rate:.4f}"
            )
        else:
            self.status_label.config(text="No data available")

    def toggle_auto_refresh(self):
        if hasattr(self, '_auto_refresh_job'):
            self.after_cancel(self._auto_refresh_job)
            delattr(self, '_auto_refresh_job')
        
        if self.auto_refresh_var.get():
            self.schedule_refresh()

    def schedule_refresh(self):
        self.update_plot()
        self._auto_refresh_job = self.after(60000, self.schedule_refresh)  # 60000ms = 60s

if __name__ == "__main__":
    app = ExchangeRateViewer()
    app.mainloop()