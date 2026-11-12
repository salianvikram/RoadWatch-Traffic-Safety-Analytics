"""Streamlit dashboard for traffic accident exploration."""
from pathlib import Path
import streamlit as st
import folium
from streamlit_folium import st_folium
from src.data_processing import load_data,validate_data
from src.analytics import kpi_summary,cluster_hotspots
from src.visualizations import severity_chart,hourly_chart,weekday_chart,monthly_chart,factor_heatmap
ROOT=Path(__file__).resolve().parent
DATA=ROOT/"usa_traffic_accidents_2023_2024_1000.csv"
st.set_page_config(page_title="RoadWatch | Accident Intelligence",page_icon="🚦",layout="wide")
st.markdown("""<style>.stApp{background:radial-gradient(circle at 10% 0%,#172554 0,#0b1220 40%,#080d18 100%)}[data-testid="stMetric"]{background:#111c2e;border:1px solid #26364f;padding:16px;border-radius:14px}[data-testid="stMetricValue"]{color:#7dd3fc}.block-container{padding-top:2rem}</style>""",unsafe_allow_html=True)
st.sidebar.title("🚦 RoadWatch")
st.sidebar.caption("Traffic Accident Intelligence")
if not DATA.exists():st.error(f"Dataset not found: {DATA}");st.stop()
@st.cache_data
def get_data(path,stamp):return load_data(path)
df=get_data(str(DATA),DATA.stat().st_mtime)
st.sidebar.header("Filters")
years=sorted(df.Year.dropna().astype(int).unique())
sev=sorted(df.Accident_Severity.dropna().unique())
weather=sorted(df.Weather_Condition.dropna().unique())
roads=sorted(df.Road_Type.dropna().unique())
ys=st.sidebar.multiselect("Year",years,default=years)
ss=st.sidebar.multiselect("Severity",sev,default=sev)
ws=st.sidebar.multiselect("Weather",weather,default=weather)
rs=st.sidebar.multiselect("Road type",roads,default=roads)
d=df[df.Year.isin(ys)&df.Accident_Severity.isin(ss)&df.Weather_Condition.isin(ws)&df.Road_Type.isin(rs)].copy()
st.title("RoadWatch — Traffic Accident Intelligence")
st.caption("Explore accident patterns, severity, environmental conditions and coordinate clusters.")
if d.empty:st.warning("No records match these filters.");st.stop()
k=kpi_summary(d);c=st.columns(4)
c[0].metric("Recorded accidents",f"{k['total_accidents']:,}")
c[1].metric("Fatal accidents",f"{k['fatal_accidents']:,}")
c[2].metric("Severe + fatal",f"{k['severe_or_fatal']:,}")
c[3].metric("Severe/fatal share",f"{k['severe_or_fatal_pct']}%")
overview,patterns,mapping,quality=st.tabs(["Overview","Time & conditions","Hotspot explorer","Data quality"])
with overview:
    a,b=st.columns(2);a.plotly_chart(severity_chart(d),use_container_width=True);b.plotly_chart(weekday_chart(d),use_container_width=True)
    st.plotly_chart(factor_heatmap(d,"Weather_Condition"),use_container_width=True)
with patterns:
    a,b=st.columns(2);a.plotly_chart(hourly_chart(d),use_container_width=True);b.plotly_chart(monthly_chart(d),use_container_width=True)
    a,b=st.columns(2);a.plotly_chart(factor_heatmap(d,"Road_Type"),use_container_width=True);b.plotly_chart(factor_heatmap(d,"Light_Condition"),use_container_width=True)
with mapping:
    st.subheader("Accident coordinate explorer")
    geo=d.dropna(subset=["Latitude","Longitude"])
    geo=geo[geo.Latitude.between(-90,90)&geo.Longitude.between(-180,180)]
    if geo.empty:st.info("No valid coordinates for current filters.")
    else:
        m=folium.Map(location=[geo.Latitude.mean(),geo.Longitude.mean()],zoom_start=4,tiles="CartoDB dark_matter")
        for _,r in geo.head(1500).iterrows():
            folium.CircleMarker([r.Latitude,r.Longitude],radius=4,color="#38BDF8",fill=True,fill_opacity=.65,popup=f"ID {r.Accident_ID} · {r.Accident_Severity}").add_to(m)
        st_folium(m,use_container_width=True,height=520)
    st.markdown("#### DBSCAN hotspot clustering")
    a,b=st.columns(2);eps=a.slider("Radius (km)",1,50,8);minimum=b.slider("Minimum records",2,30,5)
    clusters=cluster_hotspots(d,eps,minimum)
    if clusters.empty:st.info("No clusters found. Adjust radius or minimum records.")
    else:
        st.dataframe(clusters,use_container_width=True,hide_index=True)
        st.download_button("Download cluster CSV",clusters.to_csv(index=False),"hotspot_clusters.csv","text/csv")
with quality:
    st.subheader("Dataset quality report");st.json(validate_data(df))
    st.download_button("Download filtered records",d.to_csv(index=False),"filtered_accidents.csv","text/csv")
st.divider()
st.caption("Exploratory analysis only. The supplied dataset's provenance and representativeness have not been independently verified.")
