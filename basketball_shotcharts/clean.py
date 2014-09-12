"""
Data comes from
http://vorped.com/bball/index.php/

By copying the shots js variable on one of the shot charts pages
"""

from json import load
import pandas as pd
import numpy as np

files = {'Tim Duncan': 'duncan_2013.json',
         'LeBron James': 'lebron_2013.json',
         'Kawhi Leonard': 'leonard_2013.json',
         'Tony Parker': 'parker_2013.json',
         'Dwyane Wade': 'wade_2013.json',
         'Manu Ginobili': 'ginobili_2013.json',
         }

dfs = []
for name, path in files.items():
    df = pd.DataFrame(load(open(path)))
    df['player'] = name
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True).convert_objects(convert_numeric=True)
df['is_home'] = df.ish
df['margin'] = df.mgn
df['period'] = df.p
df['shot_made'] = df.shm
df['game_id'] = np.searchsorted(df.gid.unique(), df.gid)

shots = np.array(['', 'Tip', 'Dunk', 'Jump Shot',
                 'Special Jump Shot', 'Alleyoop', 'Hook', 'Layup'])
df['shot_type'] = shots[df['st'].values]

cols = ['player', 'game_id', 'is_home', 'margin', 'period', 'shot_made',
        'shot_type', 'x', 'y']
df = df[cols]

df.to_csv('shots.csv', index=False)
