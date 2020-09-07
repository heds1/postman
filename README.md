# Postman

Postman is a simple Python script that searches a dictionary of provided websites
and opens them in the browser if new changes are detected. It was initially
designed to alert the user when new blog posts have been published, but 
can be extended to any similar task.

## How it works

Postman is about as simple as you could imagine. It scrapes the given URLs
and stores the HTML in a dictionary that is stored as JSON. When the script is
run, it checks the new HTML content against the old HTML content, and opens
a browser window for each URL that is different to the last time the script
was run.

## Quickstart

```
git clone https://github.com/heds1/postman.git
cd postman
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Edit the dictionary `blog_urls` (replace with your desired URLs and names).
Run the script:

```
python postman
```

You should see an output of 'First time setup completed.'. In your working
directory should be a new file, `old_content.json`. The next time you run
the script, it will check the HTML of the scraped webpages against that 
stored in `old_content.json`.

## Next steps

TODO: put this into a crontab

## Contributors
- [Hedley Stirrat](https://github.com/heds1)