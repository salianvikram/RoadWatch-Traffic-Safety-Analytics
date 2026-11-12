import pandas as pd
from src.analytics import kpi_summary,hourly_summary,cluster_hotspots
def sample():
    return pd.DataFrame({"Date":pd.to_datetime(["2024-01-01","2024-01-02","2024-01-03"]),"Hour":[8,9,8],"Accident_Severity":["Minor","Severe","Fatal"],"Latitude":[37,37.001,37.002],"Longitude":[-122,-122.001,-122.002]})
def test_kpis():
    result=kpi_summary(sample());assert result["total_accidents"]==3;assert result["fatal_accidents"]==1;assert result["severe_or_fatal"]==2
def test_hourly_aggregation():
    result=hourly_summary(sample());assert len(result)==24;assert result.loc[result.Hour==8,"Accidents"].iloc[0]==2
def test_geographic_cluster():
    result=cluster_hotspots(sample(),eps_km=2,min_samples=2);assert not result.empty;assert result.iloc[0].Records==3
