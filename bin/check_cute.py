"""
Brings in every cute class of every part of Qt on the machine it runs
on, and makes a few objects and uses them as a program would, against
the target files built there. It runs after 'bin/check_summon.py' in the
four horsemen, so each of the four systems shows that the Python side
works, not only that the rituals build.

  PYTHONPATH=src QT_QPA_PLATFORM=offscreen \\
    python bin/check_cute.py REPORT_FILE

Two checks:

1. Bringing in. Every part that is a package of cutienator is brought
   in, each in a process of its own, so that a part that crashes costs
   only itself; then every name its '__all__' lists, and every name of
   each of its namespaces, as 'from cutienator.QtCore import QObject'
   would. That runs no ritual, so it needs no target file. A name that
   cannot be brought in is listed with what was raised.
2. Objects. A QObject with a parent and an object name, a QSize, a
   QPoint and a QTimer of QtCore, then a QApplication with a QWidget and
   a QPushButton of QtWidgets, each step compared with what Qt gives.
   That needs the target files of QtCore, QtGui and QtWidgets. Qt draws
   off screen, as 'QT_QPA_PLATFORM=offscreen' says.

It writes what it found to REPORT_FILE and prints it, and ends with code
0 once both checks have run, whatever they found: the verdict says OK,
GAPS when something raised NotImplementedError, a gap of this machine
said where it is used, or FAILED when something raised anything else or
gave another answer than Qt's. Only a check that cannot run at all ends
otherwise, with what Python raised.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, Dict, List, Tuple

#  Stands for any answer: the step only has to give one.
ANY = object()

#  Brings in one part and every name it lists, in a process of its own,
#  and prints what it brought in and what it could not, as JSON.
ONE_PART = r'''
import importlib, json, sys, types
part = sys.argv[1]
out = dict(part=part, brought=0, failed={})
def walk(module, dotted):
  for name in getattr(module, '__all__', ()):
    try:
      value = getattr(module, name)
    except BaseException as exception:
      out['failed']['%s.%s' % (dotted, name)] = '%s: %s' % (
          type(exception).__name__, ' '.join(str(exception).split())[:300])
      continue
    out['brought'] += 1
    if isinstance(value, types.ModuleType):
      walk(value, '%s.%s' % (dotted, name))
try:
  walk(importlib.import_module('cutienator.%s' % part), part)
except BaseException as exception:
  out['failed'][part] = '%s: %s' % (
      type(exception).__name__, ' '.join(str(exception).split())[:300])
print(json.dumps(out))
'''


def findParts() -> List[str]:
  """Gives every part that is a package of cutienator, by name."""
  import cutienator
  folder = os.path.dirname(os.path.abspath(cutienator.__file__))
  return sorted(
      name for name in os.listdir(folder)
      if name.startswith('Qt') and os.path.isfile(
          os.path.join(folder, name, '__init__.py')))


def bringIn(partName: str) -> Dict[str, Any]:
  """Brings in one part and every name it lists, in a process of its
  own; gives what it brought in and what it could not."""
  try:
    done = subprocess.run(
        [sys.executable, '-B', '-c', ONE_PART, partName],
        capture_output=True, text=True, timeout=1200)
  except subprocess.TimeoutExpired:
    return dict(part=partName, brought=0, failed={
        partName: 'TimeoutExpired: it did not end within 1200 seconds'})
  lines = done.stdout.strip().splitlines()
  if done.returncode or not lines:
    said = ' '.join(done.stderr.split())[-300:]
    return dict(part=partName, brought=0, failed={
        partName: 'the process ended with %s: %s' % (
            done.returncode, said)})
  return json.loads(lines[-1])


def checkBringingIn() -> Tuple[List[str], int, int]:
  """Brings in every part; gives the lines of the report, how many names
  could not be brought in for a gap, and how many for anything else."""
  parts = findParts()
  with ThreadPoolExecutor(os.cpu_count() or 1) as pool:
    results = [*pool.map(bringIn, parts)]
  failed = [
      (name, said) for result in results
      for name, said in sorted(result['failed'].items())]
  gaps = sum(1 for _, said in failed
             if said.startswith('NotImplementedError'))
  lines = [
      'BRINGING IN',
      'parts: %d, every one a package of cutienator' % len(parts),
      'names brought in: %d' % sum(r['brought'] for r in results),
      'names not brought in: %d (%d of them gaps)' % (len(failed), gaps),
      'parts that did not import: %s' % (' '.join(
          r['part'] for r in results if r['part'] in r['failed'])
          or 'none'),
  ]
  lines.extend('  %s: %s' % pair for pair in failed)
  return lines, gaps, len(failed) - gaps


def checkObjects() -> Tuple[List[str], int, int]:
  """Makes a few objects and uses them; gives the lines of the report,
  how many steps raised NotImplementedError, and how many went wrong
  otherwise."""
  lines, gaps, wrong = ['OBJECTS'], 0, 0

  def step(said: str, function: Callable, expected: Any) -> Any:
    nonlocal gaps, wrong
    try:
      given = function()
    except NotImplementedError as gap:
      gaps += 1
      lines.append('GAP     %s: %s' % (said, ' '.join(str(gap).split())))
      return None
    except BaseException as exception:
      wrong += 1
      lines.append('RAISED  %s: %s: %s' % (
          said, type(exception).__name__,
          ' '.join(str(exception).split())[:300]))
      return None
    if expected is not ANY and given != expected:
      wrong += 1
      lines.append('WRONG   %s gave %r, Qt gives %r' % (
          said, given, expected))
    else:
      lines.append('ok      %s: %r' % (said, given))
    return given

  try:
    from cutienator.QtCore import QObject, QPoint, QSize, QTimer
  except BaseException as exception:
    lines.append('RAISED  bringing in QtCore: %s: %s' % (
        type(exception).__name__, exception))
    return lines, gaps, wrong + 1
  mother = step('QObject()', QObject, ANY)
  child = step('QObject()', QObject, ANY)
  if mother is not None and child is not None:
    step('child.parent()', child.parent, None)
    step('child.setParent(mother)', lambda: child.setParent(mother), None)
    step('child.parent() is mother', lambda: child.parent() is mother,
         True)
    step('len(mother.children())', lambda: len([*mother.children()]), 1)
    step("child.setObjectName('kid')",
         lambda: child.setObjectName('kid'), None)
    step('child.objectName()', child.objectName, 'kid')
  size = step('QSize(3, 4)', lambda: QSize(3, 4), ANY)
  if size is not None:
    step('size.width(), size.height()',
         lambda: (size.width(), size.height()), (3, 4))
    step('size.transposed().width()', lambda: size.transposed().width(),
         4)
  point = step('QPoint(5, 7)', lambda: QPoint(5, 7), ANY)
  if point is not None:
    step('point.manhattanLength()', point.manhattanLength, 12)
  timer = step('QTimer()', QTimer, ANY)
  if timer is not None:
    step('timer.setInterval(250)', lambda: timer.setInterval(250), None)
    step('timer.interval()', timer.interval, 250)
  try:
    from cutienator.QtWidgets import QApplication, QPushButton, QWidget
  except BaseException as exception:
    wrong += 1
    lines.append('RAISED  bringing in QtWidgets: %s: %s' % (
        type(exception).__name__, exception))
    return lines, gaps, wrong
  application = step(
      "QApplication(['check_cute'])",
      lambda: QApplication(['check_cute']), ANY)
  if application is None:
    return lines, gaps, wrong
  window = step('QWidget()', QWidget, ANY)
  if window is not None:
    step('window.resize(320, 200)', lambda: window.resize(320, 200), None)
    step('window.width(), window.height()',
         lambda: (window.width(), window.height()), (320, 200))
    button = step("QPushButton('Press', window)",
                  lambda: QPushButton('Press', window), ANY)
    if button is not None:
      step('button.text()', button.text, 'Press')
      step('button.parent() is window', lambda: button.parent() is window,
           True)
    step("window.setWindowTitle('cutienator')",
         lambda: window.setWindowTitle('cutienator'), None)
    step('window.windowTitle()', window.windowTitle, 'cutienator')
  return lines, gaps, wrong



def main(reportFile: str) -> int:
  """Runs both checks, writes the report and prints it; gives 0."""
  began = time.time()
  head = [
      'system: %s %s, %s' % (
          platform.system(), platform.release(), platform.machine()),
      'Python: %s' % platform.python_version(),
      'drawing: %s' % os.environ.get('QT_QPA_PLATFORM', 'the default'),
  ]
  broughtLines, broughtGaps, broughtWrong = checkBringingIn()
  objectLines, objectGaps, objectWrong = checkObjects()
  if broughtWrong or objectWrong:
    verdict = 'FAILED'
  elif broughtGaps or objectGaps:
    verdict = 'GAPS'
  else:
    verdict = 'OK'
  lines = [
      *head, *broughtLines, *objectLines,
      'seconds: %.0f' % (time.time() - began), 'verdict: %s' % verdict,
  ]
  folder = os.path.dirname(os.path.abspath(reportFile))
  os.makedirs(folder, exist_ok=True)
  with open(reportFile, 'w') as file:
    file.write('\n'.join(lines) + '\n')
  print('\n'.join(lines), flush=True)
  return 0


if __name__ == '__main__':
  sys.exit(main(*sys.argv[1:2]))
