#!/usr/bin/env python
# -*- coding: utf-8 -*-

__project__ = 'line_limitter'
__author__ = 'natanaelfneto'
__description__ = "Script for limiting content lines"


# python imports
import argparse
import re
import sys
import textwrap 


# get content from source file
def get_content(source=None):
    '''
    Argument(s):
        source: file with desired content
    '''

    # read source file
    with open(source, 'r') as f:
        # get content lines
        content = f.readlines()

    # return splited paragraphs within content variable
    return content


# function for string justification align
def justify_string(line, limit):
    '''
    Argument(s):
        line: string to be justified
        limit: maximum number of chars in each line
    '''

    # get number of spaces missing from desired limit
    left = limit - len(line)

    # split line into words
    items = line.split()

    # add space lost in split() to each word, except last
    for i in range(len(items) - 1):
        items[i] += '{0}'.format(chr(32))

    # loop until length matches limit
    while left > 0 and len(items) > 1:

        # for all items, except last
        for i in range(len(items) - 1):

            # add required spaces
            items[i] += '{0}'.format(chr(32))

            # decrement remaining spaces needed
            left -= 1

            # avoid over spacing
            if left < 1:
                break

    # return concatenated items
    return ''.join(items)


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
        'source',
        help='source to be formatted', 
        default=None
    )

    # number of lines to limit
    parser.add_argument(
        '-n','--limit',
        type=int,
        help='format char limit of source lines', 
        default=None,
        required=True
    )

    # justification flag
    parser.add_argument(
        '--justified',
        action='store_true', 
        help='justify lines on output',
        default=False,
        required=False
    )

    # write output flag
    parser.add_argument(
        '--write',
        action='store_true', 
        help='write output in a file',
        default=False,
        required=False
    )

    # passing filtered arguments as array
    args = parser.parse_args(args)

    if args.source == None or args.limit == None:
        output = 'Error: not a valid source: {0} or limit value: {1}'.format(args.source, args.limit)
        raise ValueError(output)
        sys.exit()

    # call function
    run(
        source=args.source,
        limit=args.limit,
        justified=args.justified,
        write=args.write,
    )


# run function
def run(source=None, limit=None, justified=False, write=False):
    '''
        Argument(s):
            source: file with desired content
            limit: maximum number of chars in each line
            justified: boolean value to align text with/without justification 
    '''

    # check write flag
    if write and not justified:
        output_file = open('output_parte1.txt', 'w')
    elif write and justified:
        output_file = open('output_parte2.txt', 'w')
    else:
        pass

    # get content from source file
    content = get_content(source)
 
    # check for justification flag
    if justified:

        # output variable
        output = ''

        # check for paragraphs in content
        for paragraph in content:

            # check for empty lines
            if not paragraph == '\n':

                # get wrapped paragraph content
                wrapped_paragraph = textwrap.wrap(paragraph, width=limit)

                # justify lines in paragraph
                for line in wrapped_paragraph:

                    # justify single line
                    justified = justify_string(line, limit)

                    # write justified line
                    if write:
                        output_file.write('{0}\n'.format(justified))

                    # print justified line
                    else:
                        print(justified)
            
            # print new paragraph line
            else:
                print(paragraph, end='\r')
    
    # if justification flag is not set print output
    else:
        # check for paragraphs in content
        for paragraph in content:

            # get wrapped paragraph content
            output = textwrap.fill(paragraph, width=limit)

            # write output line
            if write:
                output_file.write('{0}\n'.format(output))

            # print output line
            else:
                print(output)

    # close file if one is set
    if write:
        output_file.close()


# run function on command call
if __name__ == "__main__":
    args(sys.argv[1:])
# end of code

