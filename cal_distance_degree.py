import pyproj

# 関数の説明：地球を楕円とした時の、与えられた始点と終点の元に距離と方位角を返す関数
# 距離は[m]で返す。
# 方位角は真北を0とした時計回りのdegreeで返す。

def get_distance_and_degree(lat1, lng1, lat2, lng2):
    grs80 = pyproj.Geod(ellps='GRS80')  # GRS80楕円体
    lat_diff = abs(lat1-lat2)
    lng_diff = abs(lng1-lng2)
    if lat_diff <= 0.002 and lng_diff <= 0.002:  # 定点保持したい面積の閾値
        result = [0, 0, 0]
        return result
    else:
        result = grs80.inv(lng1, lat1, lng2, lat2)
        return result

# ex例
lat1, lng1 = 34.705185, 135.498468  # 始点：経度, 緯度
lat2, lng2 = 35.170897, 136.881537  # 終点：経度, 緯度

result = get_distance_and_degree(lat1, lng1, lat2, lng2)
print(f"進む方向：{result[0]:.2f}度、進む距離：{result[2]:.2f}m")