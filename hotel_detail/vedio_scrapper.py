import requests

url = 'https://booking.gora.golf.rakuten.co.jp/guide/course_info/drone/disp/c_id/10005'
req = requests.get(url, allow_redirects=True)

# print(req.content)
with open('vedio.mp4', 'wb') as f:
        for chunk in req.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
# open('vedio.mp4', 'wb').write(req.content)