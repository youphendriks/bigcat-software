#!/usr/bin/env python3
import os
import json
from py_markdown_table.markdown_table import markdown_table

taglist = [
    "Title",
    "Statement",
    "Description",
    "License",
    "Dependencies",
    "Code language",
    "Available platform",
    "Interface CLI",
    "Interface GUI",
    "Interface web platform",
    "Input format",
    "Output format",
    "Source code",
    "Documentation link",
    "Installation instructions",
    "Zenodo link",
    "Citation instructions"
]

def importProjectList(path):
    with open(path) as f:
        projectlist = json.load(f)
    for project in projectlist:
        name = project["name"]
        rawlink = project["rawlink"]
        os.system("mkdir -p db/" + name)
        os.system("wget -O db/" + name + "/README.md " + rawlink)
    return projectlist

def extractData(projectlist):
    for project in projectlist:
        name = project["name"]
        projectlib = open(("db/" + name + "/README.md"), 'r').read()
        tagdict = extractTags(projectlib, taglist)

def extractTags(projectlib, taglist):
    tagdict = {}
    for tag in taglist:
        split1 = projectlib.split("<!--"+tag+"-->")
        split2 = split1[1].split("<!--/"+tag+"-->")
        tagdict[tag]=split2[0]
    print(tagdict)
    return tagdict

#def createJson(dblist):

#def saveJson(dbjson):

#def createMarkdownTable(dbjson):

#def saveMarkdownTable(dbmarkdown):

projectlist = importProjectList("db/project_list.json")
extractData(projectlist)
