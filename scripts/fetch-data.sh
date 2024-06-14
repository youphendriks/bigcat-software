#!/usr/bash
rm -f open.txt
touch open.txt

mkdir -p db/neo4j
wget -O db/neo4j/README.md https://raw.githubusercontent.com/youphendriks/bigcat-software-project/main/README.md
