"""
TestBuild tests what 'Build' finds of Qt on this machine, and the
command it gives, on whichever system the tests run.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os

from worktoy.waitaminute import MissingVariable
from worktoy.work_test import BaseTest

from cutienator.occult import Build, Rituals, System


class TestBuild(BaseTest):
  """
  Tests 'Build' against the Qt that is installed. Nothing is faked: the
  folders are asked of Qt's own 'qmake6', and the files are looked for
  where 'System' says they are on the system the tests run on. So on
  each system this also tests that 'System' names Qt's files rightly
  there.

  What to know before adding a test
  ---------------------------------

  No test here compiles. 'TestQObject' does, when the shared object of
  rituals is missing or older than a ritual file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IS FOUND  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_header_folder_holds_the_headers(self) -> None:
    """The header folder holds the header of 'QObject'."""
    header = os.path.join(Build.getQtHeaderFolder(), 'QtCore', 'qobject.h')
    self.assertTrue(os.path.isfile(header), header)

  def test_shared_object_folder_holds_what_system_names(self) -> None:
    """The file 'System' names for 'QtCore' is where Qt keeps them."""
    name = System.getHere().getQtFileName('QtCore')
    path = os.path.join(Build.getQtSharedObjectFolder(), name)
    self.assertTrue(os.path.isfile(path), path)
    self.assertEqual(
        Rituals.getQtSharedObjects(), (path,),
    )

  def test_program_folder_holds_qmake(self) -> None:
    """The program folder holds 'qmake6', which answered for it."""
    folder = Build.getQtProgramFolder()
    names = ('qmake6', 'qmake6.exe')
    found = [n for n in names if os.path.isfile(os.path.join(folder, n))]
    self.assertTrue(found, folder)

  def test_folders_are_kept(self) -> None:
    """Each folder is asked for once and then kept on the class."""
    self.assertIs(Build.getQtHeaderFolder(), Build().getQtHeaderFolder())
    self.assertIs(
        Build.getQtSharedObjectFolder(), Build().getQtSharedObjectFolder(),
    )
    self.assertIs(Build.getQtProgramFolder(), Build().getQtProgramFolder())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE COMMAND  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_command_is_put_together_from_what_the_system_says(self) -> None:
    """The command holds what every system and what this one is told."""
    system = System.getHere()
    build = Build()
    build.setRitualFiles(*Rituals.getRitualFiles())
    build.setTargetFile(Rituals.getTargetFile())
    build.setQtSharedObjects(*Rituals.getQtSharedObjects())
    qtFolder = Build.getQtSharedObjectFolder()
    expected = (
        'clang++', '-std=c++17', '-shared', '-O2',
        *system.getCompilerFlags(qtFolder),
        *system.getLinkerFlags(qtFolder),
        '-I%s' % Build.getQtHeaderFolder(),
        *build.getRitualFiles(),
        '-o', build.getTargetFile(),
        *build.getQtSharedObjects(),
    )
    self.assertEqual(build.getCommand(), expected)
    self.assertEqual(len(build.getRitualFiles()), 3)

  def test_command_needs_all_three(self) -> None:
    """A build that was told nothing names what it is missing."""
    with self.assertRaises(MissingVariable):
      Build().getCommand()
