import random
import requests
import time
import geopandas as gpd
from shapely.geometry import Point
import ctypes
import winreg
import os

# Mapbox API
token="your token" # replace with your own token
mapbox_url = "https://api.mapbox.com/styles/v1/thtooong1/cm7bzk3t7007l01r7fdu23m1e/static/{lon},{lat},{scale},0/1280x800?access_token={token}"

def set_lock_screen_wallpaper(image_path):
    """
    通过调用 Windows API 将指定图片设置为桌面壁纸
    """
    """
    将壁纸设置为“填充”方式，使图片自适应屏幕分辨率。
    """
    # 先修改注册表中壁纸样式
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE)
    # “10”表示Fill填充；如果想要Stretch拉伸，可以改为 “2”
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "10") 
    # 是否平铺：0 不平铺；1 平铺
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    winreg.CloseKey(key)

    # 调用 Windows API (SystemParametersInfoW) 设置新的壁纸
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATE_INI_FILE = 0x1
    SPIF_SENDWININICHANGE = 0x2
    ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, image_path,
    SPIF_UPDATE_INI_FILE | SPIF_SENDWININICHANGE
)
    print("锁屏壁纸已更新")


# 随机生成经纬度
def generate_random_coordinates():
    lon = random.uniform(-180, 180)
    lat = random.uniform(-60, 90)
    scale = random.uniform(3,8)
    return lat, lon,scale


# 读取海洋Shapefile
def load_ocean_shapefile(shapefile_path):
    # 使用Geopandas读取Shapefile
    oceans = gpd.read_file(shapefile_path)
    return oceans

# 判断经纬度是否在海洋区域
def is_ocean(lat, lon, ocean_shapefile):
    # 创建一个Point对象，表示给定的经纬度
    point = Point(lon, lat)
    
    # 使用Geopandas的`contains`方法判断该点是否在任何海洋多边形内
    for _, ocean in ocean_shapefile.iterrows():
        if ocean['geometry'].contains(point):
            return True  # 如果点在海洋区域内
    return False  # 如果点不在海洋区域内

# 获取Mapbox地图图像
def get_map_image(lat, lon,scale):
    url = mapbox_url.format(lon=lon, lat=lat,scale=scale, token=token)
    response = requests.get(url)
    if response.status_code == 200:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_dir, "mappic.png")
        with open(img_path, 'wb') as file:
            file.write(response.content)
        return img_path
    return None

# 主流程
def main():
    # 随机生成经纬度并判断是否是陆地
    begin_time = time.time()
    while True:
        lat, lon,scale = generate_random_coordinates()
        print(f"生成的经纬度: ({lat}, {lon},{scale})")
        shapefile_path = "ne_10m_ocean/ne_10m_ocean.shp"
        ocean_shapefile = load_ocean_shapefile(shapefile_path)
        if is_ocean(lat, lon, ocean_shapefile):
            print(f"该位置 ({lat}, {lon}) 在海洋上")
            now_time = time.time()
            print(f"耗时: {now_time - begin_time:.2f}秒")
        else:
            print(f"该位置 ({lat}, {lon},{scale}) 在陆地上")
            img_path = get_map_image(lat, lon,scale)
            if img_path:
                print(f"下载的地图图像已保存到: {img_path}")
                set_lock_screen_wallpaper(img_path)
                break
        # else:
        #     print(f"该位置 ({lat}, {lon}) 在海洋上，重新生成...")
    end_time = time.time()
    print(f"总耗时: {end_time - begin_time:.2f}秒")

if __name__ == "__main__":
    main()
