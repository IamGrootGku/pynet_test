#!/user/bin/env python

import json

my_list = range(6)
my_list.append("json")
my_list.append("list")
my_list.append({})

print "\nCreated list for json entries.\n"

my_list[-1]['platform'] = 'Router'
my_list[-1]['version'] = '15.4M'
my_list[-1]['interface'] = range(4)

print "Dictionary items have been added.\n"

print "Here is current json list items:\n\n"
print json.dumps(my_list)

with open("json_file_result.json", "w") as f:
  json.dump(my_list, f)
  f.close()

print "json file json_file_result.json was created.\n"
print "Done!"

