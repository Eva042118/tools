import requests
import xml.etree.ElementTree as ET

def check_sitemap_range(url, start_index, end_index):
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

            # 檢查指定範圍內的網址的可訪問性
            for i in range(start_index - 1, min(end_index, num_urls)):
                url = urls[i]
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
                response = requests.get(loc)
                if response.status_code == 200:
                    print(i)
                else:
                    print(f"{loc} 無法打開，狀態碼: {response.status_code}")
        else:
            print("無法下載sitemap.xml文件")
    except Exception as e:
        print(f"出現異常: {str(e)}")

if __name__ == "__main__":
    sitemap_url = 'https://cars-pre.tvbs.com.tw/sitemap/spec.xml'  # 將此URL替換為你的sitemap.xml URL
    start_index = 456
    end_index = 490
    check_sitemap_range(sitemap_url, start_index, end_index)
