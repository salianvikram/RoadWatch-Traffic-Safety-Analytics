"""Generate polished static chart assets from the CSV."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"assets"/"generated";OUT.mkdir(parents=True,exist_ok=True)
df=pd.read_csv(ROOT/"usa_traffic_accidents_2023_2024_1000.csv")
df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
df["Hour"]=pd.to_datetime(df["Time"],format="%H:%M",errors="coerce").dt.hour
sns.set_theme(style="darkgrid",context="talk")
def save(fig,name):
    fig.savefig(OUT/name,dpi=220,bbox_inches="tight");plt.close(fig);print("Saved",OUT/name)
fig,ax=plt.subplots(figsize=(12,6));order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
df.Day_of_Week.value_counts().reindex(order).plot.bar(ax=ax,color="#38BDF8");ax.set(title="Traffic accidents by weekday",xlabel="Day",ylabel="Records");save(fig,"weekday_trend.png")
fig,ax=plt.subplots(figsize=(9,7));df.Accident_Severity.value_counts().plot.pie(ax=ax,autopct="%1.1f%%",wedgeprops={"width":.42});ax.set_ylabel("");ax.set_title("Accident severity distribution");save(fig,"severity_distribution.png")
for factor,name in [("Weather_Condition","weather_severity.png"),("Light_Condition","lighting_severity.png"),("Road_Type","road_severity.png"),("Surface_Condition","surface_severity.png")]:
    fig,ax=plt.subplots(figsize=(11,6));pd.crosstab(df[factor],df.Accident_Severity).plot.bar(stacked=True,ax=ax);ax.set(title=f"Severity by {factor.replace('_',' ')}",ylabel="Records");save(fig,name)
fig,ax=plt.subplots(figsize=(12,6));df.groupby(df.Date.dt.to_period("M")).size().plot(ax=ax,marker="o",color="#8B5CF6");ax.set(title="Monthly accident trend",ylabel="Records",xlabel="Month");save(fig,"monthly_trend.png")
fig,ax=plt.subplots(figsize=(12,6));df.groupby("Hour").size().reindex(range(24),fill_value=0).plot(ax=ax,marker="o",color="#0EA5E9");ax.set(title="Accidents by hour",xlabel="Hour of day",ylabel="Records");save(fig,"hourly_trend.png")
