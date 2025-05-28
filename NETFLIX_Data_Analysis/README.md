# 📊 Netflix Data Analysis Dashboard with Power BI

![Netflix Logo](https://upload.wikimedia.org/wikipedia/commons/6/69/Netflix_logo.svg)

## 🎯 Project Overview

This project presents an end-to-end data analysis and visualization of the Netflix Movies and TV Shows dataset sourced from [Kaggle](https://www.kaggle.com/datasets/rahulvyasm/netflix-movies-and-tv-shows). It explores trends in content types, production countries, genres, and release timelines through a fully interactive Power BI dashboard.

---

## 📁 Folder Structure

| Folder      | Description                                         |
|-------------|-----------------------------------------------------|
| `data/`     | Contains the Netflix dataset (`NETFLIX.csv`)        |
| `notebooks/`| Python script used for initial data cleaning        |
| `ppt/`      | PowerPoint presentation prepared for this project   |
| `visuals/`  | PDF/PNG snapshots of the Power BI dashboard         |

---

## ⚙️ Tools Used

- **Python (Pandas)** – Initial data cleaning
- **Power Query (Power BI)** – Splitting, transformation, and modeling
- **Power BI** – Data visualization and DAX exploration
- **DAX** – Created custom measures to analyze trends

---

## 🧹 Data Preparation

- Removed nulls in `Date_Added`, `Director`, `Rating`
- Split comma-separated columns like `Cast`, `Director`, and `Listed_In` into rows
- Built separate related tables for Director, Cast, and Genre
- Converted `Duration` into minutes for Movies
- Ensured valid data types (e.g., Date, Integer)

---

## 📊 Key Metrics

- **Total Titles**: 8,798  
- **Movies**: 6,122  
- **TV Shows**: 2,676  
- **Unique Directors**: 4,991  
- **Genres**: 47  
- **Data Range**: 2008 – 2024

---

## 📈 Dashboard Insights

- 📅 **Content Growth**: Netflix’s library grew rapidly post-2015
- 🌍 **Top Producers**: US and India dominate content creation
- 🎭 **Genres**: International Movies, Dramas, and Comedies lead
- ⏱️ **Durations**: Most movies are between 80–110 minutes

![Dashboard Preview](NETFLIX_Data_Analysis/NETFLIX_DASHBOARD 1.png)

---

## 🧠 DAX Measures Highlights

- `Total_Movie`
- `Total_TVshows`
- `Start_Year`, `End_Year`
- `Total_Directors`, `Total_Country`, `Total_Caste`
- Custom count measures using `CALCULATE`, `DISTINCTCOUNT`, etc.

---

## 🚧 Challenges & Solutions

| Challenge                      | Solution                                |
|-------------------------------|-----------------------------------------|
| Multiple directors per row    | Used Power Query to split rows          |
| Duplicate titles/descriptions | Removed duplicates via Pandas           |
| Unstructured genre values     | Normalized into a lookup table          |
| Filtering across tables       | Managed using proper model relationships|

---

## 📽️ Final Presentation

Find the summary deck inside `ppt/`:
- 📁 `Netflix-Data-Analysis-Dashboard.pptx`

---

## 🔗 References

- [Netflix Dataset - Kaggle](https://www.kaggle.com/datasets/rahulvyasm/netflix-movies-and-tv-shows)
- [Power BI Desktop](https://powerbi.microsoft.com/desktop)

---

## 📬 Let's Connect

If you enjoyed this project or want to collaborate, feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/priya-mohan-058b79208/)!

---

## 🏷️ Tags

`#PowerBI` `#Python` `#DataAnalysis` `#NetflixProject` `#DAX` `#DataVisualization` `#Portfolio`

