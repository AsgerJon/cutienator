"""
TestOccultSystem tests 'System', which says what differs from one
operating system to the next, apart from its three subclasses.
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

from cutienator.occult import System, Linux, MacOS, Windows

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict


class TestOccultSystem(BaseTest):
  """
  Tests 'System': which subclass answers for the system Python runs on,
  the questions only a subclass answers, and what 'System' itself reads
  for every system: the '.prl' files of Qt, the folders of its headers
  and the folders Qt's installer puts a Qt into.

  What to know before adding a test
  ---------------------------------

  - 'System.getHere()' keeps its answer for the whole program. A test
    that makes it answer anew puts the kept answer back before it ends,
    through '_keepHere'.
  - The '.prl' files and the folders of an installer are made in a
    temporary folder for each test, so nothing of a real Qt is read.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _keepHere(self) -> None:
    """Puts the kept answer of 'getHere' back when the test ends."""
    kept = System.__system_here__
    self.addCleanup(setattr, System, '__system_here__', kept)

  @staticmethod
  def _writePrl(folder: str, part: str, lines: Dict[str, str]) -> None:
    """Writes the '.prl' file of a part as Linux names it, into
    'folder', one 'KEY = value' line for each entry."""
    path = os.path.join(folder, Linux().getQtPrlFileName(part))
    with open(path, 'w', encoding='utf-8') as file:
      for key, value in lines.items():
        file.write('%s = %s\n' % (key, value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHICH SYSTEM   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_three_systems_are_known(self) -> None:
    """'System' has the three subclasses, each with its platform name."""
    named = {s.__platform_name__: s for s in System.__subclasses__()}
    self.assertEqual(named, dict(linux=Linux, darwin=MacOS, win32=Windows))
    self.assertIsNone(System.__platform_name__)

  def test_here_is_the_system_python_runs_on(self) -> None:
    """'getHere' gives an object of the subclass of this platform."""
    self._keepHere()
    System.__system_here__ = None
    here = System.getHere()
    self.assertIsInstance(here, System)
    self.assertEqual(type(here).__platform_name__, sys.platform)

  def test_here_is_kept(self) -> None:
    """'getHere' gives the same object each time."""
    self._keepHere()
    System.__system_here__ = None
    first = System.getHere()
    self.assertIs(System.getHere(), first)
    self.assertIs(Windows.getHere(), first)

  def test_each_system_platform_gives_its_class(self) -> None:
    """On each of the three platforms, its own subclass answers."""
    self._keepHere()
    for platform, system in (
        ('linux', Linux), ('darwin', MacOS), ('win32', Windows)):
      with self.subTest(platform=platform):
        System.__system_here__ = None
        with mock.patch.object(sys, 'platform', platform):
          self.assertIs(type(System.getHere()), system)

  def test_a_platform_of_no_subclass_is_refused(self) -> None:
    """A platform no subclass is written for raises, naming it."""
    self._keepHere()
    System.__system_here__ = None
    with mock.patch.object(sys, 'platform', 'sunos5'):
      with self.assertRaises(NotImplementedError) as caught:
        System.getHere()
    self.assertIn("'sunos5'", str(caught.exception))
    self.assertIsNone(System.__system_here__)

  def test_here_raises_when_making_it_leaves_nothing(self) -> None:
    """When making the object leaves none, 'getHere' does not loop."""
    self._keepHere()
    System.__system_here__ = None
    with mock.patch.object(System, '_createHere'):
      with self.assertRaises(RecursionError):
        System.getHere()

  def test_str_and_repr_name_the_class(self) -> None:
    """'str' and 'repr' give the name of the class in angle brackets."""
    for system in (System(), Linux(), MacOS(), Windows()):
      with self.subTest(system=type(system).__name__):
        self.assertEqual(str(system), '<%s>' % type(system).__name__)
        self.assertEqual(repr(system), str(system))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ONLY A SUBCLASS ANSWERS  # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_each_question_of_a_subclass_is_refused_here(self) -> None:
    """Each question asked of 'System' itself raises, naming it."""
    system = System()
    asked = dict(
        getQtFileName=('QtCore',), getQtStaticFileName=('QtCore',),
        getQtPrlFileName=('QtCore',), getCompilerFlags=('/qt',),
        getLinkerFlags=('/qt',), buildsObjectiveC=(),
        prepareOpening=('/qt/libQt6Core.so.6',), getUsualQtFolders=(),
    )
    for name, args in asked.items():
      with self.subTest(name=name):
        with self.assertRaises(NotImplementedError) as caught:
          getattr(system, name)(*args)
        self.assertIn("'System.%s'" % name, str(caught.exception))
        self.assertIn('System.getHere()', str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PRL FILES  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_missing_prl_file_reads_as_nothing(self) -> None:
    """A part with no '.prl' file has no lines, and is no static
    library, and needs nothing beside it."""
    with tempfile.TemporaryDirectory() as folder:
      linux = Linux()
      self.assertEqual(linux._readPrlFile(folder, 'QtCore'), {})
      self.assertIs(linux.isQtStaticLibrary(folder, 'QtCore'), False)
      self.assertEqual(linux.readStaticDependencies(folder, 'QtCore'), ())

  def test_each_line_of_a_prl_file_is_read(self) -> None:
    """Each line is read as its key and its value, spaces taken away;
    a line with no '=' is a key with nothing."""
    with tempfile.TemporaryDirectory() as folder:
      self._writePrl(folder, 'QtCore', dict(
          QMAKE_PRL_TARGET='libQt6Core.so', QMAKE_PRL_CONFIG='shared'))
      path = os.path.join(folder, 'libQt6Core.prl')
      with open(path, 'a', encoding='utf-8') as file:
        file.write('ALONE\n')
      self.assertEqual(Linux()._readPrlFile(folder, 'QtCore'), dict(
          QMAKE_PRL_TARGET='libQt6Core.so', QMAKE_PRL_CONFIG='shared',
          ALONE=''))

  def test_a_shared_part_is_no_static_library(self) -> None:
    """A part whose config does not say 'static' needs nothing beside."""
    with tempfile.TemporaryDirectory() as folder:
      self._writePrl(folder, 'QtCore', dict(
          QMAKE_PRL_CONFIG='shared release', QMAKE_PRL_LIBS='-lm'))
      linux = Linux()
      self.assertIs(linux.isQtStaticLibrary(folder, 'QtCore'), False)
      self.assertEqual(linux.readStaticDependencies(folder, 'QtCore'), ())

  def test_a_prl_file_without_config_is_no_static_library(self) -> None:
    """A '.prl' file naming no config says the part is not static."""
    with tempfile.TemporaryDirectory() as folder:
      self._writePrl(folder, 'QtCore', dict(QMAKE_PRL_LIBS='-lm'))
      self.assertIs(Linux().isQtStaticLibrary(folder, 'QtCore'), False)

  def test_a_static_part_lists_what_it_needs(self) -> None:
    """A static part gives the words of its libraries, with Qt's folder
    where the file writes '$$[QT_INSTALL_LIBS]'."""
    with tempfile.TemporaryDirectory() as folder:
      self._writePrl(folder, 'QtAxServer', dict(
          QMAKE_PRL_CONFIG='static release',
          QMAKE_PRL_LIBS='$$[QT_INSTALL_LIBS]/libQt6Widgets.so -lole32'))
      linux = Linux()
      self.assertIs(linux.isQtStaticLibrary(folder, 'QtAxServer'), True)
      self.assertEqual(
          linux.readStaticDependencies(folder, 'QtAxServer'),
          ('%s/libQt6Widgets.so' % folder, '-lole32'))

  def test_a_static_part_without_libraries_needs_nothing(self) -> None:
    """A static part whose file lists no libraries needs nothing."""
    with tempfile.TemporaryDirectory() as folder:
      self._writePrl(folder, 'QtAxServer', dict(QMAKE_PRL_CONFIG='static'))
      self.assertEqual(
          Linux().readStaticDependencies(folder, 'QtAxServer'), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FOLDERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_private_folders_of_a_part(self) -> None:
    """The four folders of a part's private headers, in Qt's layout."""
    folders = System().getPrivateFolders(
        '/qt/include', '/qt/lib', '6.12.0', 'QtWidgets')
    self.assertEqual(folders, (
        os.path.join('/qt/include', 'QtWidgets'),
        os.path.join('/qt/include', 'QtWidgets', '6.12.0'),
        os.path.join('/qt/include', 'QtWidgets', '6.12.0', 'QtWidgets'),
        os.path.join(
            '/qt/include', 'QtWidgets', '6.12.0', 'QtWidgets', 'private'),
    ))

  def test_installer_folders_newest_first(self) -> None:
    """Each version folder holding the kit is found, the newest first;
    a name that is no version, and a version without the kit, are
    passed by."""
    with tempfile.TemporaryDirectory() as root:
      for name in ('6.9.3', '6.12.0', '6.10.1'):
        os.makedirs(os.path.join(root, name, 'gcc_64'))
      os.makedirs(os.path.join(root, '6.11.0', 'macos'))
      os.makedirs(os.path.join(root, 'Tools', 'gcc_64'))
      found = System._findInstallerFolders('gcc_64', root)
    self.assertEqual(found, (
        os.path.join(root, '6.12.0', 'gcc_64'),
        os.path.join(root, '6.10.1', 'gcc_64'),
        os.path.join(root, '6.9.3', 'gcc_64'),
    ))

  def test_installer_folders_of_each_root_in_turn(self) -> None:
    """The roots are looked in in the order given; one that is not
    there gives nothing."""
    with tempfile.TemporaryDirectory() as first:
      with tempfile.TemporaryDirectory() as second:
        os.makedirs(os.path.join(first, '6.12.0', 'gcc_64'))
        os.makedirs(os.path.join(second, '6.13.0', 'gcc_64'))
        missing = os.path.join(first, 'not-there')
        found = System._findInstallerFolders(
            'gcc_64', missing, first, second)
    self.assertEqual(found, (
        os.path.join(first, '6.12.0', 'gcc_64'),
        os.path.join(second, '6.13.0', 'gcc_64'),
    ))

  def test_installer_folders_expand_the_home_folder(self) -> None:
    """A root starting with '~' is looked for in the home folder."""
    with tempfile.TemporaryDirectory() as home:
      os.makedirs(os.path.join(home, 'Qt', '6.12.0', 'gcc_64'))
      with mock.patch.dict(os.environ, HOME=home):
        found = System._findInstallerFolders('gcc_64', '~/Qt')
    self.assertEqual(found, (os.path.join(home, 'Qt', '6.12.0', 'gcc_64'),))
