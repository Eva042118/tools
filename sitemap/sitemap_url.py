import requests
import xml.etree.ElementTree as ET
import time

def check_sitemap(url):
    try:
        # 下載sitemap.xml文件
        response = requests.get(url)
        if response.status_code == 200:
            # 解析XML
            root = ET.fromstring(response.content)
            urls = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            # 統計網址數量
            num_urls = len(urls)
            print(f"總共有 {num_urls} 個網址")
            # 檢查每個網址的可訪問性
            for url in urls:
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                response = requests.get(loc)
                if response.status_code == 200:
                    None
                else:
                    print(f"{loc} 無法打開，狀態碼: {response.status_code}")
                
                time.sleep(5)
        else:
            print("無法下載sitemap.xml文件")
    except Exception as e:
        print(f"出現異常: {str(e)}")

if __name__ == "__main__":
    sitemap_url = 'https://cars-pre.tvbs.com.tw/sitemap/spec.xml'  # 將此URL替換為你的sitemap.xml URL
    check_sitemap(sitemap_url)
