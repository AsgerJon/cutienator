"""
Builds the target file of every part of Qt on the machine it runs on, as
'Rituals.summon()' does, and says EVERYTHING the compiler and the linker
refused on the way.

  PYTHONPATH=src python bin/check_summon.py REPORT_FILE

Each part is built by its own 'Summon', as 'summon' builds it: what the
compiler or the linker refuses is left out, the ritual alone where it
can be, and every other ritual is built; see 'Exorcist'. The report
names, for each ritual file, what was left out and what the compiler or
the linker said of it, so all of it can be mended at once, and the
target files are there to be tried. The workflow 'four-horsemen' runs it
on GitHub's machines of all four systems: Linux, Windows, Apple silicon
Mac and Intel Mac.

It writes what it found to REPORT_FILE and prints it, and ends with
code 0 when nothing was refused, else with 1. As it works it prints a
line of progress at most every half minute, and one as each part
begins: a bar, how many of all the ritual files are compiled, the part
it is at, the time gone and the time it should still take at the pace
so far, as

  PROGRESS  34% [######..............] 3270 of 9609 ritual files,
  QtGui, 12m03s gone, about 23m20s left

on one line. Run it with 'python -u', so that each line shows at once.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import platform
import subprocess
import sys
import time
from typing import TYPE_CHECKING

from cutienator.occult import Summon, Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional


#  How far the check is; see 'sayProgress'. A line is printed at most
#  every '_EVERY' seconds, unless it is asked for.
_EVERY = 30.0
_PROGRESS = dict(total=0, done=0, began=0.0, said=0.0)


def showTime(seconds: float) -> str:
  """Gives a time as minutes and seconds, as '12m03s'."""
  minutes, seconds = divmod(int(seconds), 60)
  return '%dm%02ds' % (minutes, seconds)


def sayProgress(step: str, done: int = 0, force: bool = False) -> None:
  """
  Counts 'done' more ritual files compiled and, when half a minute has
  gone since the last line or 'force' is given, prints one line: a bar,
  how many of all the ritual files are compiled, the step, the time
  gone, and the time it should still take at the pace so far.
  """
  _PROGRESS['done'] += done
  now = time.time()
  if not force and now - _PROGRESS['said'] < _EVERY:
    return
  _PROGRESS['said'] = now
  total, count = _PROGRESS['total'], _PROGRESS['done']
  gone = now - _PROGRESS['began']
  share = count / total if total else 1.0
  bar = ('#' * int(20 * share)).ljust(20, '.')
  if count and count < total:
    left = ', about %s left' % showTime(gone * (total - count) / count)
  else:
    left = ''
  print('PROGRESS %3d%% [%s] %d of %d ritual files, %s, %s gone%s' % (
      100 * share, bar, count, total, step, showTime(gone), left),
      flush=True)


def describeMachine(build: Summon) -> List[str]:
  """Says which system, processor, Qt and compiler the check ran with."""
  compiler = subprocess.run(
      ('clang++', '--version'), stdout=subprocess.PIPE,
      stderr=subprocess.PIPE, universal_newlines=True).stdout
  return [
      'system: %s %s, %s' % (
          platform.system(), platform.release(), platform.machine()),
      'Qt: %s' % build.getQtVersion(),
      'compiler: %s' % (compiler.split('\n')[0] or 'unknown'),
      'Python: %s' % platform.python_version(),
  ]


def buildPart(partName: str, build: Summon) -> List[str]:
  """
  Builds the target file of one part as 'Summon.run' does, each ritual
  file compiled counting for the progress as it is done, and gives the
  lines of the report for what was left out.
  """
  compileOne = build._compile

  def compileCounted(ritualFile: str) -> Optional[str]:
    try:
      return compileOne(ritualFile)
    finally:
      sayProgress(partName, 1)

  #  'run' compiles through the method of the object, so the counting
  #  one stands in for it here.
  build._compile = compileCounted
  sayProgress('%s, %d ritual files' % (
      partName, len(build.getRitualFiles())), force=True)
  lines = []
  try:
    build.run()
  except RuntimeError as runtimeError:
    lines.append('the target file of %s was not built:' % partName)
    lines.append('  %s' % ' '.join(str(runtimeError).split())[-20000:])
  record = build.getRecord()
  if record['common header'] is not None:
    lines.append('the common header of %s was refused, and every ritual '
                 'file compiled without it:' % partName)
    lines.append('  %s' % ' '.join(record['common header'].split())[-3000:])
  for key, entry in sorted(record['ritual files'].items()):
    lines.extend(describeLeftOut(key, entry))
  return lines


def describeLeftOut(key: str, entry: Dict[str, Any]) -> List[str]:
  """Gives the lines of the report for one ritual file something of
  which was left out: its name, each item dropped with what the
  compiler or the linker said, and each ritual left out."""
  lines = ['  %s' % key]
  if entry.get('whole'):
    whole = ' '.join(entry['whole'].split())
    lines.append('    WHOLE FILE: %s' % whole[:300])
  for kind, name, first, last, reason in entry.get('dropped', ()):
    lines.append('    dropped %s %s (lines %d-%d): %s' % (
        kind, name[:80], first, last, ' '.join(reason.split())[:300]))
  for name, (function, reason) in sorted(entry.get('leftOut', {}).items()):
    lines.append('    left out: %s' % function[:160])
  return lines


def main(reportFile: str) -> int:
  """
  Runs the check and writes the report.

  Parameters
  ----------

  reportFile : str
    Where the report is written. Its folder has to exist.

  Returns
  -------

  int
    The exit code: 0 when every ritual file compiled and no link
    missed anything, else 1.
  """
  partNames = Rituals.getBuiltParts()
  builds = [Rituals.createPartSummon(partName) for partName in partNames]
  began = time.time()
  lines = [*describeMachine(builds[0])]
  _PROGRESS.update(
      total=sum(len(build.getRitualFiles()) for build in builds),
      began=began)
  sayProgress('%d parts of Qt' % len(builds), force=True)
  found = []
  for partName, build in zip(partNames, builds):
    found.extend(buildPart(partName, build))
  sayProgress('done', force=True)
  ritualCount = sum(len(build.getRitualFiles()) for build in builds)
  records = [build.getRecord()['ritual files'] for build in builds]
  touched = sum(len(record) for record in records)
  leftOut = sum(len(build.getLeftOut()) for build in builds)
  built = sum(os.path.isfile(build.getTargetFile()) for build in builds)
  lines.append('target files: %d of %d built, ritual files: %d, with '
               'something left out: %d, rituals left out: %d' % (
                   built, len(builds), ritualCount, touched, leftOut))
  lines.extend(found)
  verdict = 1 if found else 0
  lines.append('seconds: %d' % (time.time() - began))
  lines.append('verdict: %s' % ('REFUSED' if verdict else 'OK'))
  text = '%s\n' % '\n'.join(lines)
  with open(reportFile, 'w') as file:
    file.write(text)
  print(text)
  return verdict


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print(__doc__.strip(), file=sys.stderr)
    sys.exit(2)
  sys.exit(main(sys.argv[1]))
