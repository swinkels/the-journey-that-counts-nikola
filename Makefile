all:
	# some of the required Python packages depend need packages that cannot
	# be provided by pip
	sudo apt-get install libxml2-dev libxslt-dev
	pip install -r requirements.txt
	nikola build
