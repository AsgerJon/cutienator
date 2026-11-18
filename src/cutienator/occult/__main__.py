"""
Prints what a shared object offers.

  python -m cutienator.occult FILE         how many names FILE offers
  python -m cutienator.occult FILE TEXT    each function containing TEXT,
                                           readable spelling, a tab, then
                                           the stored spelling
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import sys

from . import SharedObject


def main(*args: str) -> int:
  """
  Prints what the shared object named by the arguments offers.

  Parameters
  ----------

  *args : str
    The path of the file, optionally followed by the text to look for.

  Returns
  -------

  int
    The exit code: 0, or 2 when the arguments are not one or two.
  """
  if len(args) not in (1, 2):
    print(__doc__.strip(), file=sys.stderr)
    return 2
  sharedObject = SharedObject(args[0])
  if len(args) == 1:
    infoSpec = """'%s' offers %d names, %d of them functions."""
    counts = (len(sharedObject), len(sharedObject.functions()))
    print(infoSpec % (sharedObject.path, *counts))
    return 0
  for symbol in sharedObject.search(args[1]):
    if symbol.isFunction():
      print('%s\t%s' % (symbol.readable, symbol.mangled))
  return 0


if __name__ == '__main__':
  sys.exit(main(*sys.argv[1:]))
