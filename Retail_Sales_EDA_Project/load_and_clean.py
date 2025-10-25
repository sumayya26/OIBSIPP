import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    return df

def basic_clean(df):
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    print("Cleaned dataset.")
    return df

if __name__ == "__main__":
    data_path = "retail_sales_dataset.csv"
    df = load_data(data_path)
    df = basic_clean(df)
    df.to_csv("retail_sales_dataset_cleaned.csv", index=False)
