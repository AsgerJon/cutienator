"""
Writes, on the system it runs on, the rituals of the classes of that
system alone: those declared in the header files of Qt's source that
the reader refused on Linux, as 'bin/dev_tooling/refused_on_linux.txt'
lists them, and reads here. On macOS those of macOS, on Windows those
of Windows. The workflow 'system-rituals' runs it on GitHub's machines.

  PYTHONPATH=bin:src python bin/system_rituals.py QTBASE WORK INSTALLED OUT

QTBASE     the folder 'qtbase' of Qt's source, with the others beside it
WORK       a folder for the header folder and the readings
INSTALLED  the installed Qt each ritual file is tested against
OUT        where the ritual file and the rows file of each class that
           passed are written, in the folder of its part, as
           'QtCoreRituals', the way the package keeps them

Step by step, as gcloud's steps 1, 3 and 2 do for Linux:
1. 'HeaderFolder' makes the folder of header files from the source.
2. 'HeaderReader' reads each part with a header file of the list, and
   every part such a part needs.
3. Of the header files of the list, those read here give the classes:
   each class the tree finds declared in one, and not in the package.
4. 'RitualGenerator' writes the ritual file of each, 'RitualTester'
   tests it against the installed Qt. Only those that pass stay in OUT.

It writes 'report.txt' into OUT and ends with 0 when it ran through,
also when no class passed; with 1 when something raised.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import multiprocessing
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from typing import TYPE_CHECKING

from dev_tooling import (DependencyTree, HeaderFolder, HeaderReader,
                         Machine, RitualGenerator, RitualTester,
                         SourceReader)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List, Set, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
REFUSED_FILE = os.path.join(HERE, 'dev_tooling', 'refused_on_linux.txt')
UNCOVERED_FILE = os.path.join(HERE, 'dev_tooling', 'uncovered_names.txt')
PACKAGE = os.path.join(
    os.path.dirname(HERE), 'src', 'cutienator', 'occult', 'rituals')


def say(step: str, done: int, total: int, since: float) -> None:
  """One line of progress: the step, done of total, seconds gone."""
  print('PROGRESS %s %d %d %d' % (step, done, total, time.time() - since),
        flush=True)


def readRefused() -> Set[Tuple[str, str]]:
  """Gives each part and header file the list names."""
  found = set()  # type: Set[Tuple[str, str]]
  with open(REFUSED_FILE, encoding='utf-8') as file:
    for line in file:
      words = line.split()
      if line.startswith('#') or len(words) < 2:
        continue
      found.add((words[0], words[1]))
  return found


def makePart(partName: str, readings: str) -> HeaderReader:
  """Gives the 'HeaderReader' of one part, as gcloud's steps set it."""
  part = HeaderReader()
  part.setPartName(partName)
  part.setPrivate(True)
  part.setWorkFolder(readings)
  return part


def makeFolder(qtbase: str, work: str) -> HeaderFolder:
  """Gives the 'HeaderFolder' of the source in the work folder, and
  tells 'HeaderReader' of it, and of the list of names no class
  covers."""
  folder = HeaderFolder()
  folder.setSourceFolder(qtbase)
  folder.setFolder(os.path.join(work, 'headers'))
  HeaderReader.setHeaderFolder(folder)
  HeaderReader.setUncoveredFile(UNCOVERED_FILE)
  return folder


def readPart(partName: str, qtbase: str, work: str) -> str:
  """Reads one part; gives '' or what was raised. It runs in a process
  of its own, which on Windows starts from nothing, so it tells
  'HeaderReader' of the folder itself."""
  try:
    makeFolder(qtbase, work)
    makePart(partName, os.path.join(work, 'readings')).read()
    return ''
  except Exception as exception:
    return '%s: %s' % (type(exception).__name__, exception)


def getContext() -> multiprocessing.context.BaseContext:
  """Gives how processes are made: by 'spawn', each one starting from
  nothing, as Windows has no other way, and as Python makes them on
  macOS anyway."""
  return multiprocessing.get_context('spawn')


def main(qtbase: str, work: str, installed: str, out: str) -> int:
  """Runs the four steps and writes the report. See the docstring of
  this file."""
  began = time.time()
  readings = os.path.join(work, 'readings')
  os.makedirs(readings, exist_ok=True)
  os.makedirs(out, exist_ok=True)
  lines = [
      'system: %s, as %s' % (
          Machine.getSystemName(), Machine.getSpecName()),
  ]
  #  1. The folder of header files.
  tic = time.time()
  say('folder', 0, 1, tic)
  folder = makeFolder(qtbase, work)
  if not folder.isMade():
    folder.make()
  say('folder', 1, 1, tic)
  #  2. The parts with a header file of the list, and those they need.
  refused = readRefused()
  partNames = folder.getPartNames()
  wanted = []  # type: List[str]
  for partName in sorted({part for part, _ in refused}):
    if partName not in partNames:
      continue
    for need in HeaderReader.getNeededParts(partName):
      if need in partNames and need not in wanted:
        wanted.append(need)
  tic = time.time()
  say('reading', 0, len(wanted), tic)
  raised = dict()  # type: Dict[str, str]
  #  Two at a time: QtCore and QtGui each take some GB while read.
  with ProcessPoolExecutor(2, mp_context=getContext()) as pool:
    jobs = [pool.submit(readPart, name, qtbase, work) for name in wanted]
    for done, (name, job) in enumerate(zip(wanted, jobs), 1):
      said = job.result()
      if said:
        raised[name] = said
      say('reading', done, len(wanted), tic)
  lines.append('parts read: %d, raising: %d' % (
      len(wanted) - len(raised), len(raised)))
  for name, said in sorted(raised.items()):
    lines.append('RAISED %s: %s' % (name, ' '.join(said.split())[:600]))
  #  3. The header files of the list read here, and their classes.
  readHere = set()  # type: Set[Tuple[str, str]]
  for partName in wanted:
    if partName in raised:
      continue
    stampFile = os.path.join(readings, partName, 'reading.json')
    with open(stampFile, encoding='utf-8') as file:
      entries = json.load(file)['headerFiles']
    for name, entry in entries.items():
      if (partName, name) in refused and entry['read']:
        readHere.add((partName, name))
  lines.append('header files of the list read here: %d of %d' % (
      len(readHere), len(refused)))
  parts = [makePart(name, readings) for name in wanted if name not in raised]
  tree = DependencyTree()
  tree.setHeaderReaders(*parts)
  source = SourceReader()
  source.setSourceFolder(qtbase)
  source.setHeaderReaders(*parts)
  tree.setSourceReader(source)
  candidates = []  # type: List[Tuple[str, str]]
  inPackage = []  # type: List[Tuple[str, str]]
  for partName, className in tree.getMakeOrder():
    headerPath = tree.getHeaderPath(className, partName)
    generator = RitualGenerator()
    generator.setDependencyTree(tree)
    generator.setPartName(partName)
    generator.setClassName(className)
    stem = generator.getFileStem()
    packaged = os.path.isfile(os.path.join(
        PACKAGE, '%sRituals' % partName, '%s.cpp' % stem))
    if packaged:
      inPackage.append((partName, className))
    elif (partName, os.path.basename(headerPath)) in readHere:
      candidates.append((partName, className))
  lines.append('classes of those header files, not in the package: %d' % (
      len(candidates)))
  #  A class has a cute class when the package has one for it: a value
  #  class is passed only then, as on gcloud.
  tree.setCuteNames(*inPackage, *candidates)
  RitualTester.setInstalledFolder(installed)
  #  4. Write and test each, one after the other.
  tic = time.time()
  say('rituals', 0, len(candidates), tic)
  passed = 0
  for done, (partName, className) in enumerate(candidates, 1):
    target = os.path.join(out, '%sRituals' % partName)
    os.makedirs(target, exist_ok=True)
    try:
      generator = RitualGenerator()
      generator.setDependencyTree(tree)
      generator.setPartName(partName)
      generator.setClassName(className)
      generator.setWorkFolder(target)
      generator.write()
      tester = RitualTester()
      tester.setRitualGenerator(generator)
      faults = tester.test()
    except Exception as exception:
      faults = ['%s: %s' % (type(exception).__name__, exception)]
      generator = None
    if faults:
      lines.append('FAILED %s/%s: %s' % (
          partName, className, ' '.join(faults[0].split())[:600]))
    else:
      passed += 1
      lines.append('PASSED %s/%s' % (partName, className))
    #  Only the ritual file and the rows file of a class that passed
    #  stay; what the tester built beside them goes.
    if generator is not None:
      stem = generator.getFileStem()
      for name in os.listdir(target):
        keep = not faults and name in ('%s.cpp' % stem, '%s.json' % stem)
        if name.startswith((stem + '.', 'lib' + stem + '.')) and not keep:
          os.remove(os.path.join(target, name))
    say('rituals', done, len(candidates), tic)
  lines.insert(1, 'passed: %d of %d' % (passed, len(candidates)))
  lines.append('seconds: %d' % (time.time() - began))
  text = '%s\n' % '\n'.join(lines)
  with open(os.path.join(out, 'report.txt'), 'w', encoding='utf-8') as file:
    file.write(text)
  print(text, flush=True)
  return 1 if raised else 0


if __name__ == '__main__':
  if len(sys.argv) != 5:
    print(__doc__.strip(), file=sys.stderr)
    sys.exit(2)
  sys.exit(main(*sys.argv[1:5]))
