from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

max_attempts = 100
wait_seconds = 600  # 10 minutes

for attempt in range(1, max_attempts + 1):
    try:
        print(f"Attempt {attempt}:")
        # Setup proxy
        pg = ProxyGenerator()
        pg.FreeProxies()  # Use free rotating proxies
        scholarly.use_proxy(pg)
        
        author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        print(f"Attempt {attempt} success")
        break  # Exit loop on first success
    except Exception as e:
        print(f"Attempt {attempt} failed with error: {e}")
        time.sleep(wait_seconds)
else:
    print("All 100 attempts failed.")

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# from scholarly import scholarly
# import jsonpickle
# import json
# from datetime import datetime
# import os

# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
# name = author['name']
# author['updated'] = str(datetime.now())
# author['publications'] = {v['author_pub_id']:v for v in author['publications']}
# print(json.dumps(author, indent=2))
# os.makedirs('results', exist_ok=True)
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)

# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }
# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)