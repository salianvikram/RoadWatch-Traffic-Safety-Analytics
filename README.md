# 🚦 RoadWatch Traffic Safety Analytics

<p align="center">
  <strong>Exploratory analysis of traffic accident patterns across time, road types, weather, lighting, and severity.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/Analysis-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Visualisation-Matplotlib-11557C?style=for-the-badge" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Status-Exploratory%20Project-0A7B59?style=for-the-badge" alt="Exploratory project">
</p>

---

## 📌 Project overview

Traffic accidents are influenced by multiple conditions, including when an incident occurs, the type of road, weather, surface conditions, and visibility. This project explores a structured traffic-accident dataset and visualises patterns that can support further road-safety investigation.

The analysis currently focuses on four questions:

- Which days of the week have the most recorded accidents?
- How are accidents distributed by severity?
- Which weather conditions appear most often in the dataset?
- How are accidents distributed across lighting conditions?

> **Dataset note:** The repository contains a 1,000-row CSV covering records dated 2023–2024. Treat it as the supplied analysis dataset; its provenance and representativeness have not been independently verified. The charts describe this dataset, not official nationwide accident totals.

## ✨ Highlights

| Dataset snapshot | Value |
|---|---:|
| Accident records | **1,000** |
| Fields | **11** |
| Date range in file | **2023–2024** |
| Severity categories | **3** |
| Weather categories | **4** |
| Road categories | **3** |

### Severity distribution

| Severity | Records | Share |
|---|---:|---:|
| Minor | 591 | 59.1% |
| Severe | 308 | 30.8% |
| Fatal | 101 | 10.1% |

### Questions explored

- **Time patterns:** weekday distribution
- **Severity:** Minor, Severe, and Fatal categories
- **Weather:** Clear, Rain, Fog, and Snow
- **Lighting:** Daylight, Dawn/Dusk, Dark, and Dark with street lighting

## 📊 Visual results

The repository includes the chart exports generated for this analysis:

| Chart | Preview |
|---|---|
| Accidents by day of week | ![Accidents by day of week](task2graph1.png) |
| Accident severity distribution | ![Accident severity distribution](task2graph2.png) |
| Accidents by weather condition | ![Accidents by weather condition](task2graph3.png) |
| Accidents by light condition | ![Accidents by light condition](task2graph4.png) |

## 🧠 Extended analytics & dashboard

![Dataset insights infographic](docs/analytics_overview.svg)

The project now includes a modular analysis package and an interactive Streamlit application.

![RoadWatch system architecture](docs/architecture.svg)

### Dashboard features

- Interactive filters for year, severity, weather, and road type
- KPI cards for total, fatal, and severe/fatal records
- Interactive Plotly charts for severity, weekday, hourly, and monthly patterns
- Severity heatmaps by weather, road type, and lighting
- Folium coordinate explorer
- DBSCAN geographic clustering with adjustable radius and minimum cluster size
- CSV downloads for filtered records and cluster summaries
- Dataset quality checks

### Run the dashboard

```bash
streamlit run app.py
```

### Generate high-resolution chart assets

```bash
python generate_report.py
```

Charts are saved to `assets/generated/` (the generated output folder is intentionally excluded from Git).

### Run automated tests

```bash
pytest
```

## 🧰 Tech stack

- **Python** — analysis
- **Pandas** — CSV loading and aggregation
- **Matplotlib** — chart generation
- **Jupyter Notebook** — reproducible, step-by-step exploration

## 📁 Repository structure

```text
.
├── app.py
├── generate_report.py
├── Task2.ipynb
├── usa_traffic_accidents_2023_2024_1000.csv
├── task2graph1.png
├── task2graph2.png
├── task2graph3.png
├── task2graph4.png
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── analytics.py
│   └── visualizations.py
├── tests/
│   └── test_analysis.py
├── docs/
│   └── architecture.svg
└── README.md
```

## 🚀 Run the project locally

### 1. Clone the repository

```bash
git clone https://github.com/salianvikram/-Traffic-Accident-Hotspot-Analysis-.git
cd -Traffic-Accident-Hotspot-Analysis-
```

### 2. Create and activate a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the notebook

```bash
jupyter notebook Task2.ipynb
```

To launch the interactive dashboard instead:

```bash
streamlit run app.py
```

Run the notebook cells in order. Keep the CSV in the repository root.

## 🗂️ Dataset fields

| Field | Description |
|---|---|
| `Accident_ID` | Record identifier |
| `Date`, `Time` | Accident date and time |
| `Day_of_Week` | Day of the week |
| `Road_Type` | Rural, Urban, or Highway |
| `Surface_Condition` | Dry, Wet, or Snow |
| `Weather_Condition` | Clear, Rain, Fog, or Snow |
| `Light_Condition` | Daylight, Dawn/Dusk, Dark, or Dark_Lighted |
| `Accident_Severity` | Minor, Severe, or Fatal |
| `Latitude`, `Longitude` | Coordinate fields supplied with each record |

## 🔭 Future improvements

- Validate coordinate clusters against authoritative geographic data and documented dataset provenance.
- Add seasonal trend analysis and additional statistical significance checks.
- Evaluate predictive models only after sourcing a representative, well-documented dataset.
- Compare severity against weather, road, surface, and lighting conditions.
- Add data validation, missing-value checks, and reproducible analysis scripts.
- Document the dataset source and methodology before drawing real-world conclusions.

## ⚠️ Scope and limitations

This is an exploratory data-analysis project, not a validated crash-prediction or causal-inference model. A geographic hotspot analysis requires checking coordinate quality, geographic coverage, duplicate records, and the dataset's source. Counts and percentages should not be interpreted as population-level risk without exposure data (such as traffic volume) and a representative source.

## 👨‍💻 Author

**Vikram K. Salian**

- GitHub: [@salianvikram](https://github.com/salianvikram)

---

<p align="center">
  If you find this project useful, consider giving it a ⭐
</p>
