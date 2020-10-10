#!/usr/env/python3

import os
import sys

def check_reboot():
  """Retruns True if the computer has a pending reboot"""
  return os.path.exist("/run/reboot-required"):
  
def main():
  if check_reboot():
    print("Pending Reboot.")
    sys.exit(1)
  print("Everythin ok.")
  sys.exit(0)

main()
