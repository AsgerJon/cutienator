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
    into and this machine has is where Qt keeps them; a part of header
    files alone has none."""
    paths = []
    for part in Rituals.getInstalledParts():
      name = System.getHere().getQtFileName(part)
      path = os.path.join(Build.getQtSharedObjectFolder(), name)
      if os.path.isfile(path):
        paths.append(path)
      else:
        header = os.path.join(Build.getQtHeaderFolder(), part)
        self.assertTrue(os.path.isdir(header), header)
    self.assertIn(os.path.join(
        Build.getQtSharedObjectFolder(),
        System.getHere().getQtFileName('QtCore')), paths)
    self.assertEqual(Rituals.getQtSharedObjects(), (*paths,))

  def test_a_part_this_machine_lacks_is_not_built(self) -> None:
    """The ritual files 'build' compiles are those of the parts this
    machine's Qt has, and only those."""
    installed = {*Rituals.getInstalledParts()}
    built = {*Rituals.getBuiltRitualFiles()}
    for ritualFile in Rituals.getRitualFiles():
      part = os.path.basename(os.path.dirname(ritualFile))[:-7]
      with self.subTest(ritualFile=ritualFile):
        self.assertIs(ritualFile in built, part in installed)

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
    """One command makes the precompiled header, one the object file
    of a ritual file, and one joins the object files. Each holds what
    this system is told."""
    system = System.getHere()
    build = Build()
    build.setRitualFiles(*Rituals.getPartRitualFiles('QtCore'))
    build.setTargetFile(Rituals.getTargetFile('QtCore'))
    build.setQtSharedObjects(*Rituals.getPartSharedObjects('QtCore'))
    qtFolder = Build.getQtSharedObjectFolder()
    ritualFile = build.getRitualFiles()[0]
    expected = (
        'clang++', '-std=c++17', '-O2', '-fno-access-control',
        *system.getCompilerFlags(qtFolder),
        '-I%s' % Build.getQtHeaderFolder(),
        '-fpch-instantiate-templates', '-x', 'c++-header',
        build.getCommonHeaderFile(),
        '-o', build.getPrecompiledHeaderFile(),
    )
    self.assertEqual(build.getPrecompileCommand(), expected)
    expected = (
        'clang++', '-std=c++17', '-O2', '-fno-access-control', '-c',
        *system.getCompilerFlags(qtFolder),
        '-I%s' % Build.getQtHeaderFolder(),
        '-include-pch', build.getPrecompiledHeaderFile(), ritualFile,
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
    self.assertEqual(
        build.getRitualFiles(), Rituals.getPartRitualFiles('QtCore'))
    self.assertTrue(build.getRitualFiles())

  def test_each_part_has_a_build_of_its_own(self) -> None:
    """The build of the target file of a part takes the ritual files of
    that part, and is joined to the shared object of that part of Qt
    first, so a function two parts of Qt offer by one name is taken
    from its own."""
    for partName in Rituals.getBuiltParts():
      build = Rituals.createPartBuild(partName)
      with self.subTest(partName=partName):
        self.assertEqual(
            build.getRitualFiles(), Rituals.getPartRitualFiles(partName))
        self.assertEqual(
            build.getTargetFile(), Rituals.getTargetFile(partName))
        self.assertEqual(
            build.getComponents(), Rituals.getPartComponents(partName))
        shared = build.getQtSharedObjects()
        own = os.path.join(
            Build.getQtSharedObjectFolder(),
            System.getHere().getQtFileName(partName))
        if os.path.isfile(own):
          self.assertEqual(shared[0], own)
        self.assertLessEqual({*Rituals.getQtSharedObjects()}, {*shared})

  def test_commands_need_what_they_are_made_of(self) -> None:
    """A build that was told nothing names what it is missing."""
    with self.assertRaises(MissingVariable):
      Build().getLinkCommand()
    with self.assertRaises(MissingVariable):
      Build().getCompileCommand('q_object.cpp')
    with self.assertRaises(MissingVariable):
      Build().getPrecompileCommand()
    with self.assertRaises(MissingVariable):
      Build().getCommonHeaderText()

  def test_an_object_file_is_named_after_its_ritual_file(self) -> None:
    """It lies in the folder 'demons' beside the target file, and for
    a ritual file of a part of Qt in the folder of that part there."""
    build = Build()
    build.setTargetFile(Rituals.getTargetFile('QtCore'))
    here = os.path.dirname(Rituals.getRitualFolder())
    folder = os.path.join(here, 'demons')
    self.assertEqual(build.getObjectFolder(), folder)
    ritualFile = os.path.join(
        Rituals.getPartFolder('QtCore'), 'q_object.cpp')
    self.assertEqual(
        build.getObjectFile(ritualFile),
        os.path.join(folder, 'QtCoreDemons', 'q_object.o'))
    self.assertEqual(
        os.path.basename(Rituals.getPartFolder('QtCore')), 'QtCoreRituals')
    self.assertEqual(
        os.path.dirname(Rituals.getTargetFile('QtCore')), here)
    self.assertEqual(
        build.getObjectFile(os.path.join('anywhere', 'q_object.cpp')),
        os.path.join(folder, 'q_object.o'),
    )

  def test_the_headers_lie_beside_the_object_files(self) -> None:
    """The common header and the precompiled header of it lie in the
    folder 'demons' beside the target file, named after the target
    file, since the builds of all the parts share that folder."""
    build = Build()
    build.setTargetFile(Rituals.getTargetFile('QtCore'))
    folder = build.getObjectFolder()
    self.assertEqual(
        build.getCommonHeaderFile(),
        os.path.join(folder, 'libcutienator_QtCore.common.h'))
    self.assertEqual(
        build.getPrecompiledHeaderFile(),
        os.path.join(folder, 'libcutienator_QtCore.common.pch'))
    self.assertEqual(
        build.getToldFile(),
        os.path.join(folder, 'libcutienator_QtCore.told.txt'))

  def test_the_common_header_of_the_package(self) -> None:
    """It holds each '#include' line of the ritual files once, the
    header of 'QObject' among them, and nothing else. A line taken
    along from Qt's source may name its file between quotes."""
    build = Build()
    build.setRitualFiles(*Rituals.getPartRitualFiles('QtCore'))
    lines = build.getCommonHeaderText().split('\n')
    self.assertEqual(lines.pop(), '')
    self.assertIn('#include <QtCore/qobject.h>', lines)
    self.assertEqual(len(lines), len({*lines}))
    for line in lines:
      self.assertTrue(line.startswith(('#include <', '#include "')), line)

  def test_a_long_command_goes_in_a_file(self) -> None:
    """A command of 'clang++' longer than Windows starts a program with
    is handed over in a file, and every word arrives as it was given:
    spaces, quotes and backslashes too."""
    words = ['-DCUTE_%d="a b\\c"' % i for i in range(1500)]
    self.assertGreater(sum(len(word) + 3 for word in words), 32767 - 5000)
    said = Build._run(
        'clang++', '-E', '-dM', '-x', 'c++', os.devnull, *words)
    lines = said.split('\n')
    self.assertIn('#define CUTE_7 "a b\\c"', lines)
    self.assertIn('#define CUTE_1499 "a b\\c"', lines)

  def test_a_program_not_installed_is_named(self) -> None:
    """Only a program that is not installed is said to be missing."""
    with self.assertRaises(FileNotFoundError) as caught:
      Build._run('no-such-program-of-cutienator', '-v')
    self.assertIn('no-such-program-of-cutienator', str(caught.exception))

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

  def _makeBuildWithHeaders(self) -> Build:
    """Gives a build as '_makeBuild' does, of two ritual files that
    name headers of C++ itself, one of them in both files."""
    build = self._makeBuild()
    one, two = build.getRitualFiles()
    with open(one, 'w') as file:
      file.write('#include <cstring>\n#include <cstdlib>\n')
      file.write('extern "C" int ritual_one() {\n')
      file.write('  return (int) std::strlen("one");\n}\n')
    with open(two, 'w') as file:
      file.write('#include <cstdlib>\n#include <climits>\n')
      file.write('extern "C" int ritual_two() {\n')
      file.write('  return std::abs(INT_MIN + 2);\n}\n')
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

  def test_the_common_header_names_each_header_once(self) -> None:
    """Every '#include' line of the ritual files, in the order they
    are first met, and a build of files naming none has an empty one."""
    build = self._makeBuildWithHeaders()
    expected = '#include <cstring>\n#include <cstdlib>\n#include <climits>\n'
    self.assertEqual(build.getCommonHeaderText(), expected)
    self.assertEqual(self._makeBuild().getCommonHeaderText(), '')

  def test_ritual_files_are_compiled_with_the_precompiled_header(
      self) -> None:
    """A build writes the common header and keeps it. The precompiled
    header is gone again when the build ends."""
    build = self._makeBuildWithHeaders()
    self.assertFalse(os.path.isfile(build.getCommonHeaderFile()))
    build.run()
    for ritualFile in build.getRitualFiles():
      self.assertTrue(os.path.isfile(build.getObjectFile(ritualFile)))
    with open(build.getCommonHeaderFile()) as file:
      self.assertEqual(file.read(), build.getCommonHeaderText())
    self.assertFalse(os.path.isfile(build.getPrecompiledHeaderFile()))
    with open(build.getToldFile()) as file:
      told = file.read()
    self.assertIn(' '.join(build.getPrecompileCommand()), told)

  def test_nothing_to_compile_needs_no_precompiled_header(self) -> None:
    """A build that has no ritual file to compile leaves the common
    header as it was and only joins the object files."""
    build = self._makeBuildWithHeaders()
    build.run()
    self._setBack(build.getCommonHeaderFile(), 100)
    written = os.path.getmtime(build.getCommonHeaderFile())
    build.run()
    self.assertEqual(
        os.path.getmtime(build.getCommonHeaderFile()), written)
    self.assertFalse(os.path.isfile(build.getPrecompiledHeaderFile()))

  def test_a_header_clang_refuses_names_the_common_header(self) -> None:
    """A ritual file naming a header that is nowhere stops the build
    before any ritual file is compiled. The refusal names the common
    header and the header that is missing."""
    build = self._makeBuildWithHeaders()
    one, two = build.getRitualFiles()
    with open(two, 'a') as file:
      file.write('#include <no_such_header_of_cutienator.h>\n')
    with self.assertRaises(RuntimeError) as context:
      build.run()
    self.assertIn(build.getCommonHeaderFile(), str(context.exception))
    self.assertIn('no_such_header_of_cutienator.h', str(context.exception))
    self.assertFalse(os.path.isfile(build.getPrecompiledHeaderFile()))
    self.assertFalse(os.path.isfile(build.getObjectFile(one)))
    self.assertFalse(os.path.isfile(build.getTargetFile()))

  def test_the_precompiled_header_is_gone_after_a_refusal(self) -> None:
    """When 'clang++' refuses a ritual file, the precompiled header
    is removed all the same."""
    build = self._makeBuildWithHeaders()
    one, two = build.getRitualFiles()
    with open(two, 'a') as file:
      file.write('this is no C++\n')
    with self.assertRaises(RuntimeError) as context:
      build.run()
    self.assertIn(two, str(context.exception))
    self.assertTrue(os.path.isfile(build.getObjectFile(one)))
    self.assertFalse(os.path.isfile(build.getPrecompiledHeaderFile()))

  def test_a_line_under_an_if_stays_with_its_ritual_file(self) -> None:
    """The common header takes no '#include' line that stands under an
    '#if': such a line is for some systems only."""
    build = self._makeBuildWithHeaders()
    one, two = build.getRitualFiles()
    with open(two, 'a') as file:
      file.write('#if defined(NO_SYSTEM_HAS_THIS)\n')
      file.write('#  include <no_such_header_of_cutienator.h>\n')
      file.write('#include <also_no_such_header.h>\n')
      file.write('#endif\n#include <cstdio>\n')
    text = build.getCommonHeaderText()
    self.assertNotIn('no_such_header', text)
    self.assertIn('#include <cstdio>', text)
    build.run()
    self.assertTrue(os.path.isfile(build.getObjectFile(two)))

  def test_the_folders_of_the_private_headers(self) -> None:
    """A build told the parts of Qt looks in the folders of the headers
    Qt calls private, and in the one of 'qplatformdefs.h'; a build
    told none looks in Qt's header folder alone."""
    build = Build()
    build.setTargetFile(Rituals.getTargetFile('QtCore'))
    self.assertEqual(build.getPrivateIncludeFolders(), ())
    build.setComponents(*Rituals.getRitualParts())
    folders = build.getPrivateIncludeFolders()
    self.assertTrue(folders)
    for folder in folders:
      self.assertTrue(os.path.isdir(folder), folder)
    self.assertTrue(
        os.path.isfile(os.path.join(folders[-1], 'qplatformdefs.h')))
    command = build.getCompileCommand('q_object.cpp')
    for folder in folders:
      self.assertIn('-I%s' % folder, command)
