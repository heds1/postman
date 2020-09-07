import requests
import json
from webbrowser import open as wbo

# define blog URL endpoints to search
blog_urls = {
    'megan_stodel': 'https://www.meganstodel.com/',
    'tunnelsup': 'https://www.tunnelsup.com/blog/archives/'
}

# import previous webpage content
try:
    with open('old_content.json', 'r') as f:
        old_content = json.load(f)
except FileNotFoundError as e:
    print(str(e) +
    ' ... Old content not found. If this script is being run for the first time, ' +
    'this is fine.')
    first_time = True

# get current webpage content
new_content = {}
for i in blog_urls:
    page = requests.get(blog_urls[i])
    new_content[i] = page.content.decode()

if 'first_time' not in locals():
    # if any new content is found that does not
    # match with old content, open in browser
    new_content_num = 0
    for i in new_content.keys():
        if new_content[i] != old_content[i]:
            wbo(blog_urls[i], 0)
            new_content_num = new_content_num + 1
    if new_content_num > 0:
        print(str(new_content_num) + ' new webpage(s) opened.')
    else:
        print('No new webpages found.')
else:
    print('First time setup completed.')

# write new blog content
with open('old_content.json', 'w') as f:
    json.dump(new_content, f, indent=4)

