#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

#print crypto_map

print "\n\nExercise 8\n\n"

i = 0

for cmap in crypto_map:
  cp = crypto_map[i]
  print cmap.text
  for child in cp.all_children:
    print child.text
  i += 1

print "\n\n"

i = 0

pfs2 = cisco_cfg.find_objects(r"group2")

print "Exercise 9\n\n"

for p in pfs2:
  print p.parent.text

print "\n\nExercise 10\n\n"

not_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

for n in not_aes:
  print n.text
  for nn in n.children:
    if "transform-set" in nn.text:
      print nn.text

print "\n\nDone!\n"
  

