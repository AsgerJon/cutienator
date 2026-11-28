"""
TestTrialVerdict tests 'Verdict', what a Judge found when it heard one
Trial.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute import MissingVariable
from worktoy.work_test import BaseTest

from cutienator.trial import Verdict


class TestTrialVerdict(BaseTest):
  """
  Tests 'Verdict': what is filled in, how each half ended, the lines
  printed differently, and the verdict in words.

  What to know before adding a test
  ---------------------------------

  - A test fills a verdict in itself, as a 'Judge' would; nothing is
    run.
  """

  @staticmethod
  def _verdict(cpp: tuple, python: tuple) -> Verdict:
    """A verdict filled in with the two runs given."""
    verdict = Verdict()
    verdict.setTrialName('QObject: parent')
    verdict.setCppRun(*cpp)
    verdict.setPythonRun(*python)
    return verdict

  def test_nothing_filled_in(self) -> None:
    """Reading what no judge filled in raises; the short text says it is
    not filled in."""
    verdict = Verdict()
    for read in (verdict.getTrialName, verdict.getCppRun,
                 verdict.getPythonRun):
      with self.subTest(read=read):
        with self.assertRaises(MissingVariable):
          read()
    self.assertEqual(repr(verdict), '<Verdict not filled in yet>')

  def test_what_is_filled_in(self) -> None:
    """The name and each run, as told."""
    verdict = self._verdict((0, 'a\n', ''), (1, '', 'Traceback'))
    self.assertEqual(verdict.getTrialName(), 'QObject: parent')
    self.assertEqual(verdict.getCppRun(), (0, 'a\n', ''))
    self.assertEqual(verdict.getPythonRun(), (1, '', 'Traceback'))

  def test_how_a_program_ended(self) -> None:
    """Each return code in words: stopped, ran, killed by a signal that
    has a name or one that has none, or ended with an error."""
    end = Verdict._describeEnd
    self.assertEqual(end(None), 'was stopped for taking too long')
    self.assertEqual(end(0), 'ran to its end')
    self.assertEqual(end(-11), 'was killed (SIGSEGV)')
    self.assertEqual(end(-1000), 'was killed (signal 1000)')
    self.assertEqual(end(2), 'ended with an error (return code 2)')

  def test_a_verdict_that_passed(self) -> None:
    """Both ran to their end and printed the same."""
    printed = 'one: true\ntwo: false\n'
    verdict = self._verdict((0, printed, ''), (0, printed, ''))
    self.assertIs(verdict.ranInCpp(), True)
    self.assertIs(verdict.functions(), True)
    self.assertIs(verdict.isAsInCpp(), True)
    self.assertIs(verdict.passed(), True)
    self.assertEqual(verdict.getDifferences(), [])
    self.assertEqual(str(verdict), '\n'.join((
        'PASSED  QObject: parent',
        '  the C++ half ran to its end',
        '  the Python half ran to its end',
        '  both printed the same 2 lines',
    )))
    self.assertEqual(repr(verdict), "<Verdict: 'QObject: parent' passed>")

  def test_halves_that_printed_differently(self) -> None:
    """Each line that differs, and a line only one half printed."""
    verdict = self._verdict((0, 'a\nb\n', ''), (0, 'a\nc\nd\n', ''))
    self.assertIs(verdict.passed(), False)
    self.assertEqual(verdict.getDifferences(),
                     [(2, 'b', 'c'), (3, '', 'd')])
    said = str(verdict)
    self.assertIn('  they printed differently:', said)
    self.assertIn('    line 2, C++   : b', said)
    self.assertIn('    line 3, Python: d', said)
    self.assertEqual(repr(verdict), "<Verdict: 'QObject: parent' failed>")
    longer = self._verdict((0, 'a\nb\n', ''), (0, 'a\n', ''))
    self.assertEqual(longer.getDifferences(), [(2, 'b', '')])

  def test_halves_that_did_not_end(self) -> None:
    """A half that died is the same as nothing, and what each half
    complained about is told."""
    verdict = self._verdict((0, 'a\n', 'note\n'), (-6, 'a\n', 'abort'))
    self.assertIs(verdict.functions(), False)
    self.assertIs(verdict.isAsInCpp(), False)
    said = str(verdict)
    self.assertIn('FAILED  QObject: parent', said)
    self.assertIn('  the Python half was killed (SIGABRT)', said)
    self.assertIn('  C++ complained:\n    note', said)
    self.assertIn('  Python complained:\n    abort', said)
    self.assertNotIn('printed', said)
    stopped = self._verdict((None, '', ''), (0, '', '  '))
    self.assertIs(stopped.ranInCpp(), False)
    self.assertNotIn('complained', str(stopped))
