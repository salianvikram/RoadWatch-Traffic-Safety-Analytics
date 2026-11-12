"""Data loading and validation."""
import pandas as pd
from pathlib import Path
REQUIRED_COLUMNS = {'Accident_ID','Date','Time','Day_of_Week','Road_Type','Surface_Condition','Weather_Condition','Light_Condition','Accident_Severity','Latitude','Longitude'}
def load_data(path):
    path=Path(path)
    if not path.exists(): raise FileNotFoundError(f'Dataset not found: {path}')
    df=pd.read_csv(path)
    missing=REQUIRED_COLUMNS-set(df.columns)
    if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')
    df['Hour']=pd.to_datetime(df['Time'],format='%H:%M',errors='coerce').dt.hour
    df['Month']=df['Date'].dt.month
    df['Year']=df['Date'].dt.year
    df['Day_Name']=df['Date'].dt.day_name()
    df['Latitude']=pd.to_numeric(df['Latitude'],errors='coerce')
    df['Longitude']=pd.to_numeric(df['Longitude'],errors='coerce')
    return df.drop_duplicates(subset=['Accident_ID']).copy()
def validate_data(df):
    return {'rows':len(df),'missing_dates':int(df['Date'].isna().sum()),'missing_coordinates':int(df[['Latitude','Longitude']].isna().any(axis=1).sum()),'invalid_latitudes':int((~df['Latitude'].between(-90,90)).fillna(True).sum()),'invalid_longitudes':int((~df['Longitude'].between(-180,180)).fillna(True).sum())}
