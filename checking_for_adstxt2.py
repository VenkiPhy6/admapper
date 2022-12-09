import pandas as pd
import requests as req
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import time


def url_ads_txt_tester(base_url, dest_file):
    query_url = f"https://{base_url}/ads.txt"
    try:
        resp = req.get(query_url, timeout = 15, headers = {"Content-Type": "text/plain"}).status_code
    except Exception as e:
        resp = str(e)
    with open(dest_file, 'a') as outfile:
        outfile.write(f"{query_url}|{base_url}|{resp}\n")

if __name__ == '__main__':
    urls_df = pd.read_csv('./data/redirect_urls.txt', sep='|')
    
    dest_file = f'./data/responses2.txt'
    with open(dest_file, 'w') as outfile:
        outfile.write("query_url|base_redirect|response\n")
    
    st_time = time.time()
    
    url_ads_txt_tester_func = partial(url_ads_txt_tester, dest_file=dest_file)
    with ThreadPoolExecutor() as executor:
        executor.map(url_ads_txt_tester_func, urls_df['base_redirect'])
    print(f"It took {(time.time() - st_time)/60} mintues to finish")