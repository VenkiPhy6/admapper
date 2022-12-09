import pandas as pd
import requests as req
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import os

def ads_txt_getter(base_url):
    query_url = f"https://{base_url}/ads.txt"
    try:
        resp = req.get(query_url, timeout = 15, headers = {"Content-Type": "text/plain"})
        resp = resp.content
        with open(f'./ads_files/{base_url}.txt', 'wb') as outfile:
            outfile.write(resp)
    except Exception as e:
        resp = str(e)
        with open(f'./ads_files/{base_url}.err', 'w') as outfile:
            outfile.write(resp)
        txt_file_path = f'./ads_files/{base_url}.txt'
        if os.path.isfile(txt_file_path):
            os.remove(txt_file_path)
        
if __name__ == '__main__':
    urls_df = pd.read_csv('./data/valid_redirects.txt', sep='|')
    
    st_time = time.time() #Start time
    with ThreadPoolExecutor() as executor:
        executor.map(ads_txt_getter, urls_df['base_url'])
    print(f"It took {time.time() - st_time} to finish")