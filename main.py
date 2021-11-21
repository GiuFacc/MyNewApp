import streamlit as st
import numpy as np
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(layout="wide")

col3 = st.container()
col4 = st.container()
col1, col2 = st.columns([5,4])
with col3:
    st.markdown("<h1 style='text-align: center; color: #F4F5F5;'>DATABASE VISUALIZATION APP</h1>", unsafe_allow_html=True)

    st.sidebar.header("Upload your CSV or Excel file")

    uploaded_file = st.sidebar.file_uploader(label='', type=['csv', 'xlsx', 'xlsm'])

global df

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        df = pd.read_csv(uploaded_file, sep=';')

    with col1:
        st.header("Database:")
        st.markdown("Mostra il database")

    with col2:
        st.header("Pivot table:")
        st.markdown("Mostra il totale delle ore per nome, luogo e mese dell'anno")

    name = df['Nome'].unique()
    places = df['Luogo'].unique()
    dates = df['mm/aaaa'].unique()

    with col3:
        st.header('Visualization settings:')
        container = st.container()
        container2 = container.container()
        all = container.checkbox("Select all")

        if all:
            name_select = container.multiselect('Nome', sorted(name), sorted(name))
            place_select = container.multiselect('Luogo', sorted(places), sorted(places))
            date_select = container.multiselect('Mese/Anno', sorted(dates), sorted(dates))

            with col1:
                st.dataframe(df.style.format(precision=1), width=1000, height=704)
            with col2:
                table = pd.pivot_table(df, values='Totale', index=['Nome', 'mm/aaaa'],
                                       columns=['Luogo'], aggfunc=np.sum)
                col2.dataframe(table.style.format(formatter="{:.1f}", na_rep='-'), height=704)

        else:
            name_select = container.multiselect('Nome', sorted(name))
            place_select = container.multiselect('Luogo', sorted(places))
            date_select = container.multiselect('Mese/Anno', sorted(dates))

            if name_select:
                database = df['Nome'].isin(name_select)
                table = df['Nome'].isin(name_select)
                df2 = df[database]
                places1 = df2['Luogo'].unique()
                dates1 = df2['mm/aaaa'].unique()
                place_old = container.subheader('Luoghi disponibili: ')
                place_old_2 = container.text(' - '.join(sorted(places1)))
                date_old = container.subheader('Date disponibili: ')
                date_old_2 = container.text(' - '.join(sorted(dates1)))
                if place_select:
                    database = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select)
                    table = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select)
                    df2 = df[database]
                    dates1 = df2['mm/aaaa'].unique()
                    place_old.empty()
                    place_old_2.empty()
                    date_old.empty()
                    date_old_2.empty()
                    container.subheader('Date disponibili: ')
                    container.text(' - '.join(sorted(dates1)))
                    if date_select:
                        database = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(
                            date_select)
                        table = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(
                            date_select)
                elif date_select:
                    database = df['Nome'].isin(name_select) & df['mm/aaaa'].isin(date_select)
                    table = df['Nome'].isin(name_select) & df['mm/aaaa'].isin(date_select)
                    df2 = df[database]
                    places1 = df2['Luogo'].unique()
                    date_old.empty()
                    date_old_2.empty()
                    place_old.empty()
                    place_old_2.empty()
                    container.subheader('Luoghi disponibili: ')
                    container.text(' - '.join(sorted(places1)))
                    if place_select:
                        database = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(
                            date_select)
                        table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)

                df1 = df[table]
                df2 = df[database]

                with col1:
                    st.dataframe(df2.style.format(precision=1), width=1000, height=745)
                with col2:
                    table = pd.pivot_table(df1, values='Totale', index=['Nome', 'Luogo'],
                                           columns=['mm/aaaa'], aggfunc=np.sum)
                    col2.dataframe(table.style.format(formatter="{:.1f}", na_rep='-'), height=704)

            elif place_select:
                database = df['Luogo'].isin(place_select)
                table = df['Luogo'].isin(place_select)
                df2 = df[database]
                name1 = df2['Nome'].unique()
                dates1 = df2['mm/aaaa'].unique()
                name_old = container.subheader('Nomi disponibili: ')
                name_old_2 = container.text(' - '.join(sorted(name1)))
                date_old = container.subheader('Date disponibili: ')
                date_old_2 = container.text(' - '.join(sorted(dates1)))
                if name_select:
                    database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select)
                    table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select)
                    df2 = df[database]
                    dates1 = df2['mm/aaaa'].unique()
                    name_old.empty()
                    name_old_2.empty()
                    date_old.empty()
                    date_old_2.empty()
                    container.subheader('Date disponibili: ')
                    container.text(' - '.join(sorted(dates1)))
                    if date_select:
                        database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)
                        table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)
                elif date_select:
                    database = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
                    table = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
                    df2 = df[database]
                    name1 = df2['Nome'].unique()
                    date_old.empty()
                    date_old_2.empty()
                    name_old.empty()
                    name_old_2.empty()
                    container.subheader('Nomi disponibili: ')
                    container.text(' - '.join(sorted(name1)))
                    if name_select:
                        database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)
                        table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)

                df1 = df[table]
                df2 = df[database]

                with col1:
                    st.dataframe(df2.style.format(precision=1), width=1000, height=704)

                with col2:
                    table = pd.pivot_table(df1, values='Totale', index=['Nome', 'Luogo'],
                                           columns=['mm/aaaa'], aggfunc=np.sum)
                    col2.dataframe(table.style.format(formatter="{:.1f}", na_rep='-'), height=704)

            elif date_select:
                database = df['mm/aaaa'].isin(date_select)
                table = df['mm/aaaa'].isin(date_select)
                df2 = df[database]
                name1 = df2['Nome'].unique()
                places1 = df2['Luogo'].unique()
                name_old = container.subheader('Nomi disponibili: ')
                name_old_2 = container.text(' - '.join(sorted(name1)))
                places_old = container.subheader('Luoghi disponibili: ')
                places_old_2 = container.text(' - '.join(sorted(places1)))
                if name_select:
                    database = df['mm/aaaa'].isin(date_select) & df['Nome'].isin(name_select)
                    table = df['mm/aaaa'].isin(date_select) & df['Nome'].isin(name_select)
                    df2 = df[database]
                    dates1 = df2['mm/aaaa'].unique()
                    name_old.empty()
                    name_old_2.empty()
                    places_old.empty()
                    places_old_2.empty()
                    container.subheader('Date disponibili: ')
                    container.text(' - '.join(sorted(dates1)))
                    if place_select:
                        database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)
                        table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)
                elif place_select:
                    database = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
                    table = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
                    df2 = df[database]
                    name1 = df2['Nome'].unique()
                    name_old.empty()
                    name_old_2.empty()
                    places_old.empty()
                    places_old_2.empty()
                    container.subheader('Nomi disponibili: ')
                    container.text(' - '.join(sorted(name1)))
                    if name_select:
                        database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)
                        table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                            date_select)

                df1 = df[table]
                df2 = df[database]

                with col1:
                    st.dataframe(df2.style.format(precision=1), width=1000, height=704)

                with col2:
                    table = pd.pivot_table(df1, values='Totale', index=['Nome', 'Luogo'],
                                           columns=['mm/aaaa'], aggfunc=np.sum)
                    col2.dataframe(table.style.format(formatter="{:.1f}", na_rep='-'), height=704)
