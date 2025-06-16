# ⚽ La Liga 2024/2025 Statistics Dashboard

This project analyzes real data from the **2024/25 Spanish La Liga season**, using Python and data visualization tools. It includes:

- 🔝 **Top-scoring teams**
- 📈 **Goals per matchday**
- 📊 **KPIs exportable to Power BI or Excel**
- 🌐 **Interactive web dashboard built with Streamlit**

> ✅ A perfect project for practicing data cleaning, aggregation, and visual storytelling with football data.

---

## 🚀 Try the Live App (Streamlit)

You can explore the dashboard live here:  
👉 **[angelbrio-soccerdata.streamlit.app](https://angelbrio-soccerdata.streamlit.app)**

> ⏳ *Note: The app may take a few seconds to load if it's waking up from sleep mode.*

---

## 🧰 Technologies Used

| Tool                  | Purpose                                 |
|------------------------|------------------------------------------|
| **Python**             | Core programming language                |
| **Pandas**             | Data manipulation & cleaning             |
| **Matplotlib / Seaborn** | Charting and plots                    |
| **Streamlit**          | Web app framework for data apps          |
| **CSV (football-data.co.uk)** | Raw match data source             |
| **Power BI / Excel**   | Optional visualization of exported data |

---

## 📂 Project Structure

Soccerdata/
├── SP1.csv # La Liga match dataset
├── soccer.py # Main Streamlit app
├── requirements.txt # Project dependencies
├── output/ # Generated CSV files
│ ├── goles_por_equipo.csv
│ └── goles_por_jornada.csv
└── README.md


---

## 📝 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/angelbrio/SoccerData.git
cd SoccerData

2. Install dependencies

pip install -r requirements.txt

3. Run the Streamlit app

streamlit run soccer.py

4. (Optional) Update the dataset
You can download the most recent La Liga CSV from:
📥 football-data.co.uk/spainm.php

Place the new SP1.csv file in the project root.

