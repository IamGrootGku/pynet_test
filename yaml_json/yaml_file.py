#!/usr/bin/env python
import yaml

my_list = range(10)
my_list.append("hi")
my_list.append("there")
my_list.append({})

print "Created list, here are values:\n"

print my_list

my_list[-1]['model'] = 'c2911'
my_list[-1]['version'] = '15.3.2T'
my_list[-1]['interface id'] = range(4)

print "\nDictionary items have been added.\n"
print "Here is my_list updated:\n"

print my_list

with open("yaml_file_result.yml", "w") as f:
  f.write('---\n\n')
  f.write(yaml.dump(my_list, default_flow_style=False))
  f.close()

print "\nYaml list outputted to file.\n"
print "Done!"
