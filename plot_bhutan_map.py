import pandas as pd
import folium

# Load Excel file (must be in same folder)
file_path = "Book1.xlsx"
df = pd.read_excel(file_path)

# Create map centered on Bhutan
bhutan_map = folium.Map(location=[27.5, 90.5], zoom_start=8)

# Add markers from the Excel data
for _, row in df.iterrows():
    popup_text = (f"<b>Station:</b> {row['Station_name']}<br>"
                  f"<b>Dzongkhag:</b> {row['Dzongkhag']}<br>"
                  f"<b>Facility:</b> {row['Facility']}<br>"
                  f"<b>Status:</b> {row['Status']}")
    folium.Marker(
        location=[row['lat'], row['long']],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color='green' if str(row['Status']).lower() == 'working' else 'red')
    ).add_to(bhutan_map)

# Save to a map file
bhutan_map.save("bhutan_stations_map.html")
print("✅ Map saved as bhutan_stations_map.html")
