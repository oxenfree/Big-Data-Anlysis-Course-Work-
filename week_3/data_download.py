import os
from six.moves import urllib

LOCAL_PATH = os.path.join('data', 'stadiums')
DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/gboeing/data-visualization/master/ncaa-football-stadiums/'
DOWNLOAD_URI = DOWNLOAD_ROOT + 'data/stadiums-geocoded.csv'


def fetch_stadium_data(download_url=DOWNLOAD_URI, local_path=LOCAL_PATH):
    if not os.path.isdir(local_path):
        os.makedirs(local_path)
    tgz_path = os.path.join(local_path, 'stadiums.csv')
    urllib.request.urlretrieve(download_url, tgz_path)


if __name__ == '__main__':
    fetch_stadium_data()
