import argparse
import webparser
import downloader
import sys
import urllib.request
import configparser
import logging as log
config = configparser.ConfigParser()
config.read('config.ini')
parser = argparse.ArgumentParser(description='Download BBC programme thumbnails.')
parser.add_argument('pid', type=str, nargs='*',
                    help='programme pid')
parser.add_argument('--res', metavar='resolution', type=str, action='store',
                    default=config['DEFAULT']['resolution'],
                    help='define the thumbnail resolution (default: {})'.format(config['DEFAULT']['resolution']))
parser.add_argument('--dest', metavar='destination', type=str, action='store',
                    default=config['DEFAULT']['destination'],
                    help='define the destination folder (Default: {})'.format(config['DEFAULT']['destination']))
parser.add_argument('--series', action='store_const',
                    const=True,
                    default=False,
                    help='whole series thumbnail download (currently limited to one series)')
parser.add_argument('--all', action='store_const',
                    const=True,
                    default=False,
                    help='whole programme thumbnail download (downloads thumbnails for all seasons/series)')
parser.add_argument('--nonames', action='store_const',
                    const='True',
                    default=config['DEFAULT']['names'],
                    help='skip fetching episode names (Default: {})'.format(config['DEFAULT']['names']))
parser.add_argument('--config', action='store_const',
                    const=True,
                    default=False,
                    help='run configuration of default values')
parser.add_argument('-v', '--verbose', action='store_const',
                    const=True,
                    default=False,
                    help='run program with debug verbosity')
args = parser.parse_args()
if args.config:
    res = input('Input the wanted default resolution: ')
    dest = input('Input the wanted default destination: ')
    nonames = bool(int(input('Do you want to skip episode name fetching (1 for yes, 0 for no): ')))
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'resolution': res,
                         'destination': dest,
                         'names': nonames}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    sys.exit('Saved config! Closing.')
if args.verbose:
    log.basicConfig(format="[%(levelname)s] %(message)s", level=log.DEBUG)
    log.info("Verbose output enabled.")
else:
    log.basicConfig(format="[%(levelname)s] %(message)s")
if args.dest == '':
    log.critical('Default destination missing! Please update the defaults with --config.')
    sys.exit()
if args.pid == []:
    log.critical('No PIDs entered, closing program.')
    sys.exit()
log.info('Downloading PIDs {} at resolution {}'.format(args.pid, args.res))
urls = []
for pid in args.pid:
    if args.series:
        try:
            httpcode = urllib.request.urlopen('https://www.bbc.co.uk/programmes/' + pid + '/episodes/guide').getcode()
            seriesurl = ('https://www.bbc.co.uk/programmes/' + pid + '/episodes/guide')
        except urllib.request.HTTPError as e:
            log.critical('Website inaccessible ({})'.format(e))
            sys.exit('Unable to continue, closing program')
        urls = webparser.series(seriesurl)
    else:
        try:
            httpcode = urllib.request.urlopen('https://www.bbc.co.uk/programmes/' + pid).getcode()
            urls.append('https://www.bbc.co.uk/programmes/' + pid)
        except urllib.request.HTTPError as e:
            log.critical('Website inaccessible ({})'.format(e))
            sys.exit('Unable to continue, closing program')
        adddir=''
log.info('Found matching websites: {}'.format(urls))
imgurls = webparser.images(urls, args.res)
log.info('Adjusted resolution image urls: {}'.format(imgurls))
if args.nonames == 'False':
    try:
        names = webparser.names(urls)
        log.info('Found matching episode names: {}'.format(names))
    except:
        log.warning('Skipping episode name fetch because of acquire fail')
        names = None
else:
    log.info('Skipped fetching episode names')
    names = None
if args.series:
    adddir = '/' + names[0][1] + '/'
    log.info('Added {} directory to file destination'.format(adddir))
if downloader.imgdown(imgurls, args.dest, names, adddir):
    log.info('Success!')
    sys.exit('Done, Closing program.')