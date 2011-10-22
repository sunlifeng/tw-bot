import sys
from os.path import dirname, join as join_path
GAEHOME=  'C:/Program Files/Google/google_appengine/'
sys.path.extend([
  join_path(GAEHOME,'lib/webob'),
  join_path(GAEHOME,'lib/django'),
  join_path(GAEHOME,'lib/antlr3'),
  join_path(GAEHOME,'lib/yaml/lib'),
  GAEHOME,
])
 
from google.appengine.tools import dev_appserver
from google.appengine.tools.dev_appserver_main import *
 
option_dict = DEFAULT_ARGS.copy()
option_dict[ARG_CLEAR_DATASTORE] = True
 
config, matcher = dev_appserver.LoadAppConfig(".", {})
dev_appserver.SetupStubs(config.application, **option_dict)
 
import main
reload(main)
 
from webtest import TestApp
SAFARI4_UA = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9"
app = TestApp(main.application(), extra_environ={"HTTP_USER_AGENT": SAFARI4_UA})
 
from lxml import etree
from StringIO import StringIO
 
def parseResponse(response):
  parser = etree.HTMLParser()
  return etree.parse(StringIO(response.body), parser)

#
#import bikejibe.model
#reload(bikejibe.model)
# 
#from bikejibe.model import *

