import pandas as pd

# Load the data
file_path = "/content/DBT.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Ensure correct column names
expected_columns = ["CUSTOMERNAME", "COUNTRY", "YEAR_ID", "QTR_ID", "TOTALLOSS", "TOTALREVENUE", "PROFIT"]
if list(df.columns) != expected_columns:
    print("Warning: Column names do not match expected format!")

# User input prompt
print("Total Revenue & Loss")
try:
    n = int(input("Enter the Year: "))  # Expecting year input
    q = int(input("Enter the Qtr: "))  # Expecting quarter input

    if n in [2003, 2004, 2005] and q in [1, 2, 3, 4]:  # Ensure valid quarters
        # Filter data for the entered year and quarter
        filtered_df = df[(df["YEAR_ID"] == n) & (df["QTR_ID"] == q)]

        # Determine the previous period (Previous quarter within the same year or Q4 of the previous year)
        if q == 1:
            prev_year = n - 1
            prev_quarter = 4
        else:
            prev_year = n
            prev_quarter = q - 1

        # Filter data for the previous period
        filtered_df_p = df[(df["YEAR_ID"] == prev_year) & (df["QTR_ID"] == prev_quarter)]

        # Calculate total revenue and loss for the selected year and quarter
        total_revenue = filtered_df["TOTALREVENUE"].sum()
        total_loss = filtered_df["TOTALLOSS"].sum()

        # Calculate total revenue and loss for the previous period
        prev_total_revenue = filtered_df_p["TOTALREVENUE"].sum()
        prev_total_loss = filtered_df_p["TOTALLOSS"].sum()

        # Calculate Year-over-Year (YoY) changes
        revenue_yoy_change = total_revenue - prev_total_revenue
        loss_yoy_change = total_loss - prev_total_loss

        # Display results
        print(f"Total Revenue for Year {n}, Quarter {q}: {total_revenue}")
        print(f"Total Loss for Year {n}, Quarter {q}: {total_loss}")
        print(f"Revenue Change from Previous Period ({prev_year}, Q{prev_quarter}): {revenue_yoy_change}")
        print(f"Loss Change from Previous Period ({prev_year}, Q{prev_quarter}): {loss_yoy_change}")

    else:
        print("Invalid choice! Please enter a valid year (2003, 2004, 2005) and quarter (1-4).")

except ValueError:
    print("Invalid input! Please enter a numeric value.")

