#!/usr/bin/python3

import re

def pars_grub():

  result_str = ""
#  grubf = open("node1.example.com/etc/default/grub", "r")

  init_kernel = r"^GRUB_CMDLINE_LINUX="
  init_ifname = r".*net\.ifnames=0.*"
  init_biosde = r".*biosdevname=0.*"

  with open("node1.example.com/etc/default/grub", 'r') as f:
    for line in f:
      if re.match(init_kernel, line):
        result_str = line
        if not re.match(init_ifname, line):
          result_str = result_str[0:-2] + ' net.ifnames=0 "'
        if not re.match(init_biosde, line):
          result_str = result_str[0:-2] + ' biosdevname=0"'       
        return result_str.strip()


print(pars_grub())
