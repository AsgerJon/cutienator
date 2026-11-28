"""
TestOccultWindows tests 'Windows', which says how ritual files are
compiled and opened on Windows.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import tempfile
import types
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import Summon, System, Windows
from cutienator.occult import _windows as windowsModule


class TestOccultWindows(BaseTest):
  """
  Tests what 'Windows' answers: the names of Qt's files, what 'clang++'
  and the linker are told, how Python is told where Qt's DLLs are and
  where a usual install of Qt is found.

  What to know before adding a test
  ---------------------------------

  - What 'Windows' answers is text, the same on every system, so these
    tests run anywhere; nothing here needs Windows.
  - 'prepareOpening' tells Python of Qt's folder once for each folder,
    and keeps the folders told for the whole program. A test of it
    replaces what it calls ('os.add_dll_directory', which only Windows
    has, and 'Summon.getQtProgramFolder') and the set of folders told,
    for its own length.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _freshTold(self) -> set:
    """Gives 'Windows' an empty set of folders told for this test."""
    patcher = mock.patch.object(Windows, '__told_folders__', set())
    told = patcher.start()
    self.addCleanup(patcher.stop)
    return told

  @staticmethod
  def _qtFolder(folder: str) -> mock._patch:
    """Has 'Summon' name 'folder' as the folder of Qt's programs."""
    return mock.patch.object(
        Summon, 'getQtProgramFolder', return_value=folder)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMES AND FLAGS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_it_answers_for_windows(self) -> None:
    """'Windows' is a 'System' for the platform 'win32'."""
    self.assertIsInstance(Windows(), System)
    self.assertEqual(Windows.__platform_name__, 'win32')

  def test_the_names_of_qt_files(self) -> None:
    """The file handed to the linker, the static library and the '.prl'
    file of a part."""
    windows = Windows()
    for part, linked, prl in (
        ('QtCore', 'Qt6Core.lib', 'Qt6Core.prl'),
        ('Qt3DCore', 'Qt63DCore.lib', 'Qt63DCore.prl'),
        ('QtAxServer', 'Qt6AxServer.lib', 'Qt6AxServer.prl'),
    ):
      with self.subTest(part=part):
        self.assertEqual(windows.getQtFileName(part), linked)
        self.assertEqual(windows.getQtStaticFileName(part), linked)
        self.assertEqual(windows.getQtPrlFileName(part), prl)

  def test_compiler_flags(self) -> None:
    """The flags Qt's own build gives on Windows, and 'cmpxchg16b'."""
    self.assertEqual(Windows().getCompilerFlags('C:\\Qt\\lib'), (
        '-fms-runtime-lib=dll', '-DNOMINMAX', '-DWIN32', '-DWIN64',
        '-D_WIN64', '-D_ENABLE_EXTENDED_ALIGNED_STORAGE', '-DUNICODE',
        '-D_UNICODE', '-mcx16'))

  def test_no_objective_c(self) -> None:
    """Objective-C++ is not built on Windows."""
    self.assertIs(Windows().buildsObjectiveC(), False)

  def test_linker_flags(self) -> None:
    """The linker is told nothing beyond what every system tells it."""
    self.assertEqual(Windows().getLinkerFlags('C:\\Qt\\lib'), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPENING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_python_is_told_the_folder_of_qt_once(self) -> None:
    """Python 3.8 and later are told Qt's folder by 'add_dll_directory',
    once, whatever the files handed."""
    told = self._freshTold()
    folder = os.path.normpath('/qt/bin')
    with self._qtFolder('/qt/bin/'), mock.patch.object(
        os, 'add_dll_directory', create=True) as add:
      Windows().prepareOpening('/qt/lib/Qt6Core.lib')
      Windows().prepareOpening('/qt/lib/Qt6Gui.lib')
    add.assert_called_once_with(folder)
    self.assertEqual(told, {folder})

  def test_each_folder_is_told_on_its_own(self) -> None:
    """A second folder of Qt is told as well."""
    told = self._freshTold()
    with mock.patch.object(os, 'add_dll_directory', create=True) as add:
      with self._qtFolder('/first/bin'):
        Windows().prepareOpening()
      with self._qtFolder('/second/bin'):
        Windows().prepareOpening()
    self.assertEqual(add.call_args_list, [
        mock.call(os.path.normpath('/first/bin')),
        mock.call(os.path.normpath('/second/bin')),
    ])
    self.assertEqual(len(told), 2)

  def test_an_old_python_is_told_by_path(self) -> None:
    """Python 3.7 has no 'add_dll_directory': Qt's folder goes first on
    'PATH', once."""
    self._freshTold()
    folder = os.path.normpath('/qt/bin')
    oldSys = types.SimpleNamespace(version_info=(3, 7, 9))
    with self._qtFolder('/qt/bin'), \
        mock.patch.object(windowsModule, 'sys', oldSys), \
        mock.patch.dict(os.environ, PATH='/usr/bin'):
      Windows().prepareOpening()
      Windows().prepareOpening()
      self.assertEqual(
          os.environ['PATH'], os.pathsep.join((folder, '/usr/bin')))

  def test_an_old_python_with_no_path(self) -> None:
    """With no 'PATH' at all, it becomes Qt's folder and nothing more."""
    self._freshTold()
    folder = os.path.normpath('/qt/bin')
    oldSys = types.SimpleNamespace(version_info=(3, 7, 9))
    with self._qtFolder('/qt/bin'), \
        mock.patch.object(windowsModule, 'sys', oldSys), \
        mock.patch.dict(os.environ, clear=True):
      Windows().prepareOpening()
      self.assertEqual(os.environ['PATH'], os.pathsep.join((folder, '')))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A USUAL QT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_installer_folders_that_are_there(self) -> None:
    """The installer's folders of Visual Studio's kit, each with 'lib',
    only when it is there."""
    with tempfile.TemporaryDirectory() as root:
      kit = os.path.join(root, '6.12.0', 'msvc2022_64')
      os.makedirs(os.path.join(kit, 'lib'))
      gone = os.path.join(root, '6.11.0', 'msvc2022_64')
      with mock.patch.object(
          Windows, '_findInstallerFolders',
          return_value=(kit, gone)) as finder:
        folders = Windows().getUsualQtFolders()
    finder.assert_called_once_with('msvc2022_64', 'C:\\Qt')
    self.assertEqual(folders, (os.path.join(kit, 'lib'),))

  def test_no_usual_qt_at_all(self) -> None:
    """No installer folder: nothing given."""
    with mock.patch.object(
        Windows, '_findInstallerFolders', return_value=()):
      self.assertEqual(Windows().getUsualQtFolders(), ())
