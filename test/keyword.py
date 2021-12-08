from iptcinfo import IPTCInfo
import sys

fn = './images/0.png'
# Create new info object
info = IPTCInfo(fn)
print(info.keywords)