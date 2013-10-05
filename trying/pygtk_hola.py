'''
Created on Oct 5, 2013

@author: knick
'''
#!/usr/bin/env python

import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    print "error import pygtk"
try:
    import gtk
    import gtk.glade
except:
    print "error import gtk"
    print "error import gtk.glade"
    sys.exit(1)
    
    
class HellowWorldGTK:
    """This is an Hello World GTK application"""
    
    def on_window1_destroy(self, widget, data=None):
        #DBclose()
        gtk.main_quit()

    def on_btnHelloWorld_clicked(self, button):
        print "Hello World!"
        
    def __init__(self):
        try:
            self.builder = gtk.Builder()
            self.builder.add_from_file("interf_pygtk.glade")
        except:
            self.show_error_dlg("Failed to load UI XML file: pyhelloworld.glade")
            sys.exit(1)
            
        #Set the Glade file
        #self.gladefile = "pyhelloworld.glade"  
        #self.wTree = gtk.glade.XML( "pyhelloworld.glade")
        self.window = self.builder.get_object("window1")
        self.btnHelloWorld = self.builder.get_object("btnHelloWorld")
        #Create our dictionay and connect it
        #dic = { "on_btnHelloWorld_clicked" : self.on_btnHelloWorld_clicked,
        # "on_window1_destroy" : gtk.main_quit}
        #self.wTree.signal_autoconnect(dic)
        self.builder.connect_signals(self)
        
        # Run main application window
    def main(self):
        #self.window.maximize()
        self.window.show()
        gtk.main()
            
            
if __name__ == "__main__":
    hwg = HellowWorldGTK()
    hwg.main()
    #gtk.main()
            
        
            
            