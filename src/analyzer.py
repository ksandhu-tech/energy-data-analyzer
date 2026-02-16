import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_data(df):
    summary = {
        "average_usage": df["usage_kwh"].mean(),
        "max_usage": df["usage_kwh"].max(),
        "min_usage": df["usage_kwh"].min()
    }
    return summary

def generate_report(summary):
    print("Energy Usage Report")
    print("-------------------")
    for key, value in summary.items():
        print(f"{key}: {value:.2f}")

def main():
    file_path = "data/energy_data.csv"
    df = load_data(file_path)
    summary = analyze_data(df)
    generate_report(summary)

if __name__ == "__main__":
    main()
