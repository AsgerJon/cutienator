"""
TestTrialJudge tests 'Judge', which writes a Trial out as a C++ program
and a Python program, runs both, and gives a Verdict.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

import cutienator
from cutienator.occult import Rituals, Summon, System
from cutienator.trial import Judge, Trial, Verdict

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any

_RUN = 'cutienator.trial._judge.subprocess.run'


class _Done:
  """Stands in for what 'subprocess.run' gives back."""

  def __init__(self, code: int, out: str = '', err: str = '') -> None:
    """The return code and what was printed and complained."""
    self.returncode, self.stdout, self.stderr = code, out, err


class _Symbol:
  """Stands in for a function a shared object offers."""

  def __init__(self, mangled: str) -> None:
    """Its name as the shared object has it."""
    self.mangled = mangled


class TestTrialJudge(BaseTest):
  """
  Tests 'Judge' with stand-ins for Qt and for the programs: the work
  folder and the time a half may run, what is found for the judge, the
  two programs written from a trial, compiling and running them, the
  ritual faults, and hearing trials.

  What to know before adding a test
  ---------------------------------

  - Nothing is compiled or run here: 'subprocess.run' is replaced in the
    module of the judge. One trial heard for real, against Qt itself,
    is in 'TestTrialJudgeReal'.
  - Qt's header folder and shared object folder are made-up folders in
    a temporary folder of the test ('self.qt'), with a header for
    'QObject' and 'QTimer' in 'QtCore', and 'QPoint' in two parts.
  """

  def setUp(self) -> None:
    """A temporary folder, made-up folders of Qt in it, and 'Summon'
    told them."""
    super().setUp()
    folder = tempfile.TemporaryDirectory()
    self.addCleanup(folder.cleanup)
    self.folder = folder.name
    self.qt = os.path.join(self.folder, 'qt')
    headers = os.path.join(self.qt, 'include')
    shared = os.path.join(self.qt, 'lib')
    for part, names in (('QtCore', ('QObject', 'QTimer', 'QPoint')),
                        ('QtGui', ('QPoint',)), ('QtWidgets', ())):
      os.makedirs(os.path.join(headers, part))
      for name in names:
        open(os.path.join(headers, part, name), 'w').close()
    os.makedirs(shared)
    self.core = os.path.join(
        shared, System.getHere().getQtFileName('QtCore'))
    open(self.core, 'w').close()
    for name, value in (('getQtHeaderFolder', headers),
                        ('getQtSharedObjectFolder', shared)):
      patcher = mock.patch.object(Summon, name, return_value=value)
      patcher.start()
      self.addCleanup(patcher.stop)
    self.headers, self.shared = headers, shared

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _trial(name: str = 'QObject: parent and setParent') -> Trial:
    """A trial of every kind of step, of two classes of QtCore."""
    trial = Trial()
    trial.setName(name)
    trial.make('mother', 'QObject')
    trial.make('child', 'QObject')
    trial.make('timer', 'QTimer')
    trial.call('child', 'setParent', 'mother')
    trial.call('child', 'setParent', None)
    trial.expectSame('child', 'parent', 'mother')
    trial.expectNothing('child', 'parent')
    return trial

  def _judge(self) -> Judge:
    """A judge writing to the temporary folder."""
    judge = Judge()
    judge.setWorkFolder(self.folder)
    return judge

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT YOU PROVIDE   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_work_folder(self) -> None:
    """Asked before it is set, it raises; it is kept in full; what is no
    text or no folder is refused."""
    judge = Judge()
    with self.assertRaises(MissingVariable):
      judge.getWorkFolder()
    self.assertEqual(str(judge), '<Judge still waiting for: setWorkFolder>')
    judge.setWorkFolder(os.path.relpath(self.folder))
    self.assertEqual(judge.getWorkFolder(), os.path.abspath(self.folder))
    self.assertEqual(str(judge), "<Judge writing to '%s'>" % os.path.abspath(
        self.folder))
    self.assertEqual(repr(judge), str(judge))
    with self.assertRaises(TypeException):
      judge.setWorkFolder(7)
    with self.assertRaises(FileNotFoundError):
      judge.setWorkFolder(os.path.join(self.folder, 'nowhere'))

  def test_the_time_a_half_may_run(self) -> None:
    """60 seconds unless told; a number above zero, and nothing else."""
    judge = Judge()
    self.assertEqual(judge.getTimeout(), 60.)
    judge.setTimeout(5)
    self.assertEqual(judge.getTimeout(), 5.)
    self.assertIsInstance(judge.getTimeout(), float)
    for wrong in (True, '5', None):
      with self.subTest(wrong=wrong):
        with self.assertRaises(TypeException):
          judge.setTimeout(wrong)
    for wrong in (0, -1.5):
      with self.subTest(wrong=wrong):
        with self.assertRaises(ValueError):
          judge.setTimeout(wrong)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FOUND FOR YOU  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_python_and_the_package(self) -> None:
    """The Python running the judge, and the folder holding this very
    cutienator."""
    judge = Judge()
    self.assertEqual(judge.getPython(), sys.executable)
    here = os.path.dirname(os.path.dirname(os.path.abspath(
        cutienator.__file__)))
    self.assertEqual(judge.getPackageFolder(), here)

  def test_the_environment_of_both_halves(self) -> None:
    """The package folder first on the path, before any path there was;
    Qt's messages to the error stream; off screen unless told."""
    judge = Judge()
    package = judge.getPackageFolder()
    with mock.patch.dict(os.environ, {}, clear=True):
      environment = judge.getEnvironment()
    self.assertEqual(environment['PYTHONPATH'], package)
    self.assertEqual(environment['QT_FORCE_STDERR_LOGGING'], '1')
    self.assertEqual(environment['QT_QPA_PLATFORM'], 'offscreen')
    given = dict(PYTHONPATH='/mine', QT_QPA_PLATFORM='xcb')
    with mock.patch.dict(os.environ, given, clear=True):
      environment = judge.getEnvironment()
    self.assertEqual(environment['PYTHONPATH'],
                     os.pathsep.join((package, '/mine')))
    self.assertEqual(environment['QT_QPA_PLATFORM'], 'xcb')

  def test_the_part_of_a_class(self) -> None:
    """The one part with a header of the class; none, or two, is
    refused."""
    judge = Judge()
    self.assertEqual(judge.getQtModule('QObject'), 'QtCore')
    for name, listed in (('QNothing', 'none'), ('QPoint', 'QtCore, QtGui')):
      with self.subTest(name=name):
        with self.assertRaises(LookupError) as caught:
          judge.getQtModule(name)
        self.assertIn('but found: %s.' % listed, str(caught.exception))

  def test_the_shared_object_of_a_class(self) -> None:
    """The shared object of its part, which has to be there."""
    judge = Judge()
    self.assertEqual(judge.getQtSharedObject('QObject'), self.core)
    os.remove(self.core)
    with self.assertRaises(FileNotFoundError) as caught:
      judge.getQtSharedObject('QObject')
    self.assertIn("'QObject' belongs to 'QtCore'", str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE TWO PROGRAMS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_file_stem_of_a_trial(self) -> None:
    """Letters and digits in lower case, the rest as one underscore."""
    self.assertEqual(Judge.getFileStem(self._trial()),
                     'qobject_parent_and_setparent')
    self.assertEqual(Judge.getFileStem(self._trial(' -A--b 2- ')), 'a_b_2')

  def test_the_cpp_half(self) -> None:
    """Qt's headers, and each step as C++ writes it."""
    self.assertEqual(Judge().getCppProgram(self._trial()), '\n'.join((
        '//  Written by cutienator.trial, and written again each time',
        '//  the trial is heard. Changes made here are lost.',
        '//  Trial: QObject: parent and setParent',
        '#include <QtCore/QObject>',
        '#include <QtCore/QTimer>',
        '#include <iostream>',
        '',
        'int main() {',
        '  std::cout << std::boolalpha;',
        '  QObject *mother = new QObject();',
        '  QObject *child = new QObject();',
        '  QTimer *timer = new QTimer();',
        '  child->setParent(mother);',
        '  child->setParent(nullptr);',
        '  std::cout << "child.parent() is mother: "',
        '            << (child->parent() == mother) << "\\n";',
        '  std::cout << "child.parent() is nothing: "',
        '            << (child->parent() == nullptr) << "\\n";',
        '  return 0;',
        '}',
        '',
    )))

  def test_the_python_half(self) -> None:
    """The cute classes of their parts, and each step as Python writes
    it."""
    self.assertEqual(Judge().getPythonProgram(self._trial()), '\n'.join((
        '#  Written by cutienator.trial, and written again each time',
        '#  the trial is heard. Changes made here are lost.',
        '#  Trial: QObject: parent and setParent',
        'from __future__ import annotations',
        '',
        'from cutienator.QtCore import QObject',
        'from cutienator.QtCore import QTimer',
        '',
        '',
        'def word(flag: bool) -> str:',
        '  """Spells a truth value the way C++ prints it."""',
        "  return 'true' if flag else 'false'",
        '',
        '',
        'mother = QObject()',
        'child = QObject()',
        'timer = QTimer()',
        'child.setParent(mother)',
        'child.setParent(None)',
        "print('child.parent() is mother:', word(child.parent() is "
        "mother))",
        "print('child.parent() is nothing:', word(child.parent() is "
        "None))",
        '',
    )))

  def test_a_step_of_no_kind(self) -> None:
    """A step of a kind neither half knows is refused by both."""
    trial = self._trial()
    trial._addStep('odd', 'child', 'parent', ())
    for write in (Judge().getCppProgram, Judge().getPythonProgram):
      with self.subTest(write=write):
        with self.assertRaises(ValueError) as caught:
          write(trial)
        self.assertIn("unknown kind 'odd'", str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  COMPILING AND RUNNING  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_compiling_the_cpp_half(self) -> None:
    """'clang++' told the headers, and each shared object once."""
    with mock.patch(_RUN, return_value=_Done(0)) as run:
      Judge()._compile(self._trial(), 'in.cpp', 'out')
    command = run.call_args[0][0]
    self.assertEqual(command[:3], ('clang++', '-std=c++17', '-O2'))
    self.assertIn('-I%s' % self.headers, command)
    self.assertEqual(command[-4:], ('in.cpp', '-o', 'out', self.core))

  def test_a_cpp_half_that_does_not_compile(self) -> None:
    """What 'clang++' said is told; no 'clang++' at all is told too."""
    refused = _Done(1, err='  no member named parent  ')
    with mock.patch(_RUN, return_value=refused):
      with self.assertRaises(RuntimeError) as caught:
        Judge()._compile(self._trial(), 'in.cpp', 'out')
    said = str(caught.exception)
    self.assertIn("'QObject: parent and setParent' does not compile", said)
    self.assertIn('said:\n      no member named parent', said)
    with mock.patch(_RUN, side_effect=FileNotFoundError):
      with self.assertRaises(FileNotFoundError) as caught:
        Judge()._compile(self._trial(), 'in.cpp', 'out')
    self.assertIn("'clang++' is needed", str(caught.exception))

  def test_running_a_half(self) -> None:
    """How it ended, what it printed and complained, run with the
    environment of the judge and its time."""
    judge = Judge()
    judge.setTimeout(3)
    with mock.patch(_RUN, return_value=_Done(0, 'out', 'err')) as run:
      self.assertEqual(judge._runHalf('prog', 'arg'), (0, 'out', 'err'))
    args, kwargs = run.call_args
    self.assertEqual(args, (('prog', 'arg'),))
    self.assertEqual(kwargs['timeout'], 3.)
    self.assertEqual(kwargs['env']['QT_FORCE_STDERR_LOGGING'], '1')

  def test_a_half_that_takes_too_long(self) -> None:
    """Stopped, with what it printed so far, as text whichever way it
    came; nothing raised."""
    judge = Judge()
    for printed, shown in ((b'half\xff', 'half�'), ('half', 'half'),
                           (None, '')):
      with self.subTest(printed=printed):
        expired = subprocess.TimeoutExpired('prog', 60., output=printed)
        with mock.patch(_RUN, side_effect=expired):
          self.assertEqual(judge._runHalf('prog'), (
              None, shown, 'It did not end within 60.0 seconds.'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  RITUAL FAULTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_ritual_faults(self) -> None:
    """A ritual listed and not offered, and one offered and not listed,
    each a sentence; none when the two agree."""
    shared = mock.MagicMock()
    shared.return_value.functions.return_value = [
        _Symbol('ritual_b'), _Symbol('ritual_c')]
    for name, value in (
        ('getBuiltParts', ('QtFake',)),
        ('getSigils', {'ritual_a': 1, 'ritual_b': 2}),
        ('getTargetFile', '/made/up.so'),
    ):
      patcher = mock.patch.object(Rituals, name, return_value=value)
      patcher.start()
      self.addCleanup(patcher.stop)
    with mock.patch('cutienator.trial._judge.SharedObject', shared):
      faults = Judge().findRitualFaults()
      shared.assert_called_once_with('/made/up.so')
      self.assertEqual(len(faults), 2)
      self.assertIn("The ritual 'ritual_a' is listed for QtFake",
                    faults[0])
      self.assertIn("of QtFake offers 'ritual_c'", faults[1])
      shared.return_value.functions.return_value = [
          _Symbol('ritual_a'), _Symbol('ritual_b')]
      self.assertEqual(Judge().findRitualFaults(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HEARING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_hearing_a_trial(self) -> None:
    """Both programs written under the stem, the C++ one compiled, each
    run, and the verdict filled in."""
    judge = self._judge()
    trial = self._trial()
    stem = os.path.join(self.folder, 'qobject_parent_and_setparent')
    runs = {stem: (0, 'same\n', ''),
            sys.executable: (0, 'same\n', '')}

    def runHalf(*command: str) -> Any:
      return runs[command[0]]

    with mock.patch.object(Judge, '_compile') as compiled:
      with mock.patch.object(Judge, '_runHalf', side_effect=runHalf):
        verdict = judge.hear(trial)
    compiled.assert_called_once_with(trial, '%s.cpp' % stem, stem)
    self.assertIsInstance(verdict, Verdict)
    self.assertIs(verdict.passed(), True)
    self.assertEqual(verdict.getTrialName(), trial.getName())
    with open('%s.cpp' % stem) as file:
      self.assertEqual(file.read(), judge.getCppProgram(trial))
    with open('%s.py' % stem) as file:
      self.assertEqual(file.read(), judge.getPythonProgram(trial))

  def test_hearing_what_is_no_trial(self) -> None:
    """Only a trial is heard."""
    with self.assertRaises(TypeException):
      self._judge().hear('trial')

  def test_hearing_several_trials(self) -> None:
    """The verdicts in the order of the trials; two trials written to
    the same files are refused."""
    judge = self._judge()
    trials = [self._trial('first'), self._trial('second')]

    def hear(trial: Trial) -> str:
      return trial.getName()

    with mock.patch.object(Judge, 'hear', side_effect=hear):
      self.assertEqual(judge.hearAll(*trials), ('first', 'second'))
      with mock.patch('os.cpu_count', return_value=None):
        self.assertEqual(judge.hearAll(*trials), ('first', 'second'))
    with self.assertRaises(ValueError) as caught:
      judge.hearAll(self._trial('Same!'), self._trial('same'))
    self.assertIn("files named 'same'", str(caught.exception))
