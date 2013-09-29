all: install install-posts
	nikola build
	@echo Execute \"nikola serve\" to start serving the website locally

install:
	# some of the required Python packages need packages that are not
	# provided by pip
	sudo apt-get install libxml2-dev libxslt-dev
	hg pull ; hg update
	pip install -r requirements.txt

install-posts: _posts
	cd _posts; hg pull ; hg update nikola

_posts:
	hg clone ssh://hg@bitbucket.org/swinkels/the-journey-that-counts-contents _posts
