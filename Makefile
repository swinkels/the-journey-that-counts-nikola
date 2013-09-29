all: install
	nikola build
	@echo Execute \"nikola serve\" to start serving the website locally

install:
	# some of the required Python packages need packages that are not
	# provided by pip
	sudo apt-get install libxml2-dev libxslt-dev
	pip install -r requirements.txt
