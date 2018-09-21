#!/usr/bin/env python2
import psutil

memory = psutil.virtual_memory()
swap   = psutil.swap_memory()

totalusedpercent = float(swap.used + memory.used) / (swap.total + memory.total)
totalfree = (swap.total + memory.total) - (swap.used + memory.used)

output = """<?xml version="1.0" encoding='UTF-8'?>
<prtg>
  <result>
    <channel>Physical Used Percent</channel>
    <float>1</float>
    <unit>Percent</unit>
    <value>{}</value>
  </result>
  <result>
    <channel>Physical Free</channel>
    <float>0</float>
    <unit>BytesMemory</unit>
    <value>{}</value>
  </result>
  <result>
    <channel>Swap Used Percent</channel>
    <float>1</float>
    <unit>Percent</unit>
    <value>{}</value>
  </result>
  <result>
    <channel>Swap Used</channel>
    <float>0</float>
    <unit>BytesMemory</unit>
    <value>{}</value>
  </result>
  <result>
    <channel>Swap Free</channel>
    <float>0</float>
    <unit>BytesMemory</unit>
    <value>{}</value>
  </result>
  <result>
    <channel>Total Used Percent</channel>
    <float>1</float>
    <unit>Percent</unit>
    <value>{}</value>
  </result>
  <result>
    <channel>Total Free</channel>
    <float>0</float>
    <unit>BytesMemory</unit>
    <value>{}</value>
  </result>
  <text>OK</text>
</prtg>""".format(memory.percent,
                  memory.available,
                  swap.percent,
                  swap.used,
                  swap.free,
                  totalusedpercent,
                  totalfree)

print(output)
