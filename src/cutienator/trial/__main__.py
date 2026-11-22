"""Builds what is stale, hears every trial, and prints the verdicts."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import sys
import tempfile

from ..occult import Rituals
from . import Judge, qObjectTrials


def main() -> int:
  """
  Runs the three checks and prints what each found.

  Built correctly: the rituals listed for Python are the ones the shared
  object offers. Functions correctly and is as in C++: every trial is
  heard, and its verdict printed.

  Returns
  -------

  int
    The exit code: 0 when nothing is at fault, 1 otherwise.
  """
  if Rituals.isStale():
    print('Building %s' % Rituals.getTargetFile())
    Rituals.build()

  judge = Judge()
  workFolder = tempfile.mkdtemp(prefix='cutienator-trial-')
  judge.setWorkFolder(workFolder)

  print('BUILT CORRECTLY')
  faults = judge.findRitualFaults()
  for fault in faults:
    print('  %s' % fault)
  if not faults:
    infoSpec = """  all %d listed rituals are offered by the shared object,
    and it offers no others of its own"""
    count = len(Rituals.getRitualNames())
    print('  %s' % ' '.join((infoSpec % count).split()))

  print('FUNCTIONS CORRECTLY, AND IS AS IN C++')
  verdicts = judge.hearAll(*qObjectTrials())
  for verdict in verdicts:
    print(verdict)

  failed = [verdict for verdict in verdicts if not verdict.passed()]
  print('The two programs of each trial are in %s' % workFolder)
  infoSpec = """%d of %d trials passed, %d ritual faults."""
  passed = len(verdicts) - len(failed)
  print(infoSpec % (passed, len(verdicts), len(faults)))
  return 1 if failed or faults else 0


if __name__ == '__main__':
  sys.exit(main())
