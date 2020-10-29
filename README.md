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

## Bash command (Linux)

To avoid going to the postman directory and activating the virtual environment,
you can just add executable privileges to the `bashman` script,
then copy it to a binary directory, e.g.:

```
chmod +x bashman
cp bashman $HOME/.local/bin
```

Simply call the script from any terminal:

```
bashman
```

## Set up script on schedule with crontab

Open the crontab editor, and copy in the following settings:

```
DISPLAY=:0
0 */8 * * * $HOME/.local/bin/bashman
```

The `DISPLAY` environment variable is required to allow the browser to open. The `0 */8 * * *` syntax means that the script will run every eight hours. If you moved `bashman` to a different bin, set the path there.

You can redirect the output of the script to a logfile by appending `>> /var/log/cron.log`, for example.

## Contributors
- [Hedley Stirrat](https://github.com/heds1)