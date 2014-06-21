ARTICLE_URL = 's/{slug}/'
ARTICLE_SAVE_AS = 's/{slug}/index.html'

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'submit', 'search', '404'))

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['tipue_search']

RECENT_ARTICLES_COUNT = 5       # Sets # of articles to be shown on front page

SITENAME = 'Merge Stories'
SITE_DESCRIPTION = 'A project of OpenHatch'
SITEURL = 'http://mergestories.com'

SUMMARY_MAX_LENGTH = 100

THEME = './themes/pelican-elegant'  # Specify a customized theme, via absolute path

TIMEZONE = 'America/New_York'




