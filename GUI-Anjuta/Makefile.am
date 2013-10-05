## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

clemente_clientdocdir = ${prefix}/doc/clemente_client
clemente_clientdoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(clemente_clientdoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(clemente_clientdocdir)
