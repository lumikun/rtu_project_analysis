import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def time_to_seconds(t):
    m, s = t.split(':')
    return int(m) * 60 + float(s)

def sec_to_time(x, pos):
    m = int(x)//60
    s = x % 60
    return f"{m}:{s:05.2f}"

df = pd.read_csv("raw_data/23_Analysis_Race_Hour 24.CSV", sep=';')
filtered_df = df[df['CLASS'].str.contains("HYPERCAR")]
filtered_df = filtered_df.reset_index(drop=True)

ferrari = filtered_df.loc[filtered_df['NUMBER'] == 50]
ferrari = ferrari.reset_index(drop=True)
ferrari['LAP_TIME_S'] = ferrari['LAP_TIME'].apply(time_to_seconds)
porsche = filtered_df.loc[filtered_df['NUMBER'] == 6]
porsche['LAP_TIME_S'] = porsche['LAP_TIME'].apply(time_to_seconds)



# print(ferrari['LAP_TIME_S'].sum()/ferrari['LAP_NUMBER'].max())

# plt.plot(ferrari['LAP_NUMBER'], ferrari['LAP_TIME_S'], linestyle='-', color='red')
# plt.title("Ferrari 50 vs. Porsche 6")
# plt.plot(porsche["LAP_NUMBER"], porsche["LAP_TIME_S"], color="blue")
# plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(sec_to_time))
# plt.xlabel("Lap")
# plt.ylabel("Time (MM:SS)")
# plt.grid(True)
# plt.tight_layout()
# plt.show()
