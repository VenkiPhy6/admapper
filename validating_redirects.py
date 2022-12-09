import pandas as pd
import requests as req
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import os
from functools import partial

def redirects_getter(base_url, dest_file):
    query_url = f"https://{base_url}/ads.txt"
    try:
        resp = req.get(query_url, timeout = 15, headers = {"Content-Type": "text/plain"})
        with open(dest_file, 'a') as outfile:
            outfile.write(f"{query_url}|{base_url}|{resp.url}|y\n")
    except Exception as e:
        resp = str(e)
        with open(dest_file, 'a') as outfile:
            outfile.write(f"{query_url}|{base_url}|{resp}|n\n")
        
if __name__ == '__main__':
    urls_df = pd.read_csv('./data/valid_urls.txt', sep='|')
    
    #Creating the dest file
    dest_file = f'./data/redirects_response.txt'
    with open(dest_file, 'w') as outfile:
        outfile.write("query_url|base_url|redirect|status\n")
    
    redirect_func = partial(redirects_getter, dest_file=dest_file)
    st_time = time.time() #Start time
    with ThreadPoolExecutor() as executor:
        executor.map(redirect_func, urls_df['base'])
    print(f"It took {(time.time() - st_time)/60} minutes to finish")