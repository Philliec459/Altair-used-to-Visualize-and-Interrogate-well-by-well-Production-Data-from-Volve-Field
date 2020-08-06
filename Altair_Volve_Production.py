#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:26:14 2020

@author: craig
"""

from pandas import DataFrame, read_csv

import altair as alt
alt.renderers.enable('altair_viewer')

import pandas as pd
import numpy as np



#read the file
#file = r'Volve production data_Monthly_brief_Query2.xlsx'
file = r'Query3.xlsx'
df = pd.read_excel(file,index_col=False)


interval = alt.selection_interval()

base = alt.Chart(df).properties(
    width=350,
    height=350, 
).add_selection(interval)

points = base.mark_point(filled=True, size=1000).encode(
    x='XX_Bottom:Q',
    y='YY_Bottom:Q',
    size='BOPD:Q',
    #color=alt.condition(interval, 'Well_Name', alt.value('lightgray')),
    color=alt.condition(interval, 'Well_Name', alt.value('lightgray')),
    tooltip='Well_Name', 
).properties(
    title='Volve Field Map',
    selection=interval


)

timeseries = base.mark_line().encode(
    x='Date',
    y=alt.Y('BOPD', scale=alt.Scale(domain=(0, 40000))),
    color=alt.Color('Well_Name:O')
    
).properties(
    title='Volve Production by Well in BOPD',
    #selection=interval
).transform_filter(
    #title='Volve Field BOPD',    
    interval
)

hist = alt.Chart(df).mark_bar().encode(
    x='sum(BOPM)',
    y='Well_Name',
    color='Well_Name'
).properties(
    width=700,
    height=80
).transform_filter(
    interval
)

hist2 = alt.Chart(df).mark_bar().encode(
    x='sum(BWPM)',
    y='Well_Name',
    color='Well_Name'
).properties(
    width=700,
    height=80
).transform_filter(
    interval
)

hist3 = alt.Chart(df).mark_bar().encode(
    x='sum(beGpm)',
    y='Well_Name',
    color='Well_Name'
).properties(
    width=700,
    height=80
).transform_filter(
    interval
)



plot =  points.encode() | timeseries.encode()  | hist.encode() & hist2.encode() & hist3.encode()


plot.show()  