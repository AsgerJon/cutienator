"""Reads the header files of parts of Qt and says what each part gave."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from . import QtPart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple


def readPart(workFolder: str, partName: str) -> str:
  """
  Reads one part of Qt into the work folder and gives a summary.

  Parameters
  ----------

  workFolder : str
    The path of an existing folder to keep the reading in.

  partName : str
    The part of Qt, as 'QtCore'.

  Returns
  -------

  str
    A few lines: how many header files the part has, how many hold
    records and how many records, and each header file that was not
    read with what the compiler said of it.
  """
  qtPart = QtPart()
  qtPart.setPartName(partName)
  qtPart.setWorkFolder(workFolder)
  qtPart.read()
  stamp = qtPart.getStamp()
  headerFiles = qtPart.getHeaderFiles()
  holding = [h for h in headerFiles if h.getRecordCount()]
  unread = [h for h in headerFiles if not h.wasRead()]
  empty = len(headerFiles) - len(holding) - len(unread)
  infoSpec = """%s, read from Qt %s in %d seconds"""
  lines = [infoSpec % (partName, stamp['qtVersion'], stamp['seconds'])]
  infoSpec = """  %d header files: %d hold %d records, %d hold only
  macros and includes, %d were not read"""
  info = infoSpec % (
      len(headerFiles), len(holding), stamp['keptRecords'], empty,
      len(unread),
  )
  lines.append('  %s' % ' '.join(info.split()))
  for headerFile in unread:
    said = headerFile.getComplaint().splitlines()
    errors = [line for line in said if 'error' in line] or said
    infoSpec = """  not read: %s"""
    lines.append(infoSpec % headerFile.getHeaderPath())
    lines.append('    %s' % errors[0].strip())
  lines.append('  kept in %s' % qtPart.getReadingFolder())
  return '\n'.join(lines)


def readInChild(arguments: Tuple[str, str]) -> Tuple[int, str]:
  """
  Reads one part of Qt in a Python of its own, so that several parts
  can be read at the same time.

  Parameters
  ----------

  arguments : Tuple[str, str]
    The work folder and the part of Qt.

  Returns
  -------

  Tuple[int, str]
    The exit code of that Python, and all it printed.
  """
  command = (sys.executable, '-m', 'dev_tooling', *arguments)
  done = subprocess.run(command, capture_output=True, text=True)
  return done.returncode, '%s%s' % (done.stdout, done.stderr)


def main(*arguments: str) -> int:
  """
  Reads each named part of Qt into the work folder and prints what it
  gave. Several parts are read at the same time.

  Parameters
  ----------

  *arguments : str
    The work folder, then the name of each part of Qt to read.

  Returns
  -------

  int
    The exit code: 0 when every part was read, 1 otherwise.
  """
  if len(arguments) < 2:
    print('usage: python -m dev_tooling WORK_FOLDER PART [PART ...]')
    print('  as:  python -m dev_tooling /some/folder QtCore QtGui QtWidgets')
    return 1
  workFolder, partNames = arguments[0], arguments[1:]
  if len(partNames) == 1:
    print(readPart(workFolder, partNames[0]))
    return 0
  jobs = [(workFolder, partName) for partName in partNames]
  with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
    results = (*pool.map(readInChild, jobs),)
  for _, printed in results:
    print(printed.rstrip())
  return 1 if any(code for code, _ in results) else 0


if __name__ == '__main__':
  sys.exit(main(*sys.argv[1:]))
