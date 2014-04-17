#!/bin/python
# -*-  coding:utf8   -*-



from collections import defaultdict

item_counter=defaultdict(int)

try:
	while True:
		line=raw_input().strip()
		item_counter[line]+=1
except EOFError:
	pass

for item in sorted(item_counter.iteritems(),key=lambda x:x[1],reverse=True):
	print item[0],"\t",item[1]


