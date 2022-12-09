import pandas as pd
import requests as req
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import time


def url_ads_txt_tester(base_url):
    query_url = f"https://{base_url}/ads.txt"
    try:
        resp = req.get(query_url, timeout = 15, headers = {"Content-Type": "text/plain"}).status_code
    except Exception as e:
        resp = str(e)
    with open(f'./data/responses.txt', 'a') as outfile:
        outfile.write(f"{query_url}|{resp}\n")

if __name__ == '__main__':
    urls_df = pd.read_csv('./data/urls_list.txt', sep='|')
    with open(f'./data/responses.txt', 'w') as outfile:
        pass
    
    st_time = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(url_ads_txt_tester, urls_df['base'])
    print(f"It took {(time.time() - st_time)/60} mintues to finish")