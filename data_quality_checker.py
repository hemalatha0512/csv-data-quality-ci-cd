import sys
import pandas as pd

print("Automated CSV Data Quality Checker")
print("----------------------------------")

if len(sys.argv) < 2:
    print("Usage: data_quality_checker.py <csv_file>")
    sys.exit(1)

file_name = sys.argv[1]

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print("Error: File not found")
    sys.exit(1)

rows, cols = df.shape
missing_values = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()

numeric_cols = df.select_dtypes(include=['int64', 'float64'])
negative_values = (numeric_cols < 0).sum().sum()

print(f"Rows: {rows}")
print(f"Columns: {cols}")
print(f"Missing Values: {missing_values}")
print(f"Duplicate Rows: {duplicate_rows}")
print(f"Invalid (Negative) Numeric Values: {negative_values}")

if missing_values == 0 and duplicate_rows == 0 and negative_values == 0:
    print("Data Quality Status: PASS ✅")
else:
    print("Data Quality Status: FAIL ❌")
