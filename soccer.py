import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(filepath):
    """
    Load the CSV dataset and prepare necessary columns.
    Converts 'Date' to datetime and sorts data by date.
    Adds a 'Matchday' (Jornada) column counting matches per HomeTeam.
    """
    try:
        df = pd.read_csv(filepath)
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        df = df.sort_values('Date')
        # Add matchday number for each home team
        df['Matchday'] = df.groupby('HomeTeam').cumcount() + 1
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None

def calculate_goals_by_team(df):
    """
    Calculate total goals scored by each team, combining home and away goals.
    Returns a Series sorted descending by total goals.
    """
    home_goals = df.groupby('HomeTeam')['FTHG'].sum()   # Full Time Home Goals
    away_goals = df.groupby('AwayTeam')['FTAG'].sum()   # Full Time Away Goals
    total_goals = home_goals.add(away_goals, fill_value=0).sort_values(ascending=False)
    return total_goals

def calculate_goals_by_matchday(df):
    """
    Calculate total goals scored per matchday.
    Sums home and away goals for each jornada.
    Returns a DataFrame with home goals, away goals, and total goals per matchday.
    """
    goals_by_matchday = df.groupby('Matchday')[['FTHG', 'FTAG']].sum()
    goals_by_matchday['Total'] = goals_by_matchday['FTHG'] + goals_by_matchday['FTAG']
    return goals_by_matchday

def create_charts(total_goals, goals_by_matchday, output_dir):
    """
    Generate and save charts visualizing:
    - Top 10 teams by total goals (bar chart)
    - Total goals per matchday (line chart)
    Saves PNG files in the specified output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Bar chart: Top 10 teams by goals scored
    plt.figure(figsize=(10,6))
    total_goals.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Teams by Total Goals')
    plt.ylabel('Total Goals')
    plt.xlabel('Team')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_10_goals_team.png'))
    plt.close()

    # Line chart: Total goals per matchday
    plt.figure(figsize=(10,6))
    goals_by_matchday['Total'].plot(kind='line', marker='o', color='orange')
    plt.title('Total Goals per Matchday')
    plt.ylabel('Goals')
    plt.xlabel('Matchday')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'goals_per_matchday.png'))
    plt.close()

def save_results(total_goals, goals_by_matchday, output_dir):
    """
    Save the KPIs to CSV files inside the output directory.
    Creates directory if it does not exist.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    total_goals.to_csv(os.path.join(output_dir, 'goals_by_team.csv'), header=['Total Goals'])
    goals_by_matchday.to_csv(os.path.join(output_dir, 'goals_by_matchday.csv'))

def main():
    input_file = 'SP1.csv'   # Input CSV filename
    output_dir = 'output'    # Output folder for CSV and charts

    df = load_data(input_file)
    if df is None:
        return

    total_goals = calculate_goals_by_team(df)
    goals_by_matchday = calculate_goals_by_matchday(df)

    save_results(total_goals, goals_by_matchday, output_dir)
    create_charts(total_goals, goals_by_matchday, output_dir)

    print("Analysis complete. CSV files and charts saved in the 'output/' folder.")

if __name__ == '__main__':
    main()



