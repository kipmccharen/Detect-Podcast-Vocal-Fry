import getpodcast

opt = getpodcast.options(
    date_from='2016-07-07',
    root_dir=r'D:\Py_ML_CS\Podcast\\',
    mostrecent=5)

podcasts = {
    "This American Life":"http://feed.thisamericanlife.org/talpodcast/"
}

getpodcast.getpodcast(podcasts, opt)