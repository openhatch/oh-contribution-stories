SITEURL = 'http://mergestories.com'
TIMEZONE = 'America/New_York'

THEME = './themes/pelican-elegant'  # Specify a customized theme, via absolute path

SITENAME = 'Merge Stories'
SITE_DESCRIPTION = 'A project of OpenHatch'

RECENT_ARTICLES_COUNT = 5       # Sets # of articles to be shown on front page

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['tipue_search']

