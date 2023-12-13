import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import numpy as np

#streamlit run C:\Users\taice\OneDrive\PyCharmProjects\FirstClass\venv\Final.py
bikes = pd.read_csv("venv/bikes.csv")
stations = pd.read_csv("venv/current_bluebikes_stations (1).csv")

def startcoords(row):
    slat = row['start station latitude']
    slon = row['start station longitude']
    return f"{slat:.6f},{slon:.6f}"

def endcoords(row):
    elat = row['end station latitude']
    elon = row['end station longitude']
    return f"{elat:.6f},{elon:.6f}"

def scatter():
    st.title("Bike Stations Map")
    districts = stations['District'].unique()
    selecteddis = st.multiselect("Select District", districts)

    fig = px.scatter_mapbox(
        stations[stations['District'].isin(selecteddis)],
        lat='Latitude',
        lon='Longitude',
        text='Name',
        title="All Bike Stations",
        hover_data={'Name': True, 'Latitude': ':.4f', 'Longitude': ':.4f'},
        mapbox_style="carto-positron",
        center={"lat": stations[stations['District'].isin(selecteddis)]['Latitude'].mean(),
                "lon": stations[stations['District'].isin(selecteddis)]['Longitude'].mean()},
        zoom=12
    )

    fig.update_layout(showlegend=False, xaxis_visible=False, yaxis_visible=False)
    st.plotly_chart(fig)

def startstations():
    st.title("Popularity of Each Station as a Start")
    districts = stations['District'].unique()
    selecteddis = st.selectbox("Select District", districts)

    merge = pd.merge(bikes, stations, left_on='start station name', right_on='Name', how='left')
    mergedistrict = merge[merge['District'] == selecteddis]

    trips = mergedistrict.groupby('start station name').size().reset_index(name='trip_count')

    fig = px.bar(trips, x='start station name', y='trip_count',
                 title=f'Popularity of Each Station as a Start in {selecteddis}',
                 labels={'trip_count': 'Number of Trips', 'start station name': 'Station Name'},
                 color_discrete_sequence=['lavender'])
    fig.update_layout(height=900, width=700)
    st.plotly_chart(fig)

def endstations():
    st.title("Popularity of Each Station as an End")
    districts = stations['District'].unique()
    selecteddis = st.selectbox("Select District", districts)

    merge = pd.merge(bikes, stations, left_on='end station name', right_on='Name', how='left')
    mergedistrict = merge[merge['District'] == selecteddis]

    trips = mergedistrict.groupby('end station name').size().reset_index(name='trip_count')

    fig = px.bar(trips, x='end station name', y='trip_count',
                 title=f'Popularity of Each Station as an End in {selecteddis}',
                 labels={'trip_count': 'Number of Trips', 'end station name': 'Station Name'},
                 color_discrete_sequence=['lavender'])
    fig.update_layout(height=900, width=700)
    st.plotly_chart(fig)

def numbikes():
    st.title("Number of Bikes at Each Station")
    districts = stations['District'].unique()
    selecteddis = st.selectbox("Select District", districts)
    totalbike = stations.groupby(['District', 'Name'])['Total docks'].sum().reset_index()

    bikedistrict = totalbike[totalbike['District'] == selecteddis]

    fig = px.bar(bikedistrict, x='Name', y='Total docks',
                 labels={'Total docks': 'Number of Bikes', 'Name': 'Station Name'},
                 title=f'Number of Bikes at Each Station in {selecteddis}')
    st.plotly_chart(fig)

def line():
    st.title("Number of Bikes and Trips at Each Station")
    districts = stations['District'].unique()
    selecteddis = st.selectbox("Select District", districts)

    stationcount = bikes.groupby(['start station name', 'end station name']).size().reset_index(name='Total Trips')
    totaltrips = stationcount.groupby(['start station name', 'end station name'])['Total Trips'].sum().reset_index()

    merge = pd.merge(totaltrips, stations, left_on=['start station name', 'end station name'], right_on=['Name', 'Name'], how='left')
    merge = merge.groupby(['District', 'Name'])[['Total docks', 'Total Trips']].sum().reset_index()

    bikedistrict = merge[merge['District'] == selecteddis]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=bikedistrict['Name'], y=bikedistrict['Total docks'], mode='lines',
                             name='Number of Bikes'))
    fig.add_trace(go.Scatter(x=bikedistrict['Name'], y=bikedistrict['Total Trips'], mode='lines',
                             name='Total Trips'))
    fig.update_layout(xaxis_title='Station Name', yaxis_title='Count',
                      title=f'Number of Bikes and Trips at Each Station in {selecteddis}')

    st.plotly_chart(fig)

def userpie():
    st.title("User Type Distribution")
    usercount = bikes['usertype'].value_counts()

    fig = px.pie(usercount, values=usercount.values, names=usercount.index,
                 title='Percentage of Subscribers vs Customers',
                 labels={'usertype': 'User Type'},
                 hole=0,
                 color_discrete_sequence=['rgb(204,235,197)', 'rgb(222,203,228)'])
    st.plotly_chart(fig)

def genderpie():
    st.title("User Type Gender Distribution")
    usercount = bikes['gender'].value_counts()

    fig = px.pie(usercount, values=usercount.values, names=usercount.index,
                 title='Percentage of Gender',
                 labels={'gender': 'Gender'},
                 hole=0,
                 color_discrete_sequence=['rgb(179,205,227)', 'rgb(222,203,228)', 'grey'])
    st.plotly_chart(fig)

def birthyear():
    st.title("Birth Year Distribution")
    bikes['birth year'] = pd.to_numeric(bikes['birth year'], errors='coerce')
    start = st.slider("Select Start Year", 1900, 1996, 1900)
    end = st.slider("Select End Year", 1900, 1996, 1996)

    emptydata = bikes[(bikes['birth year'].notna()) & (bikes['birth year'].between(start, end))]

    fig = px.histogram(emptydata, x='birth year', title=f'Birth Year Distribution ({start}-{end})',
                       color_discrete_sequence=['seashell'])
    fig.update_layout(xaxis_title='Birth Year', yaxis_title='Count')
    fig.update_traces(marker_line_color='black', marker_line_width=1.5)
    st.plotly_chart(fig)

def deployyear():
    st.title("Deployment Year Distribution by Districts")
    selecteddis = st.selectbox("Select District(s)", stations['District'].unique())
    filter = stations[stations['District'].isin([selecteddis])]

    fig = px.bar(filter, x='Name', y='Deployment Year',
                       title=f'Deployment Year Distribution ({selecteddis})',
                       color_discrete_sequence=['seashell'])
    fig.update_layout(xaxis_title='Station Name', yaxis_title='Deployment Year')
    fig.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig.update_layout(height=900, width=700)
    fig.update_layout(yaxis_range=[2010, 2024])
    st.plotly_chart(fig)

def main():
    logo = "venv/download.jpeg"
    st.image(logo, use_column_width=False, width=100)
    st.title("Welcome to Boston Blue Bikes")

    st.write("Use the sidebar to navigate.")

    page = st.sidebar.radio("Select Page",["Welcome", "Station Map", "Start Stations", "End Stations", "Number of Bikes", "Number of Bikes and Trips",
        "User Type Distribution", "User Type Gender Distribution", "Birth Year Distribution", "Deployment Year Distribution by Districts"])

    if page == "Welcome":
        st.text("Taice Brenner - CS230")
        bikepic = "venv/Bluebikes Dock 800px-09.png"
        st.image(bikepic, use_column_width=False, width=300)
    else:
        if page == "Station Map":
            scatter()
        elif page == "Start Stations":
            startstations()
        elif page == "End Stations":
            endstations()
        elif page == "Number of Bikes":
            numbikes()
        elif page == "Number of Bikes and Trips":
            line()
        elif page == "User Type Distribution":
            userpie()
        elif page == "User Type Gender Distribution":
            genderpie()
        elif page == "Birth Year Distribution":
            birthyear()
        elif page == "Deployment Year Distribution by Districts":
            deployyear()

main()