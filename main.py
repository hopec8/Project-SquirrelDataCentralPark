import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = ["Gray", "Cinnamon", "Black"]

squirrel_counts = {}
for color in fur_colors:
    squirrel_counts[color] = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])

for color, count in squirrel_counts.items():
    print(f"{color}: {count}")

squirrel_df = pd.DataFrame({
    "Fur Color": list(squirrel_counts.keys()),
    "Count": list(squirrel_counts.values())
})

print(squirrel_df)