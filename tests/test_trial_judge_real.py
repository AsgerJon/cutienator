"""
TestTrialJudgeReal tests 'Judge' against Qt itself: the trials of
QObject heard for real, and the rituals of QtCore checked against its
target file.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import tempfile
import unittest
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import Rituals
from cutienator.trial import Judge, qObjectTrials


#  The tests marked with '_compiles' start 'clang++' for real. They run
#  where 'CUTIENATOR_TEST_COMPILES' is '1': on gcloud, and in a release
#  run on one machine of each system. Every other machine skips them,
#  so it compiles nothing.
_COMPILES = os.environ.get('CUTIENATOR_TEST_COMPILES', '') == '1'
_compiles = unittest.skipUnless(
    _COMPILES, "starts clang++: runs where CUTIENATOR_TEST_COMPILES=1")


@_compiles
class TestTrialJudgeReal(BaseTest):
  """
  Tests 'Judge' for real: it compiles the C++ half of each trial of
  QObject against Qt with 'clang++', runs both halves, and they agree.

  What to know before adding a test
  ---------------------------------

  - It needs 'clang++', Qt's development files ('qmake6' on the path)
    and the target file of QtCore built, as on gcloud. It takes a few
    seconds, most of it compiling.
  """

  def setUp(self) -> None:
    """A judge writing to a temporary folder."""
    super().setUp()
    folder = tempfile.TemporaryDirectory()
    self.addCleanup(folder.cleanup)
    self.judge = Judge()
    self.judge.setWorkFolder(folder.name)

  def test_the_trials_of_qobject_pass(self) -> None:
    """Every trial of QObject is heard, and each passes."""
    for verdict in self.judge.hearAll(*qObjectTrials()):
      with self.subTest(verdict=repr(verdict)):
        self.assertIs(verdict.passed(), True, str(verdict))

  def test_the_rituals_of_qtcore_are_offered(self) -> None:
    """The rituals listed for QtCore are what its target file offers,
    save those left out where it was built."""
    with mock.patch.object(Rituals, 'getBuiltParts',
                           return_value=('QtCore',)):
      faults = self.judge.findRitualFaults()
    self.assertEqual(faults, ())
