#!/usr/bin/env python3
import os
import json
from py_markdown_table.markdown_table import markdown_table

def importProjectList(path):
    with open(path) as f:
        projectlist = json.load(f)
    for project in projectlist:
        name = project["name"]
        rawlink = project["rawlink"]
        os.system("mkdir -p ../db/" + name)
        os.system("wget -O ../db/" + name + "/README.md " + rawlink)
    return projectlist

def extractData(projectlist):
    for project in projectlist:
        name = project["name"]
        projectlib = open(("../db/" + name + "/README.md"), 'r').read()
        split1 = projectlib.split('<!--Statement-->')
        print(split1)

#def createJson(dblist):

#def saveJson(dbjson):

#def createMarkdownTable(dbjson):

#def saveMarkdownTable(dbmarkdown):



projectlist = importProjectList("../db/project_list.json")
extractData(projectlist)
