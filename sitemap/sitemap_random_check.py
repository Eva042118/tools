import requests
import xml.etree.ElementTree as ET
import time
import random

def check_random_urls(url, num_urls_to_check):
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

            # 隨機抽查幾個網址
            selected_indices = random.sample(range(num_urls), min(num_urls_to_check, num_urls))

            # 檢查隨機抽查出的網址的可訪問性
            for index in selected_indices:
                url = urls[index]
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                response = requests.get(loc)
                if response.status_code == 200:
                    print(f"可以打開，第 {index+1} 個網址")
                else:
                    print(f"{loc} 無法打開，狀態碼: {response.status_code}")

        else:
            print("無法下載sitemap.xml文件")
    except Exception as e:
        print(f"出現異常: {str(e)}")

if __name__ == "__main__":
    sitemap_url = 'https://cars-pre.tvbs.com.tw/sitemap/spec.xml'  # 將此URL替換為你的sitemap.xml URL
    num_urls_to_check = 5  # 指定要随机抽查的網址數量
    check_random_urls(sitemap_url, num_urls_to_check)
    print("done")
