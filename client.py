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
import readline
COMMANDS = ['!exit']
import urllib,urllib2
from time import sleep

URL ='http://localhost/util.php'

def complete(text, state):
    for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

userCommand = ""
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

while userCommand != "!exit":
    userCommand = raw_input('[station]: ')
    #URL du formulaire
    
    
    #Champ et valeur du formulaire 
    params = urllib.urlencode({'action':'write','buf': 'cmd', 'msg':userCommand}) 
    #Envoi de la requete
    req = urllib2.Request(URL, params)
    urllib2.urlopen(req)
    
    #Recuperation de flux cote client
    trys = 0
    
    while trys<10:
        sleep(2)
        params = urllib.urlencode({'action': 'read', 'buf': 'out'})
        req = urllib2.Request(URL, params)
        response = urllib2.urlopen(req)
        data=response.read()
        print 'data = "'+data+'"'
        if data == '':
            trys += 1
        else:
            break
    if data != "":
        print data
    else:
        print '[!] responce timed out'
    
    
    






