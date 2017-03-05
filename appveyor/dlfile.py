from __future__ import print_function, division

import sys
import urllib
import urlparse


def get_filename_from_url(url):
    return urlparse.urlsplit(url).path.split('/')[-1]


def main(url, filename):
    print('Downloading {}...'.format(filename))
    urllib.urlretrieve(url, filename=filename)
    print('Done.')


if __name__ == '__main__':
    url = ''.join(sys.argv[1:])
    filename = get_filename_from_url(url)
    main(url, filename)
