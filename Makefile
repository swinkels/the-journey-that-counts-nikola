all: install install-posts
	@echo
	@echo "**** Build the site."
	@echo
	nikola build
	@echo
	@echo "**** Execute \"nikola serve\" to start serving the website locally."
	@echo

install:
	@echo
	@echo "**** Install the required (Python) packages, e.g. 'nikola' and its"
	@echo "**** dependencies."
	@echo
	@# You can also use this target to update a current installation.
	@#
	@# Only install the required Python packages when we are running in a
	@# virtualenv: remove this restriction when you do not mind adding
	@# system-wide site packages.
ifdef VIRTUAL_ENV
	@echo "**** Install the packages on which the required Python packages depend but"
	@echo "**** that pip cannot install for us."
	@echo
	sudo apt-get install libxml2-dev libxslt-dev python-dev
	@echo
	@echo "**** We assume the current working directory is a Mercurial repo so we"
	@echo "**** update to the latest state."
	@echo
	hg pull ; hg update
	@echo
	@echo "**** Install (or update) the required Python packages."
	@echo
	pip install -r requirements.txt
else
	@echo "**** Skip the installation of required (Python) packages as we are not"
	@echo "**** running in a virtualenv."
endif

install-posts: _posts
	@echo
	@echo "**** Update the blog posts to the head of the remote repo."
	@echo
	@# Note that the blog posts for the Nikola version of the site
	@# are located in branch 'nikola'.
	cd _posts; hg pull ; hg update nikola

_posts:
	@echo
	@echo "**** Retrieve the blog posts from the remote repo."
	@echo
	@# We assume we can use ssh to retrieve the posts from the remote
	@# repo. If that is not the case, for example because you are not me :),
	@# you can clone the posts from the https address of the repo at
	@#
	@#   https://swinkels@bitbucket.org/swinkels/the-journey-that-counts-contents
	hg clone ssh://hg@bitbucket.org/swinkels/the-journey-that-counts-contents _posts
