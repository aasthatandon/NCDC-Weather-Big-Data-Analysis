#!/usr/bin/env python

import sys

for line in sys.stdin:
  usaf_id, visibility_dist = line.strip().split("\t")
  print("%s\t%s" % (usaf_id, visibility_dist))






