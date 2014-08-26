# blocktwin.py  26/08/2014  D.J.Whale
#
# An algorithm for turning a twitter handle into a minecraft block
# type.
#
# @MartinOHanlon has been pretty systematic in working out all the
# extraData values on all platforms, however if there are any missing
# we don't want to have to re-sequence this list. To protect against
# this, the algorithm works out the number of the blockid, then adds
# on the extraData. This allows the extraData to expand or even
# vary between platforms but still generate consistent blocks.


ALGORITHM_VERSION = 1
PLATFORM = "RaspberryPi"

# there are block variances between bukkit and pi, not sure quite
# the best way to differentiate those yet so that we are consistent
# across platforms - we will probably use the minimum subset of
# blocks and extradata's shared by all platforms, if we can
# work that out. For the moment, we assume this only runs on the
# RaspberryPi, and we can solve that issue later with an updated
# algorithm version.


from blocks import *

def getHandle(twit):
  """Tidy up a handle"""
  if twit == None:
    return ""
  twit = twit.strip()
  if len(twit) == 0:
    return ""
  if twit[0] == '@':
    twit = twit[1:]
  return twit
  
    
def checksum(s, m):
  """Create a checksum for a string of characters, modulo m"""
  # note, I *think* it's possible to have unicode chars in
  # a twitter handle. That makes it a bit interesting. 
  # We don't handle unicode yet, just ASCII
  total = 0
  for ch in s:
    # no non-printable ASCII chars, including space
    # but we want "!" to represent an increment of 1, hence 32 below
    total = (total + ord(ch)-32) % m
  return total
  
  
def getBlockTwin(handle):
  modulo = len(BLOCK_IDS.index)-1 # take off AIR
  handle = getHandle(handle)
  number = checksum(handle, modulo)
  # version 1 does not use extraData
  blockid   = BLOCK_IDS.index[number+1] # skip over AIR
  extraData = None
  return blockid, extraData
  
  
def getBlockName(blockid, extraData=None):
  return "(TODO:" + str(blockid) + " " + str(extraData) + ")"


def isAffectedByGravity(blockid):
  # if affected by gravity, you might not want to build with it
  # unless it is on a non affected block
  return False # TODO

  
def isActive(blockid):
  # if it is active you might want to be careful where you place
  # it, e.g. cactus cannot go next to cactus
  return False # TODO



# TEST HARNESS
if __name__ == "__main__":
  twit = raw_input("twitter handle? ") # python2
  #twit = "@whaleygeek"
  
  blockid, extradata = getBlockTwin(twit)
  name = getBlockName(blockid, extradata)
  
  print("Hello " + twit)
  print("Your block id is:" + str(blockid))
  print("Your extraData is:" + str(extradata))
  print("This block is called:" + name)
  
# END
