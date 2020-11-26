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
    parser.add_argument('-a', '--add', action='store_true', help='Add new website.')
    args = parser.parse_args()

    # instantiate source handler
    sources = bchecker.SourceHandler()

    # run initial setup
    if args.setup:

        sources.read_sources()
        sources.get_payload()

        # write new blog content
        # todo make SourceHandler.write_payload() function for this.
        if len(sources.payload) > 0:
            with open('bchecker/payload.json', 'w') as f:
                json.dump(sources.payload, f, indent=4)

    # check for new content
    elif args.check:

        sources.read_sources()
        sources.read_previous_payload()
        sources.compare_payloads()


        # if 'first_time' not in locals():
        #     # if any new content is found that does not
        #     # match with old content, open in browser
        #     new_content_num = 0
        #     for i in old_content.keys():
        #         if new_content[i] != old_content[i]:
        #             try:
        #                 wbo(blog_urls[i], 0)
        #                 print(str(datetime.now()) +': Postman opened ' + i + '.')
        #             except e:
        #                 print(e)
        #             new_content_num = new_content_num + 1
        #     if new_content_num == 0:
        #         print('No updated webpages found.')
        #     else:
        #         print('First time setup completed.')

        # # write new blog content
        # with open('old_content.json', 'w') as f:
        #     json.dump(new_content, f, indent=4)


if __name__ == '__main__':
    main()