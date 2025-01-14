import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def load_and_process_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        

        df['Date'] = pd.to_datetime(df['Date'])
        df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')  
        
        daily_report = df.groupby([df['Date'].dt.date, 'Product']).agg({'Sales': 'sum'}).reset_index()
        return daily_report
    except Exception as e:
        print(f"Error processing the data: {e}")
        return None

def generate_report(df, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        today_date = datetime.today().strftime('%Y-%m-%d')
        report_filename = f"daily_sales_report_{today_date}.csv"
        report_path = os.path.join(output_dir, report_filename)
        
        df.to_csv(report_path, index=False)
        print(f"Report saved to {report_path}")
        
        plt.figure(figsize=(10, 6))
        for product in df['Product'].unique():
            product_data = df[df['Product'] == product]
            plt.plot(product_data['Date'], product_data['Sales'], label=product)
        
        plt.title("Daily Sales by Product")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.legend()
        
        plot_filename = f"daily_sales_plot_{today_date}.png"
        plot_path = os.path.join(output_dir, plot_filename)
        plt.savefig(plot_path)
        print(f"Plot saved to {plot_path}")
        plt.close()
    except Exception as e:
        print(f"Error generating the report: {e}")

def automate_report_generation(file_path, output_dir):

    processed_data = load_and_process_data(file_path)
    
    if processed_data is not None:
        generate_report(processed_data, output_dir)
    else:
        print("Error: No data to process.")

if __name__ == "__main__":
    dataset_path = r"C:\Users\rouna\OneDrive\Desktop\cognifyz\sales_data.csv"

    
    output_directory = 'reports'
    
    automate_report_generation(dataset_path, output_directory)
