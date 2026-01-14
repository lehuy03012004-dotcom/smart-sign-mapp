import folium
from folium.plugins import MarkerCluster

SIGNS = [
    {"name":"Biển tốc độ 40","type":"speed","desc":"Giới hạn 40 km/h","prio":2,"lat":21.028511,"lon":105.804817},
    {"name":"Biển dừng lại","type":"stop","desc":"Dừng trước vạch","prio":3,"lat":21.030000,"lon":105.820000},
    {"name":"Cảnh báo công trình","type":"warning","desc":"Đường đang sửa chữa","prio":2,"lat":21.035000,"lon":105.815000},
    {"name":"Cấm rẽ trái","type":"prohibit","desc":"Không được rẽ trái","prio":3,"lat":21.027000,"lon":105.810000},
    {"name":"Đường một chiều","type":"direction","desc":"Lưu thông một chiều","prio":1,"lat":21.033000,"lon":105.805000},
    {"name":"Khu dân cư","type":"zone","desc":"Khu vực đông dân cư","prio":2,"lat":21.025500,"lon":105.818000},
    {"name":"Giao nhau nguy hiểm","type":"danger","desc":"Giao lộ nguy hiểm","prio":3,"lat":21.031500,"lon":105.812000},
]

def main():
    m = folium.Map(
        location=(21.028511, 105.804817),
        zoom_start=13,
        tiles="Esri.WorldImagery",
        attr="Esri"
    )

    cluster = MarkerCluster(name="Biển báo").add_to(m)

    for s in SIGNS:
        html = f"""
        <b>{s['name']}</b><br>
        Loại: {s['type']} • Ưu tiên: {s['prio']}<br>
        Mô tả: {s['desc']}
        """
        folium.Marker(
            location=(s["lat"], s["lon"]),
            tooltip=f"{s['name']} • {s['type']}",
            popup=folium.Popup(html, max_width=250),
            icon=folium.Icon(
                color="red" if s["prio"]>=3 else "orange" if s["prio"]==2 else "blue",
                icon="info-sign"
            )
        ).add_to(cluster)

    folium.LayerControl().add_to(m)
    m.save("smart_sign_map.html")

if __name__ == "__main__":
    main()
