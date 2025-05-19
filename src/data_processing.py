import pandas as pd



lap_time_fn = []
for i in range(1,25):
    lap_time_fn.append(str(f"raw_data/03_Classification_Race_Hour {i}.CSV"))

dfs = []
for name in lap_time_fn:
    df = pd.read_csv(name, header=0)
    dfs.append(df)
df = pd.concat(dfs, ignore_index=True)
df.drop_duplicates(inplace=True)
print("--------------")
print(df.describe)
print("--------------")
print(df.shape)
print("--------------")

df.to_csv("output.csv", index=False)