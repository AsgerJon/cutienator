"""
TestSystem tests 'System' and its three subclasses, 'Linux', 'MacOS' and
'Windows', which say what differs between the operating systems.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator import occult
from cutienator.occult import System, Linux, MacOS, Windows, Summon

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
        ('-Wl,-rpath,/opt/qt/lib',),
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
    with mock.patch.object(Summon, 'getQtProgramFolder', lambda: 'qt/bin'):
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
    with mock.patch.object(Summon, 'getQtProgramFolder', lambda: 'qt/bin'):
      with mock.patch.object(os, 'environ', environment):
        with mock.patch.object(sys, 'version_info', (3, 7, 9)):
          Windows().prepareOpening()
    expected = os.pathsep.join((folder, 'elsewhere'))
    self.assertEqual(environment, dict(PATH=expected))

  def test_static_and_prl_file_names(self) -> None:
    """Each system names the static library and the '.prl' file of a
    part as Qt installs them."""
    self.assertEqual(
        Linux().getQtStaticFileName('QtAxContainer'), 'libQt6AxContainer.a')
    self.assertEqual(
        MacOS().getQtStaticFileName('QtAxContainer'), 'libQt6AxContainer.a')
    self.assertEqual(
        Windows().getQtStaticFileName('QtAxContainer'), 'Qt6AxContainer.lib')
    self.assertEqual(Linux().getQtPrlFileName('QtCore'), 'libQt6Core.prl')
    self.assertEqual(MacOS().getQtPrlFileName('QtCore'), 'libQt6Core.prl')
    self.assertEqual(Windows().getQtPrlFileName('QtCore'), 'Qt6Core.prl')

  def _readPrl(self, text: str) -> tuple:
    """Writes 'text' as the '.prl' file of 'QtAxContainer' on Windows into
    a new folder, and gives what 'readStaticDependencies' reads of it,
    with the folder written as 'QT'."""
    with tempfile.TemporaryDirectory() as folder:
      path = os.path.join(folder, 'Qt6AxContainer.prl')
      with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
      words = Windows().readStaticDependencies(folder, 'QtAxContainer')
    return (*(word.replace(folder, 'QT') for word in words),)

  def test_a_static_library_names_what_it_needs(self) -> None:
    """A static library's '.prl' file gives its libraries, the folder of
    Qt put in for '$$[QT_INSTALL_LIBS]'."""
    text = """QMAKE_PRL_TARGET = Qt6AxContainer.lib
QMAKE_PRL_CONFIG = static
QMAKE_PRL_LIBS = $$[QT_INSTALL_LIBS]/Qt6AxBase.lib -lole32 -luuid
"""
    self.assertEqual(
        self._readPrl(text), ('QT/Qt6AxBase.lib', '-lole32', '-luuid'))

  def test_a_shared_object_needs_nothing_beside_it(self) -> None:
    """A part Qt builds as a shared object brings its own libraries, so
    its '.prl' file gives nothing, whatever it lists."""
    text = """QMAKE_PRL_TARGET = Qt6Core.lib
QMAKE_PRL_CONFIG = shared
QMAKE_PRL_LIBS = -lole32
"""
    self.assertEqual(self._readPrl(text), ())

  def test_no_prl_file_needs_nothing(self) -> None:
    """A part with no '.prl' file gives nothing."""
    with tempfile.TemporaryDirectory() as folder:
      words = Linux().readStaticDependencies(folder, 'QtAxContainer')
    self.assertEqual(words, ())
