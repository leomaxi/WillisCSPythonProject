import pandas as pd

# Load assignment CSV file
df = pd.read_csv("Assignment.csv")

# Calculate derived columns
df["Total Games"] = df["Sumer_Game"] + df["Winter_Games"]
df["Gold_Combined_Total"] = df["Gold"] + df["Gold.1"]
df["Silver_Combined_Total"] = df["Silver"] + df["Silver.1"]
df["Bronze_Combined_Total"] = df["Bronze"] + df["Bronze.1"]
df["Combined total"] = (
    df["Gold_Combined_Total"] +
    df["Silver_Combined_Total"] +
    df["Bronze_Combined_Total"]
)

# show the updated DataFrame
print(df)

# Save the updated file with new filename
df.to_csv("Assignment_Updated.csv", index=False)
