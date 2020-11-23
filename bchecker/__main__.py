import bchecker
import argparse
import json

def main():
    """
    TODO document
    """

    # parse command-line arguments
    parser = argparse.ArgumentParser(description="Check for new blog posts.")
    parser.add_argument('-s', '--setup', action='store_true', help='Run initial setup.')
    parser.add_argument('-c', '--check', action='store_true', help='Check for blog updates.')
    args = parser.parse_args()

    # run initial setup
    if args.setup:

        try:
            # read in blog sources
            with open('postman/sources.json', 'r') as f:
                sources = json.load(f)
        except:
            print("Can't read sources")
        
        # read and parse blog sources
        # new_content = {}

        for i in sources:
            blog = bchecker.Blog(name=i, url=sources[i])
            blog.parse_links()
            #new_content[i] = blog.links
            #blog.compare_links(new_content[i])
            # links_dict[i] = blog.links

    # check for new content
    elif args.check:

        # import previous webpage content
        try:
            with open('postman/old_content.json', 'r') as f:
                old_content = json.load(f)
        except FileNotFoundError as e:
            print(str(e) +
            ' ... Previous webpage data not found. Have you run postman --setup first?')
            exit



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


if __name__ == '__main__':
    main()