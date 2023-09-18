#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (usaf_id, visibility_dist,quality_code) = (val[4:10], val[78:84], val[84:85])
  if (visibility_dist != "999999" and re.match("[01459]", quality_code)):
    print("%s\t%s" % (usaf_id, visibility_dist))
