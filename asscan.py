#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse

import os
import argparse
import requests
import urllib3
import stringcolor

__author__ = 'PoCo'
__version__ = stringcolor.cs('VER: 1.0.1', '#808000')
__url__ = 'https://github.com/helGayhub233/AS-Scan'
__description__ = 'Assets Survival Scan v1.0.1'
__tips__ = '''
example:
  asscan.py -u domain.com
  asscan.py -u [-r] domain.com
  asscan.py -i input.txt -o output.txt
  
'''

_count = 1  # list counter
_YES = []  # status 200
_NO = []  # status other


def http_title(url):
    if url.startswith('http://') or url.startswith('https://'):
        target = urlparse(url)
        target = target.scheme + '://' + target.netloc
        return target
    else:
        target = 'http://' + url
        return target


def print_title():
    print("""\033[1;36m
     ___    ____       ____      \033[0m""" + __version__ + """\033[1;36m            
    / _ | / ___/     / ___/____  ___   ____
   / /| | \__ \ ____ \__ \/ ___/ __ `/ __  /
  / ___ |___/ /____ /__/ / /__/ /_/ / / / /
 /_/  |_/____/     /____/\___/\__,_/_/ /_/ 
\033[0m""" + """
Author: """ + __author__ + """
Github: """ + __url__ + """\n""")


def prase_target(target):
    _status = ''
    call_count = ' ' + str(_count) + ' :\t'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.62 Safari/537.36 '
    }
    try:
        data = requests.get(target, headers=headers, timeout=3.5, verify=False)
        value_url, value_status = target, data.status_code

        if value_status == 200:
            _status = ' [ OK ]'
            _YES.append(value_url)
        else:
            _status = ' [ OK ]'
            _YES.append(value_url)
        row = call_count + stringcolor.cs(get_tab(value_url), '#00ff00') \
              + stringcolor.cs(str(value_status), '#00ff00') + '\t\b' + stringcolor.cs(_status, '#00ff00')
        print(row)

    except requests.exceptions.ReadTimeout:
        _status = ' [ TI ]'  # timeout
        _NO.append(target)
        value_url, value_status = target, '407'
        row = call_count + stringcolor.cs(get_tab(value_url), '#ff9900') \
              + stringcolor.cs(str(value_status), '#ff9900') + '\t\b' + stringcolor.cs(_status, '#ff9900')
        print(row)

    except (requests.exceptions.InvalidURL, urllib3.exceptions.LocationParseError):
        _status = ' [ IN ]'  # invalid
        _NO.append(target)
        value_url, value_status = target, 'Null'
        row = call_count + stringcolor.cs(get_tab(target), '#696969') \
              + stringcolor.cs(value_status, '#696969') + '\t\b' + stringcolor.cs(_status, '#696969')
        print(row)

    except requests.ConnectionError:
        _status = ' [ ER ]'  # error
        _NO.append(target)
        value_url, value_status = target, 'Lose'
        row = call_count + stringcolor.cs(get_tab(value_url), '#ff0000') \
              + stringcolor.cs(str(value_status), '#ff0000') + '\t\b' + stringcolor.cs(_status, '#ff0000')
        print(row)


def print_header_scan():
    print(' No.\tTarget' + '\t' * 5 + '\bStatus\tValue')
    print('-' * 62)


def get_tab(string):
    if len(str(string)) > 27:
        return string[:27] + '..(to long)' + '\t'
    elif len(str(string)) > 23:
        return string + '\t\t'
    elif 15 < len(str(string)) <= 23:
        return string + '\t\t\t'
    else:
        return string + '\t\t\t'


def loadfile_wlist(filename):
    filename = open(filename, 'r')
    wlist = filename.read().split('\n')
    filename.close()
    return filter(None, wlist)


def main():
    global _count
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=__description__,
        epilog=__tips__)

    parser.add_argument('-u', '--url', help='target to scan, like www.domain.com')
    parser.add_argument('-i', help='import your urls', dest='wordlist', action='store',
                        required=False)
    parser.add_argument('-o', '--output', help='save output in txt', dest='output', action='store', required=False)
    parser.add_argument('-r', '--realip', help='detect the real IP-address of the target', action='store',
                        required=False)

    args = parser.parse_args()
    url = args.url
    wlist = args.wordlist  # input
    wfile = args.output  # output

    requests.packages.urllib3.disable_warnings()
    print_title()
    print_header_scan()

    if wlist:
        _ROOT = os.path.abspath(os.path.dirname(__file__))
        wordlist = os.path.join(_ROOT, wlist)

        if not os.path.isfile(wlist) and not wlist.endswith('.txt'):
            exit(f'\nFile not found: {wordlist}.txt\n')
        word_list = loadfile_wlist(wordlist)
        word_list = [item.lower() for item in word_list]
        word_list = [http_title(c_item) for c_item in word_list]

        if wfile:
            output = os.path.join(_ROOT, wfile)
            if not os.path.isfile(wfile) and not wfile.endswith('.txt'):
                exit(f'\nFile not found: {output}.txt\n')
            elif os.path.exists(wfile) and os.path.exists('FAIL.txt'):
                exit(f'\nPlease delete or rename the previous file first.\n')
            else:
                for item in word_list:
                    prase_target(item)
                    _count += 1
                with open(wfile, 'a') as y, open('FAIL.txt', 'a') as n:
                    for w_y in _YES:
                        y.write(w_y + '\n')
                    for w_n in _NO:
                        n.write(w_n + '\n')
                print(f'\nTotal: There are {len(_YES)} open, {len(_NO)} exception.')
                print(f'Please check the file {output}, See FAIL.txt for failure.\n')
        else:
            for item in word_list:
                prase_target(item)
                _count += 1
            print(f'\nTotal: {len(_YES)} domains open, {len(_NO)} domains exception.\n')

    elif url is None:
        exit(parser.print_help())

    else:
        c_target = http_title(url)
        prase_target(c_target)
        print()


if __name__ == '__main__':
    main()
