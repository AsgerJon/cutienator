"""
TestBuild tests what 'Build' finds of Qt on this machine, the commands
it gives, and that it compiles each ritual file only when it has to,
on whichever system the tests run.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import shutil
import tempfile

from worktoy.waitaminute import MissingVariable, TypeException
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

  The tests under 'WHAT IS COMPILED' compile two ritual files made up
  for them, which pull in nothing of Qt, in a folder of their own that
  is removed again. No test here compiles the ritual files of the
  package. 'TestQObject' does, when the shared object of rituals is
  missing or older than a ritual file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IS FOUND  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_header_folder_holds_the_headers(self) -> None:
    """The header folder holds the header of 'QObject'."""
    header = os.path.join(Build.getQtHeaderFolder(), 'QtCore', 'qobject.h')
    self.assertTrue(os.path.isfile(header), header)

  def test_shared_object_folder_holds_what_system_names(self) -> None:
    """The file 'System' names for each part of Qt the rituals call
    into is where Qt keeps them."""
    paths = []
    for part in ('QtCore', 'QtGui', 'QtWidgets'):
      name = System.getHere().getQtFileName(part)
      path = os.path.join(Build.getQtSharedObjectFolder(), name)
      self.assertTrue(os.path.isfile(path), path)
      paths.append(path)
    self.assertEqual(Rituals.getQtSharedObjects(), (*paths,))

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

  def test_commands_are_put_together_from_what_the_system_says(self) -> None:
    """One command makes the object file of a ritual file, and one
    joins the object files. Both hold what this system is told."""
    system = System.getHere()
    build = Build()
    build.setRitualFiles(*Rituals.getRitualFiles())
    build.setTargetFile(Rituals.getTargetFile())
    build.setQtSharedObjects(*Rituals.getQtSharedObjects())
    qtFolder = Build.getQtSharedObjectFolder()
    ritualFile = build.getRitualFiles()[0]
    expected = (
        'clang++', '-std=c++17', '-O2', '-c',
        *system.getCompilerFlags(qtFolder),
        '-I%s' % Build.getQtHeaderFolder(), ritualFile,
        '-o', build.getObjectFile(ritualFile),
    )
    self.assertEqual(build.getCompileCommand(ritualFile), expected)
    expected = (
        'clang++', '-shared',
        *system.getCompilerFlags(qtFolder),
        *system.getLinkerFlags(qtFolder),
        *(build.getObjectFile(f) for f in build.getRitualFiles()),
        '-o', build.getTargetFile(),
        *build.getQtSharedObjects(),
    )
    self.assertEqual(build.getLinkCommand(), expected)
    self.assertEqual(build.getRitualFiles(), Rituals.getRitualFiles())
    self.assertTrue(build.getRitualFiles())

  def test_commands_need_what_they_are_made_of(self) -> None:
    """A build that was told nothing names what it is missing."""
    with self.assertRaises(MissingVariable):
      Build().getLinkCommand()
    with self.assertRaises(MissingVariable):
      Build().getCompileCommand('q_object.cpp')

  def test_an_object_file_is_named_after_its_ritual_file(self) -> None:
    """It lies in the folder 'objects' beside the target file."""
    build = Build()
    build.setTargetFile(Rituals.getTargetFile())
    folder = os.path.join(Rituals.getRitualFolder(), 'objects')
    self.assertEqual(build.getObjectFolder(), folder)
    self.assertEqual(
        build.getObjectFile(os.path.join('anywhere', 'q_object.cpp')),
        os.path.join(folder, 'q_object.o'),
    )

  def test_job_count(self) -> None:
    """As many at once as the machine has processors, or as told."""
    build = Build()
    self.assertEqual(build.getJobCount(), os.cpu_count() or 1)
    build.setJobCount(2)
    self.assertEqual(build.getJobCount(), 2)
    with self.assertRaises(ValueError):
      build.setJobCount(0)
    with self.assertRaises(TypeException):
      build.setJobCount('2')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IS COMPILED   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _makeBuild(self) -> Build:
    """Gives a build of two ritual files made up for the test, in a
    folder of its own, which is removed when the test ends."""
    folder = tempfile.mkdtemp(prefix='cutienator-test-build-')
    self.addCleanup(shutil.rmtree, folder, True)
    ritualFiles = []
    for name, number in (('one', 1), ('two', 2)):
      ritualFile = os.path.join(folder, '%s.cpp' % name)
      with open(ritualFile, 'w') as file:
        file.write('extern "C" int ritual_%s() { return %d; }\n' % (
            name, number))
      ritualFiles.append(ritualFile)
    build = Build()
    build.setRitualFiles(*ritualFiles)
    build.setTargetFile(os.path.join(folder, 'libmade_up.so'))
    build.setQtSharedObjects()
    return build

  @staticmethod
  def _setBack(path: str, seconds: int) -> None:
    """Makes a file look as if it was written that many seconds ago."""
    then = os.path.getmtime(path) - seconds
    os.utime(path, (then, then))

  def test_every_ritual_file_is_compiled_the_first_time(self) -> None:
    """A build that never ran has every ritual file to compile, and
    leaves an object file for each beside the target file."""
    build = self._makeBuild()
    self.assertEqual(build.getStaleRitualFiles(), build.getRitualFiles())
    self.assertEqual(build.run(), build.getTargetFile())
    self.assertTrue(os.path.isfile(build.getTargetFile()))
    for ritualFile in build.getRitualFiles():
      self.assertTrue(os.path.isfile(build.getObjectFile(ritualFile)))
    self.assertEqual(build.getStaleRitualFiles(), ())

  def test_only_what_changed_is_compiled_again(self) -> None:
    """After one ritual file changed, that one is compiled again and
    the object file of the other is left as it was."""
    build = self._makeBuild()
    build.run()
    one, two = build.getRitualFiles()
    for ritualFile in (one, two):
      self._setBack(build.getObjectFile(ritualFile), 100)
    self._setBack(one, 200)
    madeTwo = os.path.getmtime(build.getObjectFile(two))
    self.assertEqual(build.getStaleRitualFiles(), (two,))
    build.run()
    self.assertEqual(build.getStaleRitualFiles(), ())
    self.assertGreater(os.path.getmtime(build.getObjectFile(two)), madeTwo)
    madeOne = os.path.getmtime(build.getObjectFile(one))
    build.run()
    self.assertEqual(os.path.getmtime(build.getObjectFile(one)), madeOne)

  def test_another_qt_or_other_flags_compile_everything(self) -> None:
    """When what the object files were made with is not what the build
    has now, every ritual file is compiled again."""
    build = self._makeBuild()
    build.run()
    with open(build.getToldFile(), 'w') as file:
      file.write('Qt 0.0.0\n')
    self.assertEqual(build.getStaleRitualFiles(), build.getRitualFiles())
    build.run()
    with open(build.getToldFile()) as file:
      self.assertEqual(file.read(), build.getToldText())

  def test_a_ritual_file_clang_refuses_is_named(self) -> None:
    """The refusal names the ritual file, and the other one keeps its
    object file."""
    build = self._makeBuild()
    one, two = build.getRitualFiles()
    with open(two, 'w') as file:
      file.write('this is no C++\n')
    with self.assertRaises(RuntimeError) as context:
      build.run()
    self.assertIn(two, str(context.exception))
    self.assertTrue(os.path.isfile(build.getObjectFile(one)))
    self.assertFalse(os.path.isfile(build.getTargetFile()))
