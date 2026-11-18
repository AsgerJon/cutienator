"""The trials of QObject."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import Trial

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple


def qObjectTrials() -> Tuple[Trial, ...]:
  """
  Gives every trial written for QObject so far.

  Each trial is new every time this is called, so a caller may add steps
  to one without changing what the next caller gets.

  Returns
  -------

  Tuple[Trial, ...]
    The trials, each with its name set and its steps written, ready for
    a 'Judge' to hear.
  """
  parent = Trial()
  parent.setName('QObject: parent and setParent')
  parent.make('mother', 'QObject')
  parent.make('child', 'QObject')
  parent.expectNothing('child', 'parent')
  parent.call('child', 'setParent', 'mother')
  parent.expectSame('child', 'parent', 'mother')
  parent.expectNothing('mother', 'parent')
  parent.call('child', 'setParent', None)
  parent.expectNothing('child', 'parent')
  return (parent,)
