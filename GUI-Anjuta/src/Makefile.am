## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = clemente_client.ui


## The main script
bin_SCRIPTS = clemente_client.py

## Directory where .class files will be installed
clemente_clientdir = $(pythondir)/clemente_client


clemente_client_PYTHON = \
	clemente_client.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
