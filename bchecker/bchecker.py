import requests
# import json
from webbrowser import open as wbo
from datetime import datetime
from bs4 import BeautifulSoup
import json
import sys # for error


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
                l = link.get('href')
                # todo filter https://...
                if l not in self.links:
                    self.links.append(l)
            self.links.sort()
            return
        except:
            print("Could not parse HTML a tags.")
            return None
    

class SourceHandler:
    def __init__(self):
        self.sources = {}
        self.payload = {}
        self.previous_payload = {}
        self.new_links = []

    def read_sources(self):
        """
        Read in source URLs.
        """
        print("Reading source URLs...")
        try:
            with open('bchecker/sources.json', 'r') as f:
                self.sources = json.load(f)
            print("Successfully loaded " + str(len(self.sources)) + " sources.")
        except FileNotFoundError:
            print("Can't read sources file. Ensure that bchecker/sources.json exists. Exiting program.")
            exit
        except:
            print("Unidentified error. Exiting program.")
            exit

    def read_previous_payload(self):
        """
        Read in the links gathered the last time
        the program was run.
        """
        print("Reading previous payload data...")
        try:
            with open('bchecker/payload.json', 'r') as f:
                self.previous_payload = json.load(f)
            print("Successfully loaded previous payload data.")
        except FileNotFoundError:
            print('Previous payload not found. Have you run bchecker --setup first?')
            exit
        except:
            print("Unidentified error in SourceHandler.read_previous_payload. Exiting program.")
            print(sys.exc_info()[0])
            exit

    def get_payload(self):
        """
        Get current website content.
        """
        print("Retrieving current website data...")

        self.payload = {}

        for i in self.sources:
            blog = Blog(name=i, url=self.sources[i])
            blog.parse_links()
            self.payload[i] = blog.links.sort()

        if len(self.payload) > 0:
            print("Successfully retrieved data for " + str(len(self.payload)) + " websites.")
        else:
            print("No website data were retrieved.")

    def compare_payloads(self):
        """
        Traverses through SourceHandler.payload, comparing
        to SourceHandler.previous_payload, looking for
        new links. Stores them in SourceHandler.new_links.
        """
        print("Comparing newly retrieved data with previously retrieved data...")
        for i in self.payload.keys():
            # check that there's a match in previous_payload
            if i in self.previous_payload.keys():
                if self.payload[i] != self.previous_payload[i]:
                    new_links = set(self.payload[i]) - set(self.previous_payload[i])
                    for j in new_links:
                        self.new_links.append(j)

        
        if self.new_links == []:
            print("No updated websites were found.")
        else:
            for i in self.new_links:
                try:
                    wbo(self.new_links[i], 0)
                    print(str(datetime.now()) +': bchecker opened ' + i + '.')
                except:
                    print("Error opening " + i)

            # todo handle this. probably fine to not do much
            # since there's no reference.

        # if blog.links != reference_links.sort():
        #     new_links = set(blog.links) - set(reference_links.sort())

        # else:
        #     # no updated content
        #     return None