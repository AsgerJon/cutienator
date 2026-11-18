"""Builds the example, then calls each of its functions and prints."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from . import Build, openExample, readText

def main() -> int:
  """
  Builds the shared object and calls every function it offers.

  Returns
  -------

  int
    The exit code, 0.
  """
  here = os.path.dirname(os.path.abspath(__file__))
  build = Build()
  build.setRitualFiles(
      os.path.join(here, 'q_object.cpp'),
      os.path.join(here, 'q_byte_array.cpp'),
  )
  build.setTargetFile(os.path.join(here, 'libexample.so'))
  qtFolder = build.getQtSharedObjectFolder()
  build.setQtSharedObjects(os.path.join(qtFolder, 'libQt6Core.so.6'))
  print(build)
  print('The command:')
  print('  %s' % ' '.join(build.getCommand()))
  print('Built: %s' % build.run())
  ours = openExample(build.getTargetFile())

  mother = ours.QObject_new(None)
  child = ours.QObject_new(mother)
  print('mother is at %s, child at %s' % (hex(mother), hex(child)))

  same = ours.QObject_parent(child) == mother
  print('child.parent() is mother: %s' % same)
  print('mother.parent(): %s' % ours.QObject_parent(mother))
  print('child.isWidgetType(): %s' % ours.QObject_isWidgetType(child))

  before = ours.QObject_blockSignals(child, True)
  print('child.blockSignals(True) gave the old state: %s' % before)
  print('child.signalsBlocked(): %s' % ours.QObject_signalsBlocked(child))

  for className in (b'QObject', b'QWidget'):
    answer = ours.QObject_inherits(child, className)
    print('child.inherits(%r): %s' % (className, answer))

  ours.QObject_setObjectName(child, 'småkage'.encode('utf-8'))
  name = readText(ours, ours.QObject_objectName(child))
  print('child.objectName(): %r' % name)

  ours.QObject_setParent(child, None)
  print('after child.setParent(None): %s' % ours.QObject_parent(child))

  ours.QObject_delete(child)
  ours.QObject_delete(mother)
  print('Both deleted, and Python is still alive.')
  return 0


if __name__ == '__main__':
  sys.exit(main())
