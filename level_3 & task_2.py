import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def matplotlib_visualization(df):
    print("Generating Matplotlib visualizations...")
    plt.figure(figsize=(10, 6))
    df.hist(bins=20, figsize=(15, 10), color='skyblue', edgecolor='black')
    plt.tight_layout()
    plt.show()

def seaborn_visualization(df):
    print("Generating Seaborn visualizations...")

    # Convert 'Date' column to datetime if it's not already
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Selecting only numeric columns for correlation heatmap
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    sns.pairplot(numeric_df, diag_kind='kde', plot_kws={"alpha": 0.7})
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

def plotly_visualization(df):
    print("Generating Plotly visualizations...")

    # Ensure only numeric columns are selected
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    for column in numeric_df.columns:
        fig = px.histogram(df, x=column, title=f"Distribution of {column}", marginal="box")
        fig.show()

    if len(numeric_df.columns) >= 2:
        fig = px.scatter_matrix(numeric_df, dimensions=numeric_df.columns[:5], title="Scatter Matrix")
        fig.show()

if __name__ == "__main__":
    # Replace the file path with your actual dataset path
    file_path = r"C:\Users\rouna\OneDrive\Desktop\cognifyz\your_dataset.csv"

    # Load the dataset
    df = load_dataset(file_path)

    if df is not None:
        print("Dataset loaded successfully. Columns:", df.columns)

        # Generate visualizations
        matplotlib_visualization(df)
        seaborn_visualization(df)
        plotly_visualization(df)
