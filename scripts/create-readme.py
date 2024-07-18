#!/usr/bin/env python3
import os
import json
from py_markdown_table.markdown_table import markdown_table

def importProjectlist(path):
    with open(path) as f:
        projectlist = json.load(f)
    for project in projectlist:
        name = project["name"]
        rawlink = project["rawlink"]
        os.system("rm -vr db/" + name)
        os.system("mkdir -p db/" + name)
        os.system("wget -O db/" + name + "/README.md " + rawlink)
    return projectlist

def importTaglist(path):
    with open(path) as f:
        taglist = json.load(f)
    print("Taglist:")
    print(taglist)
    return taglist

def extractData(projectlist):
    for project in projectlist:
        ##name = project["name"]
        projectlib = open(("db/" + name + "/README.md"), 'r').read()
        tagdict = extractTags(projectlib, taglist)
        createJson(tagdict, name)

def extractTags(projectlib, taglist):
    tagdict = {}
    for tag in taglist:
        try:
            split1 = projectlib.split("<!--"+tag+"-->")
            split2 = split1[1].split("<!--/"+tag+"-->")
            ## tagdict[tag]=split2[0]
            tagdict[tag]=":heavy_check_mark:"
        except:
            tagdict[tag]=":x:"
    print(tagdict)
    return tagdict

def createJson(tagdict, name):
    os.system("rm -vr db/collect.json")
    collectjson = []
    for project in projectlist:
        name = project["name"]
        projectlib = open(("db/" + name + "/README.md"), 'r').read()
        tagdict = extractTags(projectlib, taglist)
        with open(('db/' + name + '/' + name+'.json'), 'w') as f:
            json.dump(tagdict, f)
        collect.append(tagdict)
    return collect

#def saveMarkdownTable(dbmarkdown):

projectlist = importProjectlist("db/project_list.json")
taglist = importTaglist("db/tag_list.json")
extractData(projectlist)
