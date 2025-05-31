#!/usr/bin/env python3
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def time_to_sec(t):
    m, s = t.split(':')
    return int(m) * 60 + float(s)

def sec_to_time(x, pos):
    m = int(x)//60
    s = x % 60
    return f"{m}:{s:05.2f}"

def analysis(f, s=None):
    top_5 = [50, 7, 51, 6, 8]
    df = pd.read_csv(f, sep=';')
    fdf = df[df['NUMBER'].isin(top_5)]
    fdf['LAP_TIME_S'] = fdf.loc[:,'LAP_TIME'].apply(time_to_sec)
    fdf = fdf.reset_index(drop=True)
    # Drop lap times higher than 5 minutes as those are more than likelly FCY/YF/SC/PIT_LAPS
    max_laptime = 5*60
    fdf = fdf[fdf['LAP_TIME_S'] <= max_laptime]
    # Group, the fastest drivers of each car
    grouped = fdf.groupby(['NUMBER', 'DRIVER_NAME'])['LAP_TIME_S'].mean().reset_index()
    fastest_drivers = grouped.loc[grouped.groupby('NUMBER')['LAP_TIME_S'].idxmin()]
    # Set up plotting for the fastest drivers, on average
    plt.figure(figsize=(10, 6))
    bars = plt.bar(fastest_drivers['NUMBER'].astype(str), fastest_drivers['LAP_TIME_S'], color='skyblue')
    plt.xlabel('Car Number')
    plt.ylabel('Average Lap Time (MM:SS.ms)')
    plt.title("Fastest Drivers on average, for each of the Top 5 finnishers of Le Mans 2024")
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(sec_to_time))

    # more plot setup.
    for bar, driver in zip(bars, fastest_drivers['DRIVER_NAME']):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height, driver, ha='center', va='bottom')
    plt.show()

    # Find the fastest driver, with the fastest average lap time.
    average_lap_times = fdf.groupby('DRIVER_NAME')['LAP_TIME_S'].mean()
    fastest_driver = average_lap_times.idxmin()
    fastest_driver_avg_time = average_lap_times.min()
    print(f"The fastest Driver on average is {fastest_driver} with an average lap time of {sec_to_time(fastest_driver_avg_time, None)}.")
    
    fastest_driver_data = fdf[fdf['DRIVER_NAME'] == fastest_driver]
    plt.figure(figsize=(10, 6))
    plt.plot(fastest_driver_data['LAP_NUMBER'], fastest_driver_data['LAP_TIME_S'], marker='o', linestyle='-', color='r')
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(sec_to_time))
    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (MM:SS.ms)')
    plt.title(f"Lap times for {fastest_driver}")
    plt.grid(True)
    plt.show()

    if s == None:
        print("No Savefile provided.")
    else:
        fastest_driver_data.to_csv(s)


def main():
    parser = argparse.ArgumentParser(
        prog='FIA WEC 24h Le Mans',
        description="Lap time analysis of the top 5 overall finishers. Goal is to find fastest driver(on average) from the TOP 5 finishers.",
        epilog='Usage: data_analysis_final.py -f [filename] -s [output_csv]'
    )
    parser.add_argument('-f', '--filename', required=True)
    parser.add_argument('-s', '--savefile')
    args = parser.parse_args()

    
    if (args.savefile == None):
        print("No output file selected!")
        analysis(args.filename)
    else: 
        print(f"Output file {args.savefile}")
        analysis(args.filename, args.savefile)

if __name__ == "__main__":
    main()
