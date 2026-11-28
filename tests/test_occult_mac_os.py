"""
TestOccultMacOS tests 'MacOS', which says how ritual files are compiled
and opened on macOS.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import os
import tempfile
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import MacOS, System


class TestOccultMacOS(BaseTest):
  """
  Tests what 'MacOS' answers: the names of Qt's files in its frameworks,
  what 'clang++' and the linker are told, where the headers of a part
  lie, how Qt is opened and where a usual install of Qt is found.

  What to know before adding a test
  ---------------------------------

  - What 'MacOS' answers is text, the same on every system, so these
    tests run anywhere; nothing here needs a Mac.
  - The frameworks and the installer's folders are made in a temporary
    folder; 'ctypes.CDLL' is replaced for a test that opens Qt.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMES AND FLAGS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_it_answers_for_macos(self) -> None:
    """'MacOS' is a 'System' for the platform 'darwin'."""
    self.assertIsInstance(MacOS(), System)
    self.assertEqual(MacOS.__platform_name__, 'darwin')

  def test_the_names_of_qt_files(self) -> None:
    """The shared object lies in its framework; the static library and
    the '.prl' file are named as on Linux."""
    mac = MacOS()
    self.assertEqual(
        mac.getQtFileName('QtCore'), 'QtCore.framework/Versions/A/QtCore')
    self.assertEqual(mac.getQtStaticFileName('QtCore'), 'libQt6Core.a')
    self.assertEqual(mac.getQtPrlFileName('QtCore'), 'libQt6Core.prl')
    self.assertEqual(
        mac.getQtFileName('Qt3DCore'),
        'Qt3DCore.framework/Versions/A/Qt3DCore')
    self.assertEqual(mac.getQtStaticFileName('Qt3DCore'), 'libQt63DCore.a')

  def test_compiler_flags(self) -> None:
    """As on Linux, and 'clang++' is told where the frameworks are."""
    self.assertEqual(MacOS().getCompilerFlags('/qt/lib'), (
        '-fPIC', '-fvisibility=hidden', '-fvisibility-inlines-hidden',
        '-F/qt/lib'))

  def test_objective_c(self) -> None:
    """Objective-C++ is built on macOS."""
    self.assertIs(MacOS().buildsObjectiveC(), True)

  def test_linker_flags(self) -> None:
    """The linker finds Qt where it is, and joins Apple's frameworks the
    Objective-C++ rituals call."""
    self.assertEqual(MacOS().getLinkerFlags('/qt/lib'), (
        '-Wl,-rpath,/qt/lib', '-framework', 'Foundation', '-framework',
        'AppKit', '-framework', 'Metal', '-framework', 'QuartzCore',
        '-lobjc'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HEADERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_private_folders_in_the_framework(self) -> None:
    """A part with a framework keeps its headers in it."""
    with tempfile.TemporaryDirectory() as qt:
      headers = os.path.join(qt, 'QtWidgets.framework', 'Headers')
      os.makedirs(headers)
      folders = MacOS().getPrivateFolders(
          '/qt/include', qt, '6.12.0', 'QtWidgets')
    self.assertEqual(folders, (
        headers,
        os.path.join(headers, '6.12.0'),
        os.path.join(headers, '6.12.0', 'QtWidgets'),
        os.path.join(headers, '6.12.0', 'QtWidgets', 'private'),
    ))

  def test_private_folders_of_a_part_without_framework(self) -> None:
    """A part with no framework keeps them where every system does."""
    with tempfile.TemporaryDirectory() as qt:
      folders = MacOS().getPrivateFolders(
          '/qt/include', qt, '6.12.0', 'QtQmlIntegration')
    self.assertEqual(folders, System().getPrivateFolders(
        '/qt/include', qt, '6.12.0', 'QtQmlIntegration'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPENING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_shared_objects_are_opened_for_all(self) -> None:
    """Each shared object is opened with its names for every file after
    it; a static library is passed by."""
    with mock.patch.object(ctypes, 'CDLL') as opened:
      MacOS().prepareOpening(
          '/qt/QtCore.framework/Versions/A/QtCore', '/qt/libQt6AxServer.a')
    self.assertEqual(opened.call_args_list, [mock.call(
        '/qt/QtCore.framework/Versions/A/QtCore', mode=ctypes.RTLD_GLOBAL)])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A USUAL QT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_installer_then_homebrew(self) -> None:
    """The installer's folders come first, then Homebrew's on Apple
    silicon and on Intel; each only when it is there."""
    with tempfile.TemporaryDirectory() as root:
      installer = os.path.join(root, '6.12.0', 'macos')
      os.makedirs(os.path.join(installer, 'lib'))
      gone = os.path.join(root, '6.11.0', 'macos')
      there = {
          os.path.join(installer, 'lib'), '/opt/homebrew/opt/qt/lib'}
      with mock.patch.object(
          MacOS, '_findInstallerFolders',
          return_value=(installer, gone)) as finder, \
          mock.patch.object(
              os.path, 'isdir', side_effect=there.__contains__):
        folders = MacOS().getUsualQtFolders()
    finder.assert_called_once_with('macos', '~/Qt')
    self.assertEqual(folders, (
        os.path.join(installer, 'lib'), '/opt/homebrew/opt/qt/lib'))

  def test_no_usual_qt_at_all(self) -> None:
    """Nothing there: nothing given."""
    with mock.patch.object(
        MacOS, '_findInstallerFolders', return_value=()), \
        mock.patch.object(os.path, 'isdir', return_value=False):
      self.assertEqual(MacOS().getUsualQtFolders(), ())
