#!/usr/bin/env python3
import json
import pandas as pd
from py_markdown_table.markdown_table import markdown_table

def createTable(path):
    df = pd.read_json(path)
    df = df.transpose()
    df.columns = df.iloc[0]
    df = df[1:]
    markdown = df.to_markdown()
    print(markdown)

createTable("db/research_archive.json")
createTable("db/data_analysis.json")
createTable("db/software.json")
