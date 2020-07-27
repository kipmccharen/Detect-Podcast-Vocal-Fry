import getpodcast
import os

def downloadpodcasts(podcasts, date_from, root_dir, most_recent=5):
    """Using getpodcast.py accept arguments and download podcast """
    opt = getpodcast.options(
        date_from=date_from,
        root_dir=root_dir,
        mostrecent=most_recent,
        run=True)
    getpodcast.getpodcast(podcasts, opt)

if __name__ == '__main__':    
    thisdir = os.path.dirname(os.path.abspath(__file__)) + "\\"
    savehere = thisdir + r"Podcast\\"
    date_from = '2020-01-01'
    podcasts = {"This American Life":"http://feed.thisamericanlife.org/talpodcast/"}
    downloadpodcasts(podcasts, date_from, savehere, 1)