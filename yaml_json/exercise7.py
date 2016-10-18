#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

print "\nOpening yaml file yaml_file_result.yml.\n"
print "Putting yaml data into yaml_list.\n\n"

with open("yaml_file_result.yml") as yf:
  yaml_list = yaml.load(yf)
  yf.close()

print yaml.dump(yaml_list, default_flow_style=False)
print "\nDone with YAML!"

print "\n\n\nOpening json file json_file_result.json.\n"
print "Putting json data into json_list.\n\n"


with open("json_file_result.json") as jf:
  json_list = json.load(jf)
  jf.close()

pp(json_list)

print "\nDone with JSON!"

