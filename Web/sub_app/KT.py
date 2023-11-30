import streamlit as st
import pandas as pd
import folium
from folium.plugins import LocateControl
import requests
from io import BytesIO

def main():
    file_path = r'https://github.com/DongWonC/telecom_deploy/raw/main/Web/data/KT.xlsx'
    response = requests.get(file_path)
    
    if response.status_code == 200:
        # Read the Excel file into a Pandas DataFrame
        df = pd.read_excel(BytesIO(response.content))
        print(df.head())
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

    api_key = 'AIzaSyBUqEmTNUfF0SzDnnFuXSo0y2sx_-pn5y4'

    m = folium.Map(location=[37.5665, 126.9780], zoom_start=15)

    for index, row in df.iterrows():
        name = row['장소']
        address = row['주소']

        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}')
        data = response.json()

        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            lat, lng = location['lat'], location['lng']

            html_popup = f'<strong>{name}</strong><br>{address}<br>'
            icon = folium.CustomIcon(icon_image=r'https://github.com/DongWonC/telecom_deploy/raw/main/Web/image/blue_marker.png', icon_size=(60, 60))

            folium.Marker(location=[lat, lng], icon=icon, popup=folium.Popup(html_popup, max_width=300)).add_to(m)

    lc = LocateControl()
    lc.add_to(m)

    st.title('지도를 통해 가까운 디지털 배움터 장소를 확인해보세요!')
    st.components.v1.html(m._repr_html_(), height=600)
    st.write(m)

if __name__ == "__main__":
    main()