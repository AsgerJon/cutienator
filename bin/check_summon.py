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
code 0 when nothing was refused, else with 1.
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
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from cutienator.occult import Summon, Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import List


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


def compileAll(build: Summon) -> List[str]:
  """
  Compiles every ritual file, each to its object file, and gives what
  the compiler said of each one it refused. The precompiled header is
  made first and removed after, as 'Summon.run' does.
  """
  ritualFiles = build.getRitualFiles()
  for ritualFile in ritualFiles:
    folder = os.path.dirname(build.getObjectFile(ritualFile))
    os.makedirs(folder, exist_ok=True)
  build._precompile()
  try:
    with ThreadPoolExecutor(max_workers=build.getJobCount()) as pool:
      said = [*pool.map(build._compile, ritualFiles)]
  finally:
    if os.path.isfile(build.getPrecompiledHeaderFile()):
      os.remove(build.getPrecompiledHeaderFile())
  return [refusal for refusal in said if refusal]


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
  builds = [
      Rituals.createPartSummon(partName)
      for partName in Rituals.getBuiltParts()]
  began = time.time()
  lines = [*describeMachine(builds[0])]
  ritualCount, refusals, verdict = 0, [], 0
  for build in builds:
    ritualCount += len(build.getRitualFiles())
    try:
      refusals.extend(compileAll(build))
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
  if not verdict:
    for build in builds:
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
