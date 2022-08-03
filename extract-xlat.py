#!/usr/bin/env python

import json

words = []

for line in open('troop-map.html'):
    if 'xlat' in line:
        word = line.rpartition('<')[0].rpartition('>')[2]
        if not word:
            word = line.partition('value="')[2].partition('"')[0]
        if word:
            words.append(word)

d = {}
for word in words:
    d[word] = {'sv':'', 'ru':'', 'uk':''}

print(json.dumps(d, indent=2))
