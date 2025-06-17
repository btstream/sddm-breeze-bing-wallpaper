import requests
import os
import sys
import subprocess
from datetime import datetime

def download_image(url, save_path):
    """下载图片并保存到指定路径"""
    try:
        img_response = requests.get(url)
        img_response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(img_response.content)
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        return False

def get_bing_wallpaper(save_path='./wallpapers', resolution='UHD'):
    """
    从Bing获取每日壁纸并保存到本地
    
    参数:
        save_path (str): 保存目录，默认为'./wallpapers'
        resolution (str): 首选图片分辨率，默认为'UHD'
    """
    
    # Bing壁纸API
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
    
    try:
        # 获取壁纸信息
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # 获取图片信息
        image_info = data['images'][0]
        title = image_info['title']
        bing_date = datetime.strptime(image_info['startdate'], '%Y%m%d')
        
        # 生成文件名和路径
        filename = "{title}-{date}".format(
            date=image_info['startdate'],
            title=title.replace(' ', '_')
        )
        save_path = os.path.join(save_path, filename) if save_path == "./wallpapers" else save_path

        # 检查本地文件是否存在及是否最新
        if os.path.exists(save_path):
            local_mtime = datetime.fromtimestamp(os.path.getmtime(save_path))
            if local_mtime.date() >= bing_date.date():
                print(f"已存在最新壁纸: {save_path}")
                return save_path
        
        print(f"发现新壁纸: {title} (发布于 {bing_date.date()})")
        
        # 尝试首选分辨率
        image_url = f"https://www.bing.com{image_info['urlbase']}_{resolution}.jpg"
        if download_image(image_url, save_path):
            os.utime(save_path, (bing_date.timestamp(), bing_date.timestamp()))
            print(f"壁纸已保存到: {save_path}")
            return save_path
            
        # 首选分辨率失败，尝试2K分辨率
        print("4K壁纸不可用，尝试下载2K分辨率...")
        image_url = f"https://www.bing.com{image_info['urlbase']}_2560x1440.jpg"
        if download_image(image_url, save_path):
            os.utime(save_path, (bing_date.timestamp(), bing_date.timestamp()))
            print(f"2K壁纸已保存到: {save_path}")
            return save_path
            
        # 都失败则尝试默认分辨率
        print("2K壁纸不可用，尝试默认分辨率...")
        image_url = f"https://www.bing.com{image_info['urlbase']}_1920x1080.jpg"
        if download_image(image_url, save_path):
            os.utime(save_path, (bing_date.timestamp(), bing_date.timestamp()))
            print(f"默认分辨率壁纸已保存到: {save_path}")
            return save_path
            
        print("所有分辨率尝试均失败")
        return None
        
    except Exception as e:
        print(f"获取Bing壁纸失败: {e}")
        return None



if __name__ == "__main__":
    save_path = "/usr/share/sddm/themes/breeze/wallpaper"
    if len(sys.argv) >= 2:
        save_path = sys.argv[1]

    get_bing_wallpaper(save_path=save_path)
