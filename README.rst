Introduction
------------

This repo contains the code to build the static blogging website at
http://blog.journeythatcounts.nl. The website is build using `Nikola`_, a
static website and blog generator written in Python.

The repo does not contain the actual blog posts. In the root of the repo there
is a Makefile that clones the blog post repo into a subdirectory, where they
will be automatically picked up by Nikola.

Prerequisites
-------------

The code in this repo has been build and tested using the 32-bit version of
Xubuntu 12.04 LTS, Python 2.7.3 and virtualenv 1.7.1.2. You will need the
Mercurial version control tool to clone the code repo.

Getting started
---------------

To work with this repo, first clone it from Bitbucket::

  $> hg clone ssh://hg@bitbucket.org/swinkels/the-journey-that-counts-nikola

The above statement assumes you have ssh access to that repo. If you do not
have ssh access, you can clone the repo using its https address::

  $> hg clone https://swinkels@bitbucket.org/swinkels/the-journey-that-counts-nikola

This creates a copy of the repo in subdirectory the-journey-that-counts-nikola.

The root of that subdirectory contains a Makefile that installs the required
system and Python packages but only when it executes in a virtualenv [1]_. This
restriction is there to avoid the accidental installation of system-wide Python
packages. In the remainder of this document we assume that you execute the
example command-line statements in a virtualenv named "nikola".

To install the required packages, retrieve the blog posts and build the site,
execute the following command in the root of the repo::

  (nikola) $> make

Please note that even the local installation of Python packages requires the
installation of (a couple of) system packages. These packages are installed
using the sudo command, so you will need to provide your password.

If the "make" command was successful, the last section of the output will look
something like this::

  **** Build the site.

  nikola build
  Scanning posts..done!
  .  render_site:output/categories/index.html
  .  render_sources:output/posts/scrum-tasks-estimates.rst
  .  render_sources:output/posts/scrum-bastard.rst
  ...
  .  render_tags:output/categories/dictionary.xml
  .  render_tags:output/categories/scrum.xml
  .  sitemap:output/sitemap.xml

  **** Execute "nikola serve" to start serving the website locally.

  (nikola) $>

To start serving the site locally, execute the following command::

  (nikola) $> nikola serve

This will serve the static website at 127.0.0.1 at port 8000. Start your
browser and visit http://127.0.0.1:8000 or http://localhost:8000 to see the
website.

.. _Nikola: http://getnikola.com/

.. _[1]: If you do not know what a virtualenv is and why it is a good idea to
use one, we refer to http://docs.python-guide.org/en/latest/dev/virtualenvs/
for more information.
