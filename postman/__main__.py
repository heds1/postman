import requests
import json
from webbrowser import open as wbo
from datetime import datetime
from bs4 import BeautifulSoup

# define blog URL endpoints to search
blogs = {
    'megan_stodel': 'https://www.meganstodel.com/',
    'tunnelsup': 'https://www.tunnelsup.com/blog/archives/',
    'data_colada': 'http://www.datacolada.org/',
    'dennis_schubert': 'https://schub.wtf/',
    'rachel_by_the_bay': "https://rachelbythebay.com/",
}

class Blog:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.links = None
        self.update = False

    def parse_links(self):
        """
        Get the raw HTML from the blog's homepage URL,
        and parse links found in all <a> tags.
        """
        try:
            page = requests.get(self.url).content.decode()
        except:
            print("Could not retrieve content from " + self.name)
            return None
        
        try:
            soup = BeautifulSoup(page, 'html.parser')
            self.links = []
            for link in soup.find_all('a'):
                print(link.get('href'))
                self.links.append(link.get('href'))
            self.links.sort()
            return
        except:
            print("Could not parse HTML a tags.")
            return None
    
    def compare_links(self, reference_links):
        # if the links are different, find the differences
        if blog.links != reference_links.sort():
            new_links = set(blog.links) - set(reference_links.sort())

        else:
            # no updated content
            return None
            
# import previous webpage content
try:
    with open('old_content.json', 'r') as f:
        old_content = json.load(f)
except FileNotFoundError as e:
    print(str(e) +
    ' ... Old content not found. If this script is being run for the first time, ' +
    'this is fine.')
    first_time = True

new_content = {}

for i in blogs:
    blog = Blog(name=i, url=blogs[i])
    blog.parse_links()
    new_content[i] = blog.links

    blog.compare_links(new_content[i])



    links_dict[i] = blog.links

if 'first_time' not in locals():
    # if any new content is found that does not
    # match with old content, open in browser
    new_content_num = 0
    for i in old_content.keys():
        if new_content[i] != old_content[i]:
            try:
                wbo(blog_urls[i], 0)
                print(str(datetime.now()) +': Postman opened ' + i + '.')
            except e:
                print(e)
            new_content_num = new_content_num + 1
    if new_content_num == 0:
        print('No updated webpages found.')
else:
    print('First time setup completed.')

# write new blog content
with open('old_content.json', 'w') as f:
    json.dump(new_content, f, indent=4)

