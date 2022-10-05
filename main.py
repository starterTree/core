#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO voir rempacer icon par entree ? ou/et sinon incruster icone > (ou toutes icons ?) dans le parseur


# load Plugin# 

from Plugin import pluginsA
from Plugin import pluginsB

from modules import loadData, mainPrompt, bottomToolbar

from sys import exit
import os
import sys
from prompt_toolkit import PromptSession
from shlex import quote
from rich.pretty import pprint
import modules.utils

def getTag(result):
    myComplete = {}
    myCompleteL = []
    for r in result:
        if "tags" in path_entry_name_content[r]:
            if type(path_entry_name_content[r]["tags"]) == list:
                for i in path_entry_name_content[r]["tags"]:
                    myComplete[i] = {}
    for i in myComplete:
        myCompleteL.append(i)

    completer = FuzzyCompleter(WordCompleter(myCompleteL, ignore_case=True))

    #print(myCompleteL)
    icon = "search > tag >"
    if detectNerdFont: icon = "   "
    session = PromptSession(icon + " ", style=style, key_bindings=bindings)
    prompt = session.prompt(pre_run=session.default_buffer.start_completion, default="", completer=completer)



tmpDir = modules.utils.getTmpDir(default=os.environ['HOME'] + '/.starterTree/')
configDir =  modules.utils.getConfigDir(defaultConfigDir=os.environ['HOME'] + '/.config')
defaultConfigFile=os.environ['HOME'] + '/.config/starterTree/config.yml'
try:
    configFile = str(sys.argv[1])
except IndexError:
    configFile = defaultConfigFile
promptTitle =  modules.utils.getPromptTitle(promptTitle=os.path.basename(sys.argv[0]))
#absolute_path_main_config_file = os.path.dirname(configFile) + "/"


def main(configFile,promptTitle,tmpDir,plugins=pluginsB):
    # charge data ( data yaml from plugins and data yaml file or data yaml plugins and data demo)
    starterTreeDATA = {
        "path_entry_name_content": {},
        "menu_completion": {},
        "style": {
            "completionMenu": {}
        },
        "settings": {},
        "config": {
            "name" : "default",
            "displayVersion": True,
        },
        "tmpDir": tmpDir,
        "plugins": plugins 
    }

    loadData.loadData(configFile=configFile, data=starterTreeDATA)
    loadData.loadData(configFile=os.environ['HOME'] + '/.config/starterTree/.config.yml'
, data=starterTreeDATA)
    mainPrompt.execMainPromptSession(data=starterTreeDATA, promptTitle=promptTitle,
                                     bottomToolbar=bottomToolbar.getToolbar(starterTreeDATA))


if __name__ == "__main__":
    main(plugins=pluginsB.values(),configFile=configFile,promptTitle=promptTitle,tmpDir=tmpDir)

exit()
