#!/usr/bin/env python
# -*- coding:utf-8 -*

#20 JSONデータの読み込み
import re
import json

target = "イギリス"
comp_target = re.compile(target)

with open("jawiki-country.json","r") as f, open("jawiki-England.txt","w") as Eng:
    for line in f:
        loadline = json.loads(line)

        if comp_target.search(loadline["text"]):
            Eng.write(loadline["text"] + "\n")

