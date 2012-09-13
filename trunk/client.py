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

class main:
    def __init__(self):
        #TODO: import commands from server
        self.commands = ['ls', 'mv', 'cp'] 
        self.command = ''
    
    def execute(self):

        print 'i am client'
        while self.command != 'exit':
            self.command = raw_input('> ')
        return
    
    def complete(self, text, state):
        print text
        for cmd in self.commands:
            if cmd.startswith(text):
                if not state:
                    return cmd
                else:
                    state -= 1


if __name__ == '__main__':        
    instance = main()
    
    readline.parse_and_bind("tab: complete")
    readline.set_completer(instance.complete)
    
    raw_input('> ')
    
    instance.execute()
    
    