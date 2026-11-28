"""
Keeps the release workflows from compiling the same target files on
every machine. One machine of each system builds the target files of
the parts named, and every other machine of that system gets them
instead of compiling; this script says what they are made of, and
proves afterwards that a machine which got them compiled nothing.

  PYTHONPATH=src python bin/check_libraries.py key PART ...
  PYTHONPATH=src python bin/check_libraries.py seal RECORD PART ...
  PYTHONPATH=src python bin/check_libraries.py check RECORD PART ...

'key' prints one line, 'key=' and a SHA-256, for '$GITHUB_OUTPUT': the
name the kept target files are kept under. It is made of what 'Summon'
itself checks before it compiles again, for each part: the version of
Qt and the commands 'clang++' is told, as 'Summon.getToldText' gives
them; and besides those what 'Summon' judges by the time of a file,
which says nothing on a machine of GitHub, where every file is as new
as the checkout: the text of every ritual file and sigil file of the
parts, and the text of the files of 'cutienator.occult' that decide how
they are built. And 'clang++ --version', since the commands do not say
which 'clang++' runs them. When any of it changes, the key changes, and
the target files are built again.

'seal' runs on a machine that got the target files, before the tests:
it stops, naming the part, when a target file is missing, and writes
RECORD, the SHA-256 of each. It does not judge them by their time: a
file taken from a run before keeps the time it was kept at, older than
the checkout, and the key it was kept under already says it is made of
these very ritual files.

'check' runs after the tests: it stops when a target file is not what
RECORD says, or when an object file of the parts was made. 'Summon'
makes one for each ritual file it compiles, in the folder 'demons'
beside the target files, which no machine that got them has. When
neither happened, it says that nothing was compiled here.

Each ends with code 0 when what it checks holds, and 1 when it does
not, saying why.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import glob
import hashlib
import json
import os
import subprocess
import sys
from typing import TYPE_CHECKING

from cutienator import occult
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List


def hashFile(path: str) -> str:
  """Gives the SHA-256 of a file."""
  digest = hashlib.sha256()
  with open(path, 'rb') as file:
    for block in iter(lambda: file.read(1 << 20), b''):
      digest.update(block)
  return digest.hexdigest()


def findKey(partNames: List[str]) -> str:
  """Gives the SHA-256 of what the target files of the parts are made
  of; see the docstring of the module."""
  digest = hashlib.sha256()
  version = subprocess.run(
      ('clang++', '--version'), capture_output=True, text=True)
  digest.update(version.stdout.replace('\r', '').encode())
  occultFolder = os.path.dirname(os.path.abspath(occult.__file__))
  for path in sorted(glob.glob(os.path.join(occultFolder, '*.py'))):
    digest.update(os.path.basename(path).encode())
    digest.update(hashFile(path).encode())
  for partName in partNames:
    told = Rituals.createPartSummon(partName).getToldText()
    digest.update(partName.encode())
    digest.update(told.replace('\r', '').encode())
    for path in Rituals.getPartRitualFiles(partName):
      for one in (path, '%s.json' % os.path.splitext(path)[0]):
        if os.path.isfile(one):
          digest.update(os.path.basename(one).encode())
          digest.update(hashFile(one).encode())
  return digest.hexdigest()


def seal(record: str, partNames: List[str]) -> int:
  """Checks that each target file is there, and writes the SHA-256 of
  each to RECORD."""
  hashes = dict()  # type: Dict[str, str]
  for partName in partNames:
    target = Rituals.getTargetFile(partName)
    if not os.path.isfile(target):
      print('The target file of %s is missing: %s' % (partName, target))
      return 1
    hashes[target] = hashFile(target)
    print('got %s: %s' % (partName, os.path.basename(target)))
  with open(record, 'w') as file:
    json.dump(hashes, file, indent=1)
  return 0


def check(record: str, partNames: List[str]) -> int:
  """Checks that the target files are what RECORD says, and that no
  object file of the parts was made."""
  with open(record) as file:
    hashes = json.load(file)
  wrong = 0
  for target, sealed in sorted(hashes.items()):
    if not os.path.isfile(target) or hashFile(target) != sealed:
      print('The target file %s changed during the tests.' % target)
      wrong += 1
  folders = sorted({
      Rituals.createPartSummon(partName).getObjectFolder()
      for partName in partNames})
  for folder in folders:
    made = glob.glob(os.path.join(folder, '**', '*.o'), recursive=True)
    if made:
      print('%d object files were made in %s, as %s.' % (
          len(made), folder, made[0]))
      wrong += 1
  if wrong:
    return 1
  print('Nothing was compiled here: the target files of %s are the ones '
        'this machine got, and no object file was made.' % (
            ', '.join(partNames)))
  return 0


def main(*args: str) -> int:
  """Runs one of 'key', 'seal' and 'check'."""
  if args[:1] == ('key',) and len(args) > 1:
    print('key=%s' % findKey([*args[1:]]))
    return 0
  if args[:1] in (('seal',), ('check',)) and len(args) > 2:
    run = seal if args[0] == 'seal' else check
    return run(args[1], [*args[2:]])
  print(__doc__)
  return 1


if __name__ == '__main__':
  sys.exit(main(*sys.argv[1:]))
