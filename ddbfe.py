import streamlit as st
import duckdb
import os
import pandas as pd

def get_duckdb_metadata(db_path):
    try:
        con = duckdb.connect(database=db_path, read_only=True)
        tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'").fetchall()
        table_names = [table[0] for table in tables]
        
        table_info = []
        for table in table_names:
            row_count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            table_info.append((table, row_count))
        
        con.close()
        return table_info
    except Exception as e:
        return str(e)

def get_table_schema(db_path, table_name):
    try:
        con = duckdb.connect(database=db_path, read_only=True)
        schema = con.execute(f"PRAGMA table_info({table_name})").fetchall()
        con.close()
        return schema
    except Exception as e:
        return str(e)

def get_table_data(db_path, table_name, limit=100):
    try:
        con = duckdb.connect(database=db_path, read_only=True)
        data = con.execute(f"SELECT * FROM {table_name} LIMIT {limit}").fetchdf()
        con.close()
        return data
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("DuckDB Explorer")

uploaded_file = st.file_uploader("Upload a DuckDB file", type=["db"])

if uploaded_file:
    file_path = os.path.join("/tmp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File {uploaded_file.name} uploaded successfully!")
    
    file_size = os.path.getsize(file_path)
    st.write(f"**File Size:** {file_size / (1024 * 1024):.2f} MB")
    
    metadata = get_duckdb_metadata(file_path)
    
    if isinstance(metadata, str):
        st.error(f"Error reading database: {metadata}")
    else:
        st.write(f"**Number of Tables:** {len(metadata)}")
        
        if metadata:
            df_meta = pd.DataFrame(metadata, columns=["Table Name", "Row Count"])
            st.dataframe(df_meta)
            
            selected_table = st.selectbox("Select a table to view details", df_meta["Table Name"].tolist())
            
            if selected_table:
                st.subheader(f"Schema of {selected_table}")
                schema = get_table_schema(file_path, selected_table)
                if isinstance(schema, str):
                    st.error(f"Error fetching schema: {schema}")
                else:
                    df_schema = pd.DataFrame(schema, columns=["Column ID", "Name", "Type", "Nullable", "Default", "Extra"])
                    st.dataframe(df_schema)
                    
                st.subheader(f"Data from {selected_table}")
                data = get_table_data(file_path, selected_table)
                if isinstance(data, str):
                    st.error(f"Error fetching data: {data}")
                else:
                    st.dataframe(data)
