import csv
import pandas as pd
import plotly.graph_objects as pg

df = pd.read_csv("data1.csv")

studentData = df.loc[df["student_id"]=="TRL_987"]
print(studentData.groupby("level")["attempt"].mean())

fig=pg.Figure(pg.Bar(
    x=studentData.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"    
))

fig.show()