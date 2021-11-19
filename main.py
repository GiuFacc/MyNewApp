import numpy as np
import streamlit as st
import pandas as pd

#st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(layout="wide")

col3 = st.container()
col1, col2 = st.columns([5,3])
with col3:
    st.markdown("<h1 style='text-align: center; color: #F4F5F5;'>DATABASE VISUALIZATION APP</h1>", unsafe_allow_html=True)

    st.sidebar.header("Upload your CSV or Excel file")

    uploaded_file = st.sidebar.file_uploader(label='', type=['csv', 'xlsx', 'xlsm'])

    global df

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            df = pd.read_excel(uploaded_file)

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
    all_names = st.button('Tutti', help='Mostra la tabella pivot intera')
    clear = st.button('Clear', help='Ripristina le opzioni\n\nVa cliccato dopo tutti')

    if all_names:
        name_select = st.multiselect('Nome', sorted(name), sorted(name))
        place_select = st.multiselect('Luogo', sorted(places), sorted(places))
        date_Select = st.multiselect('Mese/Anno', sorted(dates), sorted(dates))

        with col1:
            st.dataframe(df.style.format(precision=1), width=1000, height=704)
        with col2:
            table = pd.pivot_table(df, values='Totale', index=['Nome', 'Luogo'],
                                   columns=['mm/aaaa'], aggfunc=np.sum, margins=True,
                                   margins_name='TOTALE')

    else:
        name_select = st.multiselect('Nome', sorted(name))
        place_select = st.multiselect('Luogo', sorted(places))
        date_select = st.multiselect('Mese/Anno', sorted(dates))

        if name_select:
            database = df['Nome'].isin(name_select)
            table = df['Nome'].isin(name_select)
            if place_select:
                database = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select)
                table = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select)
                if date_select:
                    database = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(
                        date_select)
                    table = df['Nome'].isin(name_select) & df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(
                        date_select)
            elif date_select:
                database = df['Nome'].isin(name_select) & df['mm/aaaa'].isin(date_select)
                table = df['Nome'].isin(name_select) & df['mm/aaaa'].isin(date_select)
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

        elif place_select:
            database = df['Luogo'].isin(place_select)
            table = df['Luogo'].isin(place_select)
            if name_select:
                database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select)
                table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select)
                if date_select:
                    database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                        date_select)
                    table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                        date_select)
            elif date_select:
                database = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
                table = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
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

        elif date_select:
            database = df['mm/aaaa'].isin(date_select)
            table = df['mm/aaaa'].isin(date_select)
            if name_select:
                database = df['mm/aaaa'].isin(date_select) & df['Nome'].isin(name_select)
                table = df['mm/aaaa'].isin(date_select) & df['Nome'].isin(name_select)
                if place_select:
                    database = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                        date_select)
                    table = df['Luogo'].isin(place_select) & df['Nome'].isin(name_select) & df['mm/aaaa'].isin(
                        date_select)
            elif place_select:
                database = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
                table = df['Luogo'].isin(place_select) & df['mm/aaaa'].isin(date_select)
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

