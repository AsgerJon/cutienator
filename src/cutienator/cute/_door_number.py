"""
DoorNumber is the number of a member of an enum of Qt, on its way into
a function of Qt that takes the number.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations


class DoorNumber(int):
  """
  The number a member of an enum of Qt stands for, while it is handed
  to a function that takes an 'int'. You never make one.

  Why it exists
  -------------

  A is A: a member of an enum is only itself, and never a number. Where
  a function of Qt takes a number, a member may still be given, as C++
  allows. When no signature of a cute function takes a call as it is
  written, 'CuteSpace' swaps each member in the call for a 'DoorNumber'
  of its number and tries once more. A 'DoorNumber' is an 'int', so a
  signature naming 'int' takes it.

  It is a class of its own for one reason: the enums and flags of Qt
  refuse it. A plain number may stand for the member that has it, so
  'setFocusPolicy(11)' works. A number that came off a member of one
  enum must not turn into a member of another on the way in, which C++
  refuses as well.
  """
