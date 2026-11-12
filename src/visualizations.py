"""Reusable interactive Plotly visualizations."""
import plotly.express as px
import plotly.graph_objects as go
from .analytics import hourly_summary,weekday_summary,monthly_summary
def theme(fig,title):
    fig.update_layout(title=title,template="plotly_dark",paper_bgcolor="#0B1220",plot_bgcolor="#0B1220",font=dict(color="#E5E7EB"),margin=dict(l=18,r=18,t=55,b=18))
    fig.update_xaxes(showgrid=False);fig.update_yaxes(gridcolor="rgba(148,163,184,.16)")
    return fig
def severity_chart(df):
    d=df["Accident_Severity"].value_counts().rename_axis("Severity").reset_index(name="Accidents")
    return theme(px.pie(d,names="Severity",values="Accidents",hole=.62,color_discrete_sequence=["#38BDF8","#F97316","#F43F5E"]),"Accident severity")
def hourly_chart(df):
    return theme(px.area(hourly_summary(df),x="Hour",y="Accidents",markers=True),"Accidents by hour")
def weekday_chart(df):
    return theme(px.bar(weekday_summary(df),x="Day",y="Accidents",color="Accidents",color_continuous_scale="Blues"),"Accidents by weekday")
def monthly_chart(df):
    return theme(px.line(monthly_summary(df),x="Month",y="Accidents",markers=True),"Monthly accident trend")
def factor_heatmap(df,factor):
    table=df.groupby([factor,"Accident_Severity"]).size().unstack(fill_value=0)
    fig=go.Figure(go.Heatmap(z=table.values,x=table.columns.tolist(),y=table.index.tolist(),colorscale="Blues",text=table.values,texttemplate="%{text}"))
    return theme(fig,f"Severity by {factor.replace('_',' ').title()}")
