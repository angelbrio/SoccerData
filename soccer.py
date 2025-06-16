import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general
st.set_page_config(page_title="⚽ Soccer Match Dashboard", layout="wide")
st.title("⚽ Soccer Match Analysis Dashboard")

# Cargar datos
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df = df.sort_values('Date')
    df['Matchday'] = df.groupby('HomeTeam').cumcount() + 1
    return df

# Upload csv
uploaded_file = st.sidebar.file_uploader("Upload match data CSV", type=["csv"])
if uploaded_file:
    df = load_data(uploaded_file)
else:
    st.warning("Upload a CSV file to begin.")
    st.stop()

# Pestañas de navegación
tab1, tab2, tab3, tab4 = st.tabs(["📅 Dataset", "📊 KPIs", "📈 Charts", "🔎 Team Explorer"])

# 📅 TAB 1 – Dataset
with tab1:
    st.subheader("📅 Raw Match Data")
    st.dataframe(df)

# 📊 TAB 2 – Key Stats
with tab2:
    st.subheader("⚙️ Key Match Stats")

    total_matches = len(df)
    total_goals = df['FTHG'].sum() + df['FTAG'].sum()
    avg_goals = round(total_goals / total_matches, 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Matches", total_matches)
    col2.metric("Total Goals", total_goals)
    col3.metric("Avg Goals per Match", avg_goals)

    result_counts = df['FTR'].value_counts(normalize=True) * 100
    st.write("🏆 Match Result Distribution (%):")
    st.bar_chart(result_counts)

# 📈 TAB 3 – Views
with tab3:
    st.subheader("📈 Team & Matchday Analysis")

    # Goles por equipo (Top 10)
    home_goals = df.groupby('HomeTeam')['FTHG'].sum()
    away_goals = df.groupby('AwayTeam')['FTAG'].sum()
    total_goals_team = home_goals.add(away_goals, fill_value=0).sort_values(ascending=False)

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=total_goals_team.head(10).values, y=total_goals_team.head(10).index, ax=ax1, palette="Blues_d")
    ax1.set_title("Top 10 Scoring Teams")
    ax1.set_xlabel("Goals")
    ax1.set_ylabel("Team")
    st.pyplot(fig1)

    # Goles por jornada
    matchday_goals = df.groupby('Matchday')[['FTHG', 'FTAG']].sum()
    matchday_goals['Total'] = matchday_goals['FTHG'] + matchday_goals['FTAG']

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    matchday_goals['Total'].plot(kind='line', marker='o', color='orange', ax=ax2)
    ax2.set_title("Total Goals per Matchday")
    ax2.set_xlabel("Matchday")
    ax2.set_ylabel("Goals")
    ax2.grid(True)
    st.pyplot(fig2)

# 🔎 TAB 4 – Team Explorer
with tab4:
    st.subheader("🔍 Team Match Explorer")

    team = st.selectbox("Select a team", sorted(df['HomeTeam'].unique()))
    team_matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)]

    st.write(f"Match history for **{team}**:")
    st.dataframe(team_matches[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']])

    team_goals = (
        team_matches.apply(
            lambda row: row['FTHG'] if row['HomeTeam'] == team else row['FTAG'],
            axis=1
        )
    )

    fig3, ax3 = plt.subplots()
    ax3.plot(team_matches['Date'], team_goals, marker='o', linestyle='-')
    ax3.set_title(f"{team} Goals Over Time")
    ax3.set_ylabel("Goals")
    ax3.set_xlabel("Date")
    ax3.grid(True)
    st.pyplot(fig3)



