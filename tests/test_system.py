"""
TestSystem tests 'System' and its three subclasses, 'Linux', 'MacOS' and
'Windows', which say what differs between the operating systems.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator import occult
from cutienator.occult import System, Linux, MacOS, Windows, Build

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict


class TestSystem(BaseTest):
  """
  Tests what each system answers, on whichever system the tests run.

  What to know before adding a test
  ---------------------------------

  - The answers of all three systems are tested everywhere: what
    'Windows' says of a file name or a flag is text, and can be read on
    Linux as well.
  - Only 'Windows.prepareOpening' does something, and only Windows can
    do it. Here the two things it calls are replaced for the length of
    one test, so the test sees what it would have told Python. That it
    works for real is tested by 'TestQObject' in the rows that run on
    Windows.
  - 'System.getHere()' keeps its answer for the whole program. A test
    that makes it answer anew puts the kept answer back before it ends.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHICH SYSTEM   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_three_systems_are_known(self) -> None:
    """'System' has the three subclasses, each with its platform name."""
    named = {s.__platform_name__: s for s in System.__subclasses__()}
    self.assertEqual(named, dict(linux=Linux, darwin=MacOS, win32=Windows))
    self.assertIsNone(System.__platform_name__)

  def test_here_is_the_system_python_runs_on(self) -> None:
    """'getHere' gives the one whose platform name Python has here."""
    here = System.getHere()
    self.assertIsInstance(here, System)
    self.assertEqual(type(here).__platform_name__, sys.platform)

  def test_here_is_kept(self) -> None:
    """'getHere' gives the same object every time, on any subclass."""
    self.assertIs(System.getHere(), System.getHere())
    self.assertIs(Linux.getHere(), System.getHere())

  def test_unknown_system_is_refused(self) -> None:
    """'getHere' refuses a system no subclass is written for, by name."""
    kept = System.__system_here__
    System.__system_here__ = None
    try:
      with mock.patch.object(sys, 'platform', 'plan9'):
        with self.assertRaises(NotImplementedError) as context:
          System.getHere()
    finally:
      System.__system_here__ = kept
    self.assertIn("'plan9'", str(context.exception))
    self.assertIs(System.getHere(), kept)

  def test_text_names_the_system(self) -> None:
    """The text of a system is the name of its class in angle brackets."""
    self.assertEqual(str(Linux()), '<Linux>')
    self.assertEqual(repr(MacOS()), '<MacOS>')
    self.assertEqual(str(Windows()), '<Windows>')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT EACH ANSWERS  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_qt_file_names(self) -> None:
    """Each system names the file of a part of Qt in its own way."""
    self.assertEqual(Linux().getQtFileName('QtCore'), 'libQt6Core.so.6')
    self.assertEqual(Linux().getQtFileName('QtGui'), 'libQt6Gui.so.6')
    self.assertEqual(
        MacOS().getQtFileName('QtCore'),
        'QtCore.framework/Versions/A/QtCore',
    )
    self.assertEqual(
        MacOS().getQtFileName('QtWidgets'),
        'QtWidgets.framework/Versions/A/QtWidgets',
    )
    self.assertEqual(Windows().getQtFileName('QtCore'), 'Qt6Core.lib')
    self.assertEqual(Windows().getQtFileName('QtGui'), 'Qt6Gui.lib')

  def test_compiler_flags(self) -> None:
    """On macOS the folder of the frameworks comes on top of Linux's."""
    self.assertEqual(
        Linux().getCompilerFlags('/opt/qt/lib'),
        ('-fPIC', '-fvisibility=hidden', '-fvisibility-inlines-hidden',),
    )
    self.assertEqual(
        MacOS().getCompilerFlags('/opt/qt/lib'),
        (
          '-fPIC', '-fvisibility=hidden', '-fvisibility-inlines-hidden',
          '-F/opt/qt/lib',
        ),
    )
    self.assertEqual(
        Windows().getCompilerFlags('C:/Qt/lib'), ('-fms-runtime-lib=dll',),
    )

  def test_linker_flags(self) -> None:
    """Linux and macOS have the Qt folder written in; Windows cannot.
    Linux is also told to offer the rituals and nothing else, and to
    name only the Qt shared objects it calls into."""
    offers = os.path.join(
        os.path.dirname(os.path.abspath(occult.__file__)),
        'linux_offers.map',
    )
    self.assertTrue(os.path.isfile(offers))
    self.assertEqual(
        Linux().getLinkerFlags('/opt/qt/lib'),
        (
            '-Wl,--no-undefined', '-Wl,-rpath,/opt/qt/lib',
            '-Wl,--version-script=%s' % offers, '-Wl,--as-needed',
        ),
    )
    self.assertEqual(
        MacOS().getLinkerFlags('/opt/qt/lib'),
        ('-Wl,-undefined,error', '-Wl,-rpath,/opt/qt/lib',),
    )
    self.assertEqual(Windows().getLinkerFlags('C:/Qt/lib'), ())

  def test_system_itself_answers_nothing(self) -> None:
    """Asked of 'System' and not of a subclass, each question raises."""
    system = System()
    for ask in (
        lambda: system.getQtFileName('QtCore'),
        lambda: system.getCompilerFlags('/opt/qt/lib'),
        lambda: system.getLinkerFlags('/opt/qt/lib'),
        lambda: system.prepareOpening(),
    ):
      with self.assertRaises(NotImplementedError) as context:
        ask()
      self.assertIn('System.getHere()', str(context.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BEFORE OPENING   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_linux_and_mac_prepare_nothing(self) -> None:
    """On Linux and macOS nothing is done before a file is opened."""
    before = dict(os.environ)
    self.assertIsNone(Linux().prepareOpening())
    self.assertIsNone(MacOS().prepareOpening())
    self.assertEqual(dict(os.environ), before)

  def test_windows_tells_python_of_the_qt_folder(self) -> None:
    """From Python 3.8 on, Windows hands the folder of Qt's DLLs over."""
    told = []
    folder = os.path.join('qt', 'bin')
    with mock.patch.object(Build, 'getQtProgramFolder', lambda: 'qt/bin'):
      with mock.patch.object(
          os, 'add_dll_directory', told.append, create=True,
      ):
        with mock.patch.object(sys, 'version_info', (3, 8, 0)):
          Windows().prepareOpening()
    self.assertEqual(told, [folder])

  def test_windows_puts_the_qt_folder_first_in_path(self) -> None:
    """On Python 3.7, Windows puts the folder of Qt's DLLs into PATH."""
    environment = dict(PATH='elsewhere')  # type: Dict[str, str]
    folder = os.path.join('qt', 'bin')
    with mock.patch.object(Build, 'getQtProgramFolder', lambda: 'qt/bin'):
      with mock.patch.object(os, 'environ', environment):
        with mock.patch.object(sys, 'version_info', (3, 7, 9)):
          Windows().prepareOpening()
    expected = os.pathsep.join((folder, 'elsewhere'))
    self.assertEqual(environment, dict(PATH=expected))
