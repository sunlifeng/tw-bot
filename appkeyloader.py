from google.appengine.tools import bulkloader

import model

class AppKeyLoader(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'AppKey',
                               [('consumer_key', str),
                                ('consumer_secret', str),
                               ])

loaders = [AppKeyLoader]

