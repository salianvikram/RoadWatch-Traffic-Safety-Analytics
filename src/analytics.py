"""Statistical summaries and geographic clustering."""
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
DAY_ORDER=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
def kpi_summary(df):
    total=len(df); serious=int(df["Accident_Severity"].isin(["Severe","Fatal"]).sum())
    return {"total_accidents":total,"fatal_accidents":int((df["Accident_Severity"]=="Fatal").sum()),"severe_or_fatal":serious,"severe_or_fatal_pct":round(100*serious/total,1) if total else 0}
def hourly_summary(df):
    return df.dropna(subset=["Hour"]).groupby("Hour").size().reindex(range(24),fill_value=0).rename("Accidents").reset_index()
def weekday_summary(df):
    return df.groupby("Day_Name").size().reindex(DAY_ORDER,fill_value=0).rename_axis("Day").reset_index(name="Accidents")
def monthly_summary(df):
    x=df.dropna(subset=["Date"]).groupby(df["Date"].dt.to_period("M")).size().rename("Accidents").reset_index()
    x["Month"]=x["Date"].astype(str)
    return x.drop(columns="Date")
def cluster_hotspots(df,eps_km=8,min_samples=5):
    coords=df[["Latitude","Longitude"]].dropna()
    coords=coords[coords["Latitude"].between(-90,90)&coords["Longitude"].between(-180,180)]
    if len(coords)<min_samples:return pd.DataFrame(columns=["Cluster","Latitude","Longitude","Records"])
    labels=DBSCAN(eps=eps_km/6371.0088,min_samples=min_samples,metric="haversine").fit_predict(np.radians(coords.to_numpy()))
    grouped=coords.assign(Cluster=labels).query("Cluster >= 0")
    if grouped.empty:return pd.DataFrame(columns=["Cluster","Latitude","Longitude","Records"])
    return grouped.groupby("Cluster").agg(Latitude=("Latitude","mean"),Longitude=("Longitude","mean"),Records=("Cluster","size")).reset_index().sort_values("Records",ascending=False)
