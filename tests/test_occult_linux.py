"""
TestOccultLinux tests 'Linux', which says how ritual files are compiled
and opened on Linux.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import io
import os
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import Linux, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestOccultLinux(BaseTest):
  """
  Tests what 'Linux' answers: the names of Qt's files, what 'clang++'
  and the linker are told, how Qt is opened and where a usual install
  of Qt is found.

  What to know before adding a test
  ---------------------------------

  - What 'Linux' answers is text, the same on every system, so these
    tests run anywhere.
  - Opening a file with 'ctypes' and reading '/proc/self/maps' touch the
    machine. A test of either replaces 'ctypes.CDLL', and the file read,
    for its own length, so it sees what would be opened and read.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _maps(*lines: str) -> Any:
    """A stand-in for 'open' that gives the lines as '/proc/self/maps'."""
    realOpen = open

    def fakeOpen(path: str, *args: Any, **kwargs: Any) -> Any:
      if path == '/proc/self/maps':
        return io.StringIO(''.join('%s\n' % line for line in lines))
      return realOpen(path, *args, **kwargs)

    return fakeOpen

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMES AND FLAGS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_it_answers_for_linux(self) -> None:
    """'Linux' is a 'System' for the platform 'linux'."""
    self.assertIsInstance(Linux(), System)
    self.assertEqual(Linux.__platform_name__, 'linux')

  def test_the_names_of_qt_files(self) -> None:
    """The shared object, static library and '.prl' file of a part."""
    linux = Linux()
    for part, shared, static, prl in (
        ('QtCore', 'libQt6Core.so.6', 'libQt6Core.a', 'libQt6Core.prl'),
        ('Qt3DCore', 'libQt63DCore.so.6', 'libQt63DCore.a',
         'libQt63DCore.prl'),
        ('QtWebEngineCore', 'libQt6WebEngineCore.so.6',
         'libQt6WebEngineCore.a', 'libQt6WebEngineCore.prl'),
    ):
      with self.subTest(part=part):
        self.assertEqual(linux.getQtFileName(part), shared)
        self.assertEqual(linux.getQtStaticFileName(part), static)
        self.assertEqual(linux.getQtPrlFileName(part), prl)

  def test_compiler_flags(self) -> None:
    """'clang++' makes code for a shared object, its names hidden."""
    self.assertEqual(Linux().getCompilerFlags('/qt/lib'), (
        '-fPIC', '-fvisibility=hidden', '-fvisibility-inlines-hidden'))

  def test_no_objective_c(self) -> None:
    """Objective-C++ is not built on Linux."""
    self.assertIs(Linux().buildsObjectiveC(), False)

  def test_linker_flags(self) -> None:
    """The linker refuses a name nothing offers, finds Qt where it is,
    offers only the rituals, and joins only what is used."""
    flags = Linux().getLinkerFlags('/qt/lib')
    self.assertEqual(flags[0], '-Wl,--no-undefined')
    self.assertEqual(flags[1], '-Wl,-rpath,/qt/lib')
    self.assertTrue(flags[2].startswith('-Wl,--version-script='))
    self.assertEqual(flags[3], '-Wl,--as-needed')
    self.assertEqual(len(flags), 4)
    offers = flags[2][len('-Wl,--version-script='):]
    self.assertEqual(os.path.basename(offers), 'linux_offers.map')
    self.assertTrue(os.path.isfile(offers))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPENING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_shared_objects_are_opened_for_all(self) -> None:
    """Each shared object is opened with its names for every file after
    it; a static library is passed by, as it has nothing to open."""
    with mock.patch.object(ctypes, 'CDLL') as opened:
      Linux().prepareOpening(
          '/qt/libQt6Core.so.6', '/qt/libQt6AxServer.a',
          '/qt/libQt6Gui.so.6')
    self.assertEqual(opened.call_args_list, [
        mock.call('/qt/libQt6Core.so.6', mode=ctypes.RTLD_GLOBAL),
        mock.call('/qt/libQt6Gui.so.6', mode=ctypes.RTLD_GLOBAL),
    ])

  def test_opening_nothing_opens_nothing(self) -> None:
    """No file handed: nothing is opened."""
    with mock.patch.object(ctypes, 'CDLL') as opened:
      Linux().prepareOpening()
    opened.assert_not_called()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A USUAL QT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_installer_folders_when_no_qt_opens(self) -> None:
    """When the loader finds no QtCore, the installer's folders alone,
    each with its 'lib', as they are; nothing is read."""
    found = ('/home/me/Qt/6.12.0/gcc_64', '/opt/Qt/6.11.0/gcc_64')
    with mock.patch.object(
        Linux, '_findInstallerFolders', return_value=found) as finder, \
        mock.patch.object(ctypes, 'CDLL', side_effect=OSError('no')), \
        mock.patch('builtins.open') as opened:
      folders = Linux().getUsualQtFolders()
    finder.assert_called_once_with('gcc_64', '~/Qt', '/opt/Qt')
    opened.assert_not_called()
    self.assertEqual(folders, (
        '/home/me/Qt/6.12.0/gcc_64/lib', '/opt/Qt/6.11.0/gcc_64/lib'))

  def test_the_folder_of_the_qt_the_loader_finds(self) -> None:
    """When the loader finds QtCore, its folder, as '/proc/self/maps'
    names it, comes after the installer's; empty lines and lines of
    other files are passed by, and a folder not there is left out."""
    with tempfile.TemporaryDirectory() as root:
      installer = os.path.join(root, 'Qt', '6.12.0', 'gcc_64')
      os.makedirs(os.path.join(installer, 'lib'))
      system = os.path.join(root, 'usr', 'lib')
      os.makedirs(system)
      lines = [
          '7f00-7f10 r-xp 0 08:01 1 /usr/lib/libc.so.6',
          '',
          '7f20-7f30 r-xp 0 08:01 2 %s/libQt6Core.so.6.12.0' % system,
          '7f40-7f50 r-xp 0 08:01 3 /elsewhere/libQt6Core.so.6',
      ]
      with mock.patch.object(
          Linux, '_findInstallerFolders',
          return_value=(installer, os.path.join(root, 'gone'))), \
          mock.patch.object(ctypes, 'CDLL'), \
          mock.patch('builtins.open', self._maps(*lines)):
        folders = Linux().getUsualQtFolders()
    self.assertEqual(folders, (os.path.join(installer, 'lib'), system))

  def test_a_qt_that_opens_but_lies_nowhere_named(self) -> None:
    """When no line of '/proc/self/maps' names QtCore, only the
    installer's folders that are there are given."""
    with tempfile.TemporaryDirectory() as root:
      installer = os.path.join(root, '6.12.0', 'gcc_64')
      os.makedirs(os.path.join(installer, 'lib'))
      lines = ['7f00-7f10 r-xp 0 08:01 1 /usr/lib/libc.so.6']
      with mock.patch.object(
          Linux, '_findInstallerFolders', return_value=(installer,)), \
          mock.patch.object(ctypes, 'CDLL'), \
          mock.patch('builtins.open', self._maps(*lines)):
        folders = Linux().getUsualQtFolders()
    self.assertEqual(folders, (os.path.join(installer, 'lib'),))

  def test_no_usual_qt_at_all(self) -> None:
    """No installer folder and no Qt the loader finds: nothing."""
    with mock.patch.object(
        Linux, '_findInstallerFolders', return_value=()), \
        mock.patch.object(ctypes, 'CDLL', side_effect=OSError('no')):
      self.assertEqual(Linux().getUsualQtFolders(), ())
