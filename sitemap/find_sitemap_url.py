import requests
import xml.etree.ElementTree as ET

def find_url_position(sitemap_url, target_url):
    try:
        # 下载并解析sitemap.xml文件
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            urls = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            
            # 查找目标URL在列表中的位置
            for i, url in enumerate(urls):
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                if loc == target_url:
                    return i + 1  # 位置从1开始计数

            # 如果未找到目标URL
            return -1
        else:
            print("无法下载sitemap.xml文件")
            return -1
    except Exception as e:
        print(f"出现异常: {str(e)}")
        return -1

if __name__ == "__main__":
    sitemap_url = 'https://cars-pre.tvbs.com.tw/sitemap/spec.xml'  # 将此URL替换为您的 sitemap.xml URL
    target_url = 'https://cars-pre.tvbs.com.tw/spec/ferrari/2022-ferrari-portofino'  # 要查找的目标URL
    position = find_url_position(sitemap_url, target_url)
    if position != -1:
        print(f"{target_url} 在 sitemap.xml 中的位置是第 {position} 个")
    else:
        print(f"{target_url} 不在 sitemap.xml 中")
