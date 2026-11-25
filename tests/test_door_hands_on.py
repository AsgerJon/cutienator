"""
TestDoorHandsOn tests that a function read off an object before a class
it waited for was made still takes a call that hands over an object of
that class: the door hands the call on to the function as it is now.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.work_test import BaseTest

import cutienator
from cutienator.occult import Rituals

#  It runs in a Python of its own, which has not brought in QByteArray.
#  Each line it prints is a name, a colon and what was found.
READ_BEFORE = """
import sys

from worktoy.waitaminute.dispatch import DispatchException

from cutienator.QtCore import QMimeData

file = 'cutienator.QtCore._q_byte_array'
mime = QMimeData()
kept = mime.setData
print('brought in at first:', file in sys.modules)
#  Python reads 'mime.setData' first, and 'mime.data' then brings in
#  QByteArray, which 'setData' waited for.
mime.setData('a/b', mime.data('a/b'))
print('brought in by the argument:', file in sys.modules)
from cutienator.QtCore import QByteArray
kept('a/b', QByteArray('xyz'))
print('through the function kept:', mime.data('a/b').size())
for name, call in (('kept', kept), ('read now', mime.setData)):
  try:
    call('a/b', 5)
    print('a wrong call, %s: taken' % name)
  except DispatchException as exception:
    named = 'QMimeData.setData' in str(exception)
    print('a wrong call, %s: refused, naming the function: %s' % (
        name, named))
"""


class TestDoorHandsOn(BaseTest):
  """Runs one program in a Python of its own."""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.summon()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_function_read_before_its_class_came_in(self) -> None:
    """A call whose own arguments bring in the class the function
    waited for is taken, and so is a call through a function kept from
    before. A wrong call is refused either way."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', READ_BEFORE),
        capture_output=True, text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    expected = [
        'brought in at first: False',
        'brought in by the argument: True',
        'through the function kept: 3',
        'a wrong call, kept: refused, naming the function: True',
        'a wrong call, read now: refused, naming the function: True',
    ]
    self.assertEqual(done.stdout.strip().split('\n'), expected)
