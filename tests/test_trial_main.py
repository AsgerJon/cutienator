"""
TestTrialMain tests 'python -m cutienator.trial', which builds what is
stale, hears every trial and prints the verdicts.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import contextlib
import io
import runpy
import sys
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import Rituals
from cutienator.trial import Judge
from cutienator.trial.__main__ import main

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Tuple


class _Verdict:
  """Stands in for a verdict: passed or not, and its words."""

  def __init__(self, passed: bool) -> None:
    """Whether it passed."""
    self.__passed__ = passed

  def passed(self) -> bool:
    """Whether it passed."""
    return self.__passed__

  def __str__(self) -> str:
    """Its words."""
    return 'VERDICT %s' % ('passed' if self.__passed__ else 'failed')


class TestTrialMain(BaseTest):
  """
  Tests 'main' of 'cutienator.trial' with stand-ins for 'Rituals' and
  the judge: what it builds, what it prints, and its exit code.

  What to know before adding a test
  ---------------------------------

  - Nothing is built or heard. 'Rituals' and 'Judge' are patched, and
    the work folder is a temporary folder of the test.
  """

  def setUp(self) -> None:
    """A temporary work folder, and 'Rituals' with two built parts and
    three rituals."""
    super().setUp()
    folder = tempfile.TemporaryDirectory()
    self.addCleanup(folder.cleanup)
    self.folder = folder.name
    for target, name, value in (
        (tempfile, 'mkdtemp', self.folder),
        (Rituals, 'getBuiltParts', ('QtCore', 'QtGui')),
        (Rituals, 'getRitualFolder', '/rituals'),
        (Rituals, 'getRitualNames', ('a', 'b', 'c')),
    ):
      patcher = mock.patch.object(target, name, return_value=value)
      patcher.start()
      self.addCleanup(patcher.stop)

  def _main(self, stale: bool, faults: Tuple[str, ...],
            *verdicts: _Verdict) -> Tuple[int, str, Any]:
    """Runs 'main', and gives its exit code, what it printed, and the
    stand-in of 'Rituals.summon'."""
    printed = io.StringIO()
    with mock.patch.object(Rituals, 'isStale', return_value=stale):
      with mock.patch.object(Rituals, 'summon') as summon:
        with mock.patch.object(Judge, 'findRitualFaults',
                               return_value=faults):
          with mock.patch.object(Judge, 'hearAll',
                                 return_value=verdicts):
            with contextlib.redirect_stdout(printed):
              code = main()
    return code, printed.getvalue(), summon

  def test_nothing_at_fault(self) -> None:
    """Nothing stale is built; every trial passed and no fault: 0."""
    code, printed, summon = self._main(False, (), _Verdict(True))
    self.assertEqual(code, 0)
    summon.assert_not_called()
    self.assertNotIn('Building', printed)
    self.assertIn('all 3 listed rituals are offered', printed)
    self.assertIn('VERDICT passed', printed)
    self.assertIn('are in %s' % self.folder, printed)
    self.assertIn('1 of 1 trials passed, 0 ritual faults.', printed)

  def test_what_is_stale_is_built(self) -> None:
    """Stale target files are built first."""
    code, printed, summon = self._main(True, (), _Verdict(True))
    summon.assert_called_once_with()
    self.assertIn('Building 2 target files beside /rituals', printed)

  def test_a_fault_or_a_failed_trial(self) -> None:
    """A ritual fault, or a trial that failed: 1, and each is told."""
    code, printed, _ = self._main(False, ('a fault',), _Verdict(True))
    self.assertEqual(code, 1)
    self.assertIn('  a fault', printed)
    self.assertNotIn('listed rituals are offered', printed)
    code, printed, _ = self._main(False, (), _Verdict(False),
                                  _Verdict(True))
    self.assertEqual(code, 1)
    self.assertIn('1 of 2 trials passed', printed)

  def test_run_as_a_program(self) -> None:
    """Run as 'python -m cutienator.trial', it exits with the code of
    'main'."""
    with mock.patch.object(Rituals, 'isStale', return_value=False):
      with mock.patch.object(Judge, 'findRitualFaults', return_value=()):
        with mock.patch.object(Judge, 'hearAll', return_value=()):
          with contextlib.redirect_stdout(io.StringIO()):
            with mock.patch.dict(sys.modules):
              #  Run anew, as Python runs it, not as it was imported.
              sys.modules.pop('cutienator.trial.__main__', None)
              with self.assertRaises(SystemExit) as caught:
                runpy.run_module('cutienator.trial', run_name='__main__')
    self.assertEqual(caught.exception.code, 0)
