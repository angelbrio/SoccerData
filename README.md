# ⚽ La Liga 2024/2025 Statistics Analysis

This project analyzes real data from the **2024/25 Spanish La Liga season**, using Python data analysis tools. It generates key performance indicators such as:

- 🔝 **Top teams by total goals scored**
- 📈 **Goals per matchday**
- 📊 **KPIs exported as CSV for visualization in Power BI or Excel**

> ✅ This project is ideal for practicing data analysis, visualization, and cleaning sports datasets.

---

## 🧰 Technologies Used

| Tool                | Primary Use                            |
|---------------------|--------------------------------------|
| **Python**          | Main programming language            |
| **Pandas**          | Data manipulation and aggregation    |
| **CSV (football-data.co.uk)** | Original match dataset        |
| **Power BI / Excel**| Final visualization of exported KPIs|

---

## 📂 Project Structure

Soccerdata/
├── SP1.csv # La Liga match dataset (football-data.co.uk)
├── soccer.py # Main Python script
├── output/ # Exported CSV results
│ ├── goles_por_equipo.csv
│ └── goles_por_jornada.csv
└── README.md # This file


---

## 📝 How to Reproduce the Project Step-by-Step

### 1. Clone the repository

```bash
git clone https://github.com/your-username/futbol-dashboard.git
cd futbol-dashboard


### 2. Install dependencies

pip install pandas

### 2. Download the dataset

Go to https://www.football-data.co.uk/spainm.php and download the CSV file for La Liga.

Place the downloaded SP1.csv file in the root project folder.

### 3. Run the analysis

python soccerdata.py
