# -*- coding: utf-8 -*-

########################################
# Configuration, please edit
########################################

# post_pages contains (wildcard, destination, template, use_in_feed) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
# That fragment must have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is specified in the metadata file.
#
# if use_in_feed is True, then those posts will be added to the site's
# rss feeds.
#

POSTS = (
    ("_posts/*.txt", "posts", "post.tmpl"),
    ("_posts/*.rst", "posts", "post.tmpl"),
)
PAGES = (
    # ("stories/*.txt", "stories", "story.tmpl"),
    # ("stories/*.rst", "stories", "story.tmpl"),
)

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
DEPLOY_DRAFTS = False

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
#post_compilers = {
#    "rest": ('.txt', '.rst'),
#    "markdown": ('.md', '.mdown', '.markdown')
#    "html": ('.html', '.htm')
#    }

# What is the default language?

DEFAULT_LANG = "en"
# What languages do you have?
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location

TRANSLATIONS = {
    "en": "",
    }

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
TAG_PATH = "categories"
# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
INDEX_PATH = ""
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / archive.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
ARCHIVE_PATH = ""
# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
RSS_PATH = ""

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []

REDIRECTIONS = []

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
DEPLOY_COMMANDS = []

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py

OUTPUT_FOLDER = 'output'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
#FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
#}

##############################################################################
# Image Gallery Options
##############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
GALLERY_PATH = "galleries"
THUMBNAIL_SIZE = 180
MAX_IMAGE_SIZE = 1280
USE_FILENAME_AS_TITLE = True

##############################################################################
# HTML fragments and diverse things that are used by the templates
##############################################################################

# Data about this site
BLOG_AUTHOR = "Pieter Swinkels"
BLOG_TITLE = "The journey that counts"
BLOG_URL = "http://blog.journeythatcounts.nl"
BLOG_EMAIL = "swinkels.pieter@yahoo.com"
BLOG_DESCRIPTION = "A personal website."

# Name of the theme to use. Themes are located in themes/theme_name
THEME = 'swinkels'

# Show only teasers in the index pages? Defaults to False.
# INDEX_TEASERS = False

# A HTML fragment describing the license, for the sidebar.
# I recomment using the Creative Commons' wizard:
# http://creativecommons.org/choose/
LICENSE = """
    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
    <img alt="Creative Commons License" style="border-width:0; margin-bottom:12px;"
    src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer
CONTENT_FOOTER = u'Contents &copy; 2011-2013 <a href=mailto:"swinkels.pieter@yahoo.com">Pieter Swinkels</a> | Website powered by <a href="http://nikola.ralsina.com.ar">Nikola</a>'

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
# "googleplus" or "facebook"
# COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "the-journey-that-counts"

# Enable Addthis social buttons?
# Defaults to true
# ADD_THIS_BUTTONS = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.

#RSS_LINK = """
    #<link rel="alternate" type="application/rss+xml" title="RSS" href="http://feeds.feedburner.com/LateralOpinion">
    #<link rel="alternate" type="application/rss+xml" title="RSS en Espanol" href="http://feeds.feedburner.com/LateralOpinionEsp">
#"""
RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# This example should work for pretty much any site we generate.
SEARCH_FORM = ""
## This search form is better for the "site" theme where it appears on the navigation bar
#SEARCH_FORM = """
    #<!-- Custom search -->
    #<form method="get" id="search" action="http://duckduckgo.com/" class="navbar-form pull-left">
    #<input type="hidden" name="sites" value="%s"/>
    #<input type="hidden" name="k8" value="#444444"/>
    #<input type="hidden" name="k9" value="#D51920"/>
    #<input type="hidden" name="kt" value="h"/>
    #<input type="text" name="q" maxlength="255" placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
    #<input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
    #</form>
    #<!-- End of custom search -->
#""" % BLOG_URL

# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
ANALYTICS = """
    """

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {
    'analytics': ANALYTICS,
    'blog_author': BLOG_AUTHOR,
    'blog_title': BLOG_TITLE,
    'blog_url': BLOG_URL,
    'blog_desc': BLOG_DESCRIPTION,
    'translations': TRANSLATIONS,
    'license': LICENSE,
    'search_form': SEARCH_FORM,
    # 'disqus_forum': DISQUS_FORUM,
    'content_footer': CONTENT_FOOTER,
    'rss_path': RSS_PATH,
    'rss_link': RSS_LINK,
    # Locale-dependent links for the sidebar
    'sidebar_links': {
        'en': (
            ('/archive.html', 'Archives'),
            ('/categories/index.html', 'Tags'),
            )
        }
    }
