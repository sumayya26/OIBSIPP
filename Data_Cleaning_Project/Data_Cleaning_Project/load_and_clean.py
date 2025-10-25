import pandas as pd
import argparse

def main(input_path, output_path):
    df = pd.read_csv(input_path, on_bad_lines='skip')
    
    # Fill missing values
    df['name'].fillna("No Name", inplace=True)
    df['host_name'].fillna("Unknown", inplace=True)
    df['reviews_per_month'].fillna(0, inplace=True)
    
    # Convert date
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
    
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    
    # Standardize text
    df['neighbourhood_group'] = df['neighbourhood_group'].str.lower()
    df['room_type'] = df['room_type'].str.lower()
    
    # Remove outliers
    df = df[df['price'] <= 1000]
    
    df.to_csv(output_path, index=False)
    print("✅ Cleaned data saved to:", output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.input, args.output)
