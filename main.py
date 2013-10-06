#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 valentin basel <valentin@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import socket
import sys
import interface

# import interface
sys.path.append("GUI-Anjuta/src/")

from clemente_client import Interface

class Main():
	""" ClassName  Main
    	Clase cliente para interactuar con el servidorjango
	"""

def HELP():
	print "Ayuda para entrar a ClementeCliente;"
def VERSION():
	print "version de ClementeCliente 1.0"
def IP():
	pass	
def main():
	arg={"-h": HELP,"-v":VERSION, "-ip": IP}
	if len(sys.argv)>1:
		for dat in sys.argv[1:]:
			if arg.has_key(dat):
				arg[dat]()
			else:
				print "No se reconoce el comando intetar de nuevo", dat
				exit()
	#cliente = interface.Controller("127.0.0.1",8002)
	Interface()

	return 0

if __name__ == '__main__':
	main()

