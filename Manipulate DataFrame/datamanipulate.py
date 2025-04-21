import csv

# Open and read the original CSV
with open("Assignment.csv", mode="r", newline='', encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    # fieldnames = reader.fieldnames + [
    #     "Total Games",
    #     "Gold_Combined_Total",
    #     "Silver_Combined_Total",
    #     "Bronze_Combined_Total",
    #     "Combined total"
    # ]
    # updated_rows = []


    for row in reader:
        try:
            print("Column Names:", row.keys())
            #Convert values to integers safely
            #summer_game = int(row["Sumer_Game"])
            # gold = int(row["Gold"])
            # silver = int(row["Silver"])
            # bronze = int(row["Bronze"])
            # # summer_total = int(row[Total])
            # winter_game = int(row["Winter_Games"])
            # gold_winter = int(row["Gold"])
           # silver_winter = row["Silver.1"]
            # bronze_winter = int(row[9])
            # winter_total = int(row[10])
           # print(str(gold)+" gold 1")
           # print(str(gold_winter)+" gold 2")
        except ValueError:
            # Catch missing and invalid data
            summer_game = winter_game = gold = silver = bronze = gold_winter = silver_winter = bronze_winter = 0

        # # Compute new values
        # total_games = summer_game + winter_game
        # gold_total = gold + gold_winter
        # silver_total = silver + silver_winter
        # bronze_total = bronze + bronze_winter
        # combined_total = gold_total + silver_total + bronze_total
        #
        # # Add new fields to the row
        # row["Total Games"] = total_games
        # row["Gold_Combined_Total"] = gold_total
        # row["Silver_Combined_Total"] = silver_total
        # row["Bronze_Combined_Total"] = bronze_total
        # row["Combined total"] = combined_total
        #
        # updated_rows.append(row)

# # Write updated data to a new CSV file
# with open("Assignment_Updated.csv", mode="w", newline='', encoding="utf-8") as outfile:
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(updated_rows)
#
# print("Updated CSV file 'Assignment_Updated.csv' created successfully.")
