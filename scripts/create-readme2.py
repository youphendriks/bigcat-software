#!/usr/bin/env python3
import json
from py_markdown_table.markdown_table import markdown_table

def createTable(path):
    with open(path) as f:
        jsonlib = json.load(f)
    markdown = markdown_table(jsonlib).get_markdown()
    print(markdown)

createTable("db/research_archive.json")
createTable("db/data_analysis.json")
createTable("db/software.json")
