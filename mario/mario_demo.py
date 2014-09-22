import pandas as pd
import mario_viewer
from glue import qglue

data = pd.read_csv('mario_data.csv')
qglue(data=data)
