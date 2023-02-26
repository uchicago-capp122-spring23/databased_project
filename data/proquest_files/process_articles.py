'''
Project: Analyzing News Coverage of Chicago's 2023 Mayoral Election
Team: dataBASED

File name: process_articles.py
Associated files: export.py, select_articles.py
Primary Author: Kathryn Link-Oberstar
Addiditional Authors: None

Description: Decompress Proquest Data Files, and process articles to create a 
list of dictionaries, one for each article.
'''
import re
import tarfile
import json
import pandas as pd

# List of strings to remove from text
STRINGS_TO_REMOVE = ["<meta name='ValidationSchema' content='http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd'/>",
"</i>", "</p>", "</body>", "</html>", "<head>", "<title>", "</title>", 
"</head>", "<body>", "<p>", "<html>", "<b>", "<i>", "</b>", "\n"]

def unpack_file(tar, parquet):
    '''
    '''
    tz_file = tarfile.open(tar)
    parquet_file = tz_file.extractall("./")
    parquet_file = tz_file.extractfile(parquet)
    df_jsons = pd.read_parquet(parquet_file)
    tz_file.close()
    return df_jsons

def convert_to_dict(tar, parquet, SITE_ID):
    '''
    '''
    url_counter = 0
    df_jsons = unpack_file(tar, parquet)
    all_results = []
    for row in df_jsons.iterrows():
        url_counter += 1
        row_json = json.loads(row[1]['Data'])
        text = row_json["RECORD"]["TextInfo"]['Text']['#text']
        text_clean = re.sub('|'.join(STRINGS_TO_REMOVE), '', text)
        url = url_counter
        title = row_json["RECORD"]['Obj']['TitleAtt']['Title']
        pub_date = row_json["RECORD"]['Obj']['NumericDate']
        result_dict = {'candidate_id': None, 'name_tokens': None, 
                       'announcement_date': None, 'Newspaper_id': SITE_ID, 
                       'Url': url, 'Title': title, 'Text': text_clean, 
                       'date': pub_date}
        all_results.append(result_dict)
    return all_results
