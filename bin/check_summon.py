"""
Compiles every ritual file and joins those of each part of Qt into
its target file, on the machine it runs on, and says EVERYTHING the
compiler and the linker refuse.

  PYTHONPATH=src python bin/check_summon.py REPORT_FILE

'Rituals.summon()' does the same work and stops at the first refusal,
which is right for a user. This is for looking ahead: one run names
every ritual file that does not compile on this system and every
function the link misses, so all of it can be mended at once. The
workflow 'four-horsemen' runs it on GitHub's machines of all four
systems: Linux, Windows, Apple silicon Mac and Intel Mac.

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
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TYPE_CHECKING

from cutienator.occult import Summon, Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import List


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


def compileAll(partName: str, build: Summon) -> List[str]:
  """
  Compiles every ritual file of one part, each to its object file, and
  gives what the compiler said of each one it refused, in the order of
  the ritual files. The precompiled header is made first and removed
  after, as 'Summon.run' does. Each file compiled counts for the
  progress, as it is done.
  """
  ritualFiles = build.getRitualFiles()
  for ritualFile in ritualFiles:
    folder = os.path.dirname(build.getObjectFile(ritualFile))
    os.makedirs(folder, exist_ok=True)
  sayProgress('%s, %d ritual files, precompiled header' % (
      partName, len(ritualFiles)), force=True)
  build._precompile()
  said = dict()  # type: dict
  try:
    with ThreadPoolExecutor(max_workers=build.getJobCount()) as pool:
      futures = {
          pool.submit(build._compile, ritualFile): ritualFile
          for ritualFile in ritualFiles}
      for future in as_completed(futures):
        said[futures[future]] = future.result()
        sayProgress(partName, 1)
  finally:
    if os.path.isfile(build.getPrecompiledHeaderFile()):
      os.remove(build.getPrecompiledHeaderFile())
  return [said[f] for f in ritualFiles if said.get(f)]


def describeRefusal(refusal: str) -> List[str]:
  """Gives the lines of the report for one ritual file the compiler
  refused: its name, and the first errors the compiler named."""
  name = os.path.basename(refusal.split(': ')[0])
  #  Each error as the compiler writes it, from the name of the file
  #  on, without the folders in front: 'q_size.cpp:12:3: error: ...'.
  errors = re.findall(
      r'([^\s/]+:\d+:\d+: (?:fatal )?error: [^\n]*)', refusal)
  lines = ['  %s' % name]
  for error in errors[:3]:
    lines.append('    %s' % error.strip()[:200])
  if not errors:
    lines.append('    %s' % ' '.join(refusal.split())[-200:])
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
  ritualCount, refusals, verdict = 0, [], 0
  _PROGRESS.update(
      total=sum(len(build.getRitualFiles()) for build in builds),
      began=began)
  sayProgress('%d parts of Qt' % len(builds), force=True)
  for partName, build in zip(partNames, builds):
    ritualCount += len(build.getRitualFiles())
    try:
      refusals.extend(compileAll(partName, build))
    except RuntimeError as runtimeError:
      #  The common header itself was refused: no ritual file of the
      #  part was tried.
      lines.append('the precompiled header of %s was refused:' % (
          os.path.basename(build.getTargetFile())))
      lines.append('  %s' % str(runtimeError)[-3000:])
      verdict = 1
  lines.append('target files: %d, ritual files: %d, refused by the '
               'compiler: %d' % (len(builds), ritualCount, len(refusals)))
  for refusal in refusals:
    lines.extend(describeRefusal(refusal))
  if refusals:
    verdict = 1
  sayProgress('compiled', force=True)
  if not verdict:
    for partName, build in zip(partNames, builds):
      sayProgress('linking %s' % partName)
      try:
        build._run(*build.getLinkCommand())
      except RuntimeError as runtimeError:
        #  The linker names every function it misses, and who asks for
        #  it. Its words are kept as they are.
        lines.append('the link of %s was refused:' % build.getTargetFile())
        lines.append(str(runtimeError)[-20000:])
        verdict = 1
    if not verdict:
      lines.append('the links missed nothing: %d target files beside %s' % (
          len(builds), os.path.dirname(builds[0].getTargetFile())))
  sayProgress('done', force=True)
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
