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
COMMANDS = ['exit', 'extra', 'extension', 'stuff', 'errors',
            'email', 'foobar', 'foo','ls','pwd']
import urllib,urllib2
import commands
from time import sleep
def complete(text, state):
    for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

section = ""
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
while section != "exit":
    section = raw_input('[station]: ')
    #URL du formulaire
    url ='http://localhost/util.php'

    
    

    #Champ et valeur du formulaire 
    values={'action':'write','buf': 'cmd', 'msg':section}
    params = urllib.urlencode(values)
    
    #Envoi de la requete
    req = urllib2.Request(url, params)
    
    #Recuperation de la commande cote serveur
    response2 = urllib2.urlopen(req)
    data2=response2.read()
    
    
    #Execution de la commande(pas encore faite ) et envoi le flux dans out.txt
    s=commands.getoutput(data2)
    values1={'action': 'write','buf': 'out','msg':s}
    params1=urllib.urlencode(values1)
    
    #Envoi de la requete cote serveur
    req1=urllib2.Request(url,params1)
    
    #Recuperation de flux cote client
    sleep(15)
    values2={'action': 'read','buf': 'out'}
    response=urllib2.urlopen(req1)
    data=response.read()
    print data
    
    






