# store_app.py

import streamlit as st
from google.cloud import bigquery
import pandas as pd
import plotly.express as px

def main():
    # Google Cloud 서비스 계정 JSON 파일의 경로
    credentials_path = ".\json\streamlit-telecom-8dd3bc024a0e.json"
    client = bigquery.Client.from_service_account_json(credentials_path)

    # BigQuery 쿼리 실행
    query = "SELECT * FROM your_dataset.your_table"
    df = client.query(query).to_dataframe()

    # 지도에 위치 표시
    st.map(df)

    # 데이터 표시
    st.write(df)

if __name__ == "__main__":
    main()