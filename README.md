This is the repository for the project Merge Stories.  You can find the website for the project [here](http://mergestories.com/).  You can find more information on what the project is, who has contributed, licensing, etc, at the project's [about page](http://mergestories.com/pages/About.html).

The project is still being constructed, so pardon the mess.

###Project Overview

MergeStories is built using [Pelican](http://blog.getpelican.com/), a static site generator.  The theme is a modified version of [Pelican Elegant](http://oncrashreboot.com/elegant-best-pelican-theme-features).   The site is published via [Github Pages](https://pages.github.com/), with the help of [ghp-import](https://github.com/davisp/ghp-import).

Potentially interesting files:
+ __CNAME__ is the file which allows viewers going to mergestories.com to view the content of the github pages site.  
+ __deploy.sh__ is a file that the maintainer uses to quickly and easily push changes to the site.
+ __README.md__ is this very file.
+ __requirements.txt__ is a list of requirements that the project needs to run.  (To install them, see below.)
+ __settings.py__ is the configuration file for Pelican.
+ __settings_local.py__ is an extension of the the configuration file for Pelican which allows us to easily develop locally.

Potentially interesting directories:
+ __content__ contains the articles and some of the pages (submit, about) for the site.  
+ __pelican-plugins__ contains the plugins that add functionality to the site.  
+ __themes__ contains the Pelican Elegant theme that we use.  Within Pelican Elegant is the directory __static__ which contains CSS (you'll likely want to edit _custom.css_) and __templates__ which contain templates controlling how the site is displayed.  These are written in HTML and Jinja.

###Contributing

You can contribute stories to the project through the [submit form](http://mergestories.com/pages/Submit.html).

To contribute to Merge Stories itself, you'll want to do the following:

1) __Pick an issue to address.__  

You can find open issues in the [issue tracker](https://github.com/openhatch/oh-contribution-stories/issues).

2) __Contact a project maintainer.__  

Before getting started on an issue, please check in with me so I can make sure the issue is up to date.  This is as simple as saying, "Hi!  I'd like to help with the project." or "Hi!  I'd like to work on issue X."  You can leave a comment on the issue you're interested in, email me at hello@openhatch.org, or say hi via [IRC](http://openhatch.readthedocs.org/en/latest/community/contact.html) (I'm shauna on Freenode, most often found in #openhatch).

3) __Set up the development environment.__  

You will probably need to set up the development environment.  To do this, you'll want to fork and clone the project from Github.  If you're not familiar with git/Github, you might appreciate [this page](https://openhatch.org/wiki/Git_Basics).  

You may want to work within a [VirtualEnv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html). Note: this project's default is to use virtualenv but not activate it, hence our deploy.sh script uses bin/pelican, for instance.  To set up the virtualenv in this way, install the program and then simply type 'virtualenv .' in the top level of the repository.  For subsequent commands you should type bin/pip and bin/pelican instead of pip and pelican.

From there, you may need to install some requirements.  Requirements.txt has the list of requirements.  If you're on Linux, the easy way to install them is to type into your command line: 

    pip install -r requirements.txt

(Note: you may have to first install pip.  You may also run into permissions issues.)

Once you have installed the requirements, you can build the site by typing the following command:

    pelican content -s settings_local.py -v

To view the site, you will need to navigate into the output directory and run the following command:

    python -m SimpleHTTPServer
    
You should now be able to view your site by opening up a browser window and going to the url __http://localhost:8000/__

4) __Make and test your changes.__

There is currently no formal testing suite.  Simply check that your changes have had their intended effect by re-running the following commands:

    pelican content -s settings_local.py -v
    python -m SimpleHTTPServer    

(For ease of use, you can work with two tabs open so you don't need to switch directories each time you run these commands.)

5)  __Submit your changes.__

You can submit your changes via pull request (see [our Git Basics page again](https://openhatch.org/wiki/Git_Basics) for more details).  Please also leave a comment on the [licensing agreement](https://github.com/openhatch/oh-contribution-stories/issues/27) to formally agree to let us use your work. 

6)  __Wait.__  

I'll try to comment on your pull request within a day or two of getting it, and give you feedback shortly thereafter.  If it has been more than a few days without a response, please feel free to ping me.  I may not be able to get to your request any quicker, but I am always happy to know that you're still around and interested!

###Miscellaneous Stuff

__Deploying.__

For site maintainers, you can update the live site by running the deploy script:

    ./deploy.sh

To just add to gh-pages:

    ghp-import output -m "Regenerate site"

(See http://docs.getpelican.com/en/3.1.1/tips.html)

__Tagging structure.__

Tags can be conceptually grouped, for instance there is a set of "helped by" tags -- these should be separated by a dash.
This is not a comprehensive list of tags.  

project - X         # use all lowercase  
difficulties encountered - build  
difficulties encountered - language barrier  
tools used - git  
tools used - javascript console  
helped by - computer club  
helped by - friend  
helped by - other irc  
helped by - project irc  
kind of contribution - code  
kind of contribution - translation  
kind of contribution - documentation  
motivation - work  
motivation - school  
previous involvement - none  
previous involvement - user of the program  
relationship with maintainers - friends  
relationship with maintainers - met at event  
relationship with maintainers - socialized on irc  

