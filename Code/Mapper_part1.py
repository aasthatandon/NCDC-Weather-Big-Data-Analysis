#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (observation_date, wind_direction, quality_code) = (val[15:21], val[60:63], val[63:64])
  if (wind_direction != "999" and re.match("[01459]", quality_code)):
    print("%s\t%s" % (observation_date, wind_direction))
