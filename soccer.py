import pandas as pd

# 1. Cargar el archivo CSV
df = pd.read_csv("SP1.csv")  # Asegúrate de que está en el mismo directorio o usa una ruta completa

# 2. Revisar las primeras filas (para depuración opcional)
print(df.head())

# 3. Calcular goles por equipo (casa y fuera)
home_goals = df.groupby("HomeTeam")["FTHG"].sum()
away_goals = df.groupby("AwayTeam")["FTAG"].sum()
total_goals = home_goals.add(away_goals, fill_value=0).sort_values(ascending=False)

# 4. Mostrar el top 10 de equipos con más goles
print("\nTop 10 equipos con más goles:")
print(total_goals.head(10))

# 5. Calcular jornada por orden cronológico
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')
df['Jornada'] = df.groupby('HomeTeam').cumcount() + 1

# 6. Calcular goles por jornada
goles_por_jornada = df.groupby('Jornada')[['FTHG', 'FTAG']].sum()
goles_por_jornada['Total'] = goles_por_jornada['FTHG'] + goles_por_jornada['FTAG']

# 7. Exportar los resultados a CSV
total_goals.to_csv("output/goles_por_equipo.csv")
goles_por_jornada.to_csv("output/goles_por_jornada.csv")

print("\nExportación completada.")
