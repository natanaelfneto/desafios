#!/usr/bin/env python
# -*- coding: utf-8 -*-

__project__ = 'crawler_bot'
__author__ = 'natanaelfneto'
__description__ = "An apprentice scrapper bot"


# python imports
import argparse
import csv
import http.client
import json
import sys
# third party imports
import bs4


# base url for reddit
base_url = 'www.reddit.com'

# subreddits scrapped
scrapped_subs = []

# start connection
headers = { 'User-Agent' : __description__ }
connection = http.client.HTTPSConnection(base_url)


# get item upvotes
def get_upvotes(div):
    '''
    Argument(s):
        div: a beautiful soup result
    '''

    # get div content
    content = div.get_text()

    # check if upvotes are higher than N * 1000
    minimum_value = 5

    # try to parse upvotes number
    try:
        if 'k' in content.split('Posted by')[0]:

            # check if value can be parsed as a float number
            upvotes = float(content.split('Posted by')[0].replace('k',''))

            # check if it is bigger than 5000
            if upvotes > 5:
                upvotes = '{0}k'.format(str(upvotes))
            else:
                upvotes = None
        else:
            # upvotes = int(content.split('Posted by')[0])
            upvotes = None
    except:
        upvotes = None
        pass

    # return upvotes value
    return upvotes


# get item title 
def get_title(div):
    '''
    Argument(s):
        div: a beautiful soup result
    '''

    # aux variable
    head = None

    # get head content
    head_content = div.find('h2')

    # get head string content when exist
    if head_content is not None:
        head = head_content.get_text()
        
    # return head content value
    if head is not None:
        return ''.join([i if ord(i) < 128 else '' for i in head])
    else:
        return None


# get link for commentaries
def get_commentaries_link(div):
    '''
    Argument(s):
        div: a beautiful soup result
    '''

    # aux variable
    href = None

    # get all links inside div
    links = div.find_all('a')

    # loop though links
    for link in links:

        # check if it is a 'comments' link
        if link.get('data-click-id') is not None and 'comments' in link.get('data-click-id'):

            # get link content
            href = link.get('href')
            
    # check for no subthreads
    if href is not None:
        return '{0}{1}{2}'.format('https://', base_url, href)
    else:
        return 'No subthreads were found'


# get link for subthreads
def get_subthread_link(div):
    '''
    Argument(s):
        div: a beautiful soup result
    '''

    # aux variable
    href = None

    # get all links inside div
    links = div.find_all('a')

    # loop though links
    for link in links:

        # check if it is a subthread link
        if link.get('href') is not None and 'search?' in link.get('href'):

            # get link content
            href = link.get('href')

    # check for no subthreads
    if href is not None:
        return '{0}{1}{2}'.format('https://', base_url, href)
    else:
        return 'No subthreads were found'
    

# command line argument parser
def args(args):
    '''
        Main function for terminal call of library
        Arguments:
            args: receive all passed arguments and filter them using
                the argparser library
    '''

    # argparser init
    parser = argparse.ArgumentParser(description=__description__)

    # files to be limited
    parser.add_argument(
        'threads',
        nargs='+',
        help='threads to be crawled', 
        default=None
    )

    # passing filtered arguments as array
    args = parser.parse_args(args)

    # call function
    run(threads=args.threads)


# run function
def run(threads=None):
    '''
    Argument(s):
        threads: names for threads that will be crawled
    '''

    # aux variable
    subs = threads

    # loop through subs
    for sub in subs:

        # aux variable
        array = []  

        # get request for sub content
        connection.request('GET', '/r/{0}'.format(sub), headers=headers)

        # get response
        html = connection.getresponse()

        # output connection status and reason
        output = 'URL: https://{0}/r/{1}\nSTATUS: {2}\nREASON: {3}\n'.format(base_url, sub, html.status, html.reason)
        print(output)

        if str(html.status) != '200':
            raise ValueError('Problem with server response, please try again!')

        # soup html content
        soup = bs4.BeautifulSoup(html,'lxml')

        # get divs
        divs = soup.find_all('div')

        # loop thought founded divs
        for index, div in enumerate(divs):

            # check if it has desired class name
            if div.get('class') is not None and 'scrollerItem' in div.get('class'):
                
                # get upvotes value from div
                upvotes = get_upvotes(div)

                # get title value from div
                title = get_title(div)

                # get commentaries link
                commentaries_link = get_commentaries_link(div)

                # get thread link
                subthread_link = get_subthread_link(div)
                
                # append value if any are None
                if all(v is not None for v in [upvotes, title, commentaries_link, subthread_link]):
                    array.append({
                        'upvotes': str(upvotes),
                        'subreddit': str(sub),
                        'title': title,
                        'commentaries_link': str(commentaries_link),
                        'subthread_link': str(subthread_link)
                    })
        
        # append sub content in a global dictionary
        scrapped_subs.append({
            str(sub): array
        })

    # console output
    output = json.dumps(scrapped_subs, sort_keys=True, indent=4)
    print(output)

    # finish connection
    connection.close()


# run function on command call
if __name__ == "__main__":
    args(sys.argv[1:])
# end of code