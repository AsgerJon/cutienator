"""
TestOccultSummon tests the rules of 'Summon', which compiles ritual
files into one shared object, each rule on its own: the programs it
runs and what it asks 'qmake6', what it is told, the files it names and
the commands it gives, and each round of leaving out what is refused.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
import types
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.occult import Exorcist, Linux, Summon, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List

#  The class-level answers of 'qmake6' that 'Summon' keeps.
_KEPT = (
  '__qt_header_folder__', '__qt_shared_object_folder__', '__qt_version__',
  '__qt_program_folder__', '__qt_module_folder__',
)

#  A ritual file of one ritual, and one of two, made up for the tests.
_ONE = (
  '#include <QtCore/qglobal.h>\n'
  '\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_one() {\n'
  '  return 1;\n'
  '}\n'
)
_TWO = (
  '#include <QtCore/qglobal.h>\n'
  '\n'
  '//  int fine()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_fine() {\n'
  '  return 1;\n'
  '}\n'
  '\n'
  '//  int broken()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_broken() {\n'
  '  return 2;\n'
  '}\n'
)


class TestOccultSummon(BaseTest):
  """
  Tests each rule of 'Summon' apart from a real build.

  What to know before adding a test
  ---------------------------------

  - Every test starts with the answers of 'qmake6' set by hand, in
    'setUp': Qt in a temporary folder, version '6.12.0', and 'Linux' as
    the system, so the commands are the same on every machine; nothing
    here asks the Qt of the machine. A test of how an answer is asked
    for puts it back to None for itself.
  - Where 'Summon' would run 'clang++', the test replaces '_run' or
    '_compileCopy' and says what the program printed. The real builds
    are 'TestOccultSummonBuild'.
  - Files are made in the temporary folder of the test, removed when it
    ends.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SET UP   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setUp(self) -> None:
    """A folder for the test, the answers of 'qmake6' set to a made-up
    Qt in it, and 'Linux' as the system."""
    super().setUp()
    self.folder = tempfile.mkdtemp()
    self.addCleanup(shutil.rmtree, self.folder)
    self.qt = os.path.join(self.folder, 'qt')
    for name in ('include', 'lib', 'bin'):
      os.makedirs(os.path.join(self.qt, name))
    answers = dict(
        __qt_header_folder__=os.path.join(self.qt, 'include'),
        __qt_shared_object_folder__=os.path.join(self.qt, 'lib'),
        __qt_version__='6.12.0',
        __qt_program_folder__=os.path.join(self.qt, 'bin'),
        __qt_module_folder__=os.path.join(self.qt, 'modules'),
    )
    for name, value in answers.items():
      patcher = mock.patch.object(Summon, name, value)
      patcher.start()
      self.addCleanup(patcher.stop)
    patcher = mock.patch.object(System, '__system_here__', Linux())
    patcher.start()
    self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _write(self, relative: str, text: str) -> str:
    """Writes a file at a path inside the folder of the test."""
    path = os.path.join(self.folder, relative)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
      file.write(text)
    return path

  def _build(self, *texts: str) -> Summon:
    """A build of ritual files of these texts, in 'QtCutieRituals', into
    'libcutienator_QtCutie.so', calling into a made-up QtCore."""
    files = [self._write('QtCutieRituals/q_cutie_%d.cpp' % n, text)
             for n, text in enumerate(texts)]
    core = self._write('qt/lib/libQt6Core.so.6', '')
    build = Summon()
    build.setRitualFiles(*files)
    build.setTargetFile(
        os.path.join(self.folder, 'libcutienator_QtCutie.so'))
    build.setQtSharedObjects(core)
    return build

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  RUNNING A PROGRAM  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_program_gives_what_it_printed(self) -> None:
    """What the program prints comes back."""
    self.assertEqual(Summon._run('echo', 'cute'), 'cute\n')

  def test_a_program_not_installed_is_named(self) -> None:
    """A program that is not installed raises before anything runs."""
    with mock.patch.object(subprocess, 'run') as run:
      with self.assertRaises(FileNotFoundError) as caught:
        Summon._run('no-such-program-of-cutienator', '-v')
    run.assert_not_called()
    self.assertIn("'no-such-program-of-cutienator'", str(caught.exception))

  def test_a_program_that_fails_says_why(self) -> None:
    """A program ending with an error raises with what it said."""
    with self.assertRaises(RuntimeError) as caught:
      Summon._run('sh', '-c', 'echo broken >&2; exit 2')
    self.assertIn("'sh' failed: broken", str(caught.exception))

  def test_a_program_the_system_will_not_start(self) -> None:
    """When the system refuses to start a program, it is said why."""
    with mock.patch.object(
        subprocess, 'run', side_effect=OSError('too long')):
      with self.assertRaises(RuntimeError) as caught:
        Summon._run('sh', '-c', 'true')
    self.assertIn("did not start the program 'sh': too long",
                  str(caught.exception))

  def test_a_long_command_of_clang_on_windows(self) -> None:
    """On Windows a command of 'clang++' too long for one line hands its
    words in a file of its own, each quoted, backslashes and quotes
    escaped, and the file goes when it is done."""
    seen = dict()  # type: Dict[str, Any]

    def fakeRun(command: Any, **kwargs: Any) -> Any:
      seen['command'] = command
      path = command[2][1:]
      with open(path, encoding='utf-8') as file:
        seen['words'] = file.read()
      seen['path'] = path
      return types.SimpleNamespace(returncode=0, stdout='made', stderr='')

    long = 'x' * 9000
    with mock.patch.object(os, 'name', 'nt'), \
        mock.patch.object(subprocess, 'run', side_effect=fakeRun):
      said = Summon._run('clang++', long, 'C:\\Qt\\"a"')
    self.assertEqual(said, 'made')
    self.assertEqual(seen['command'][:2], ('clang++', '--rsp-quoting=posix'))
    self.assertTrue(seen['command'][2].startswith('@'))
    self.assertEqual(
        seen['words'], '"%s"\n"C:\\\\Qt\\\\\\"a\\""\n' % long)
    self.assertFalse(os.path.exists(seen['path']))

  def test_a_long_command_otherwise_is_run_as_it_is(self) -> None:
    """A long command of another program, or on another system, is run
    as it is."""
    long = 'x' * 9000
    done = types.SimpleNamespace(returncode=0, stdout='', stderr='')
    for name, program in (('nt', 'sh'), ('posix', 'clang++')):
      with self.subTest(name=name, program=program):
        with mock.patch.object(os, 'name', name), mock.patch.object(
            subprocess, 'run', return_value=done) as run:
          Summon._run(program, long)
        self.assertEqual(run.call_args[0][0], (program, long))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT QMAKE SAYS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_each_answer_is_asked_of_qmake_once(self) -> None:
    """Each folder and the version are asked of 'qmake6', spaces taken
    away, and kept: a second call asks nothing."""
    asked = (
        ('getQtHeaderFolder', '__qt_header_folder__', 'QT_INSTALL_HEADERS'),
        ('getQtSharedObjectFolder', '__qt_shared_object_folder__',
         'QT_INSTALL_LIBS'),
        ('getQtVersion', '__qt_version__', 'QT_VERSION'),
        ('getQtProgramFolder', '__qt_program_folder__', 'QT_INSTALL_BINS'),
    )
    for getter, name, key in asked:
      with self.subTest(getter=getter):
        with mock.patch.object(Summon, name, None), mock.patch.object(
            Summon, '_run', return_value='  answer of %s\n' % key) as run:
          self.assertEqual(getattr(Summon, getter)(), 'answer of %s' % key)
          self.assertEqual(getattr(Summon, getter)(), 'answer of %s' % key)
        run.assert_called_once_with('qmake6', '-query', key)

  def test_an_answer_never_made_does_not_loop(self) -> None:
    """When asking leaves no answer, the getter raises, not loops."""
    for getter, name, maker in (
        ('getQtHeaderFolder', '__qt_header_folder__',
         '_createQtHeaderFolder'),
        ('getQtSharedObjectFolder', '__qt_shared_object_folder__',
         '_createQtSharedObjectFolder'),
        ('getQtVersion', '__qt_version__', '_createQtVersion'),
        ('getQtProgramFolder', '__qt_program_folder__',
         '_createQtProgramFolder'),
        ('getQtModuleFolder', '__qt_module_folder__',
         '_createQtModuleFolder'),
    ):
      with self.subTest(getter=getter):
        with mock.patch.object(Summon, name, None), \
            mock.patch.object(Summon, maker):
          with self.assertRaises(RecursionError):
            getattr(Summon, getter)()

  def test_qt_found_without_qmake(self) -> None:
    """Without 'qmake6', Qt's shared objects are found in the first
    usual folder holding QtCore."""
    empty = os.path.join(self.folder, 'empty')
    holding = os.path.join(self.folder, 'holding')
    for folder in (empty, holding):
      os.makedirs(folder)
    open(os.path.join(holding, 'libQt6Core.so.6'), 'w').close()
    with mock.patch.object(Summon, '__qt_shared_object_folder__', None), \
        mock.patch.object(Summon, '_run', side_effect=FileNotFoundError), \
        mock.patch.object(
            Linux, 'getUsualQtFolders', return_value=(empty, holding)):
      self.assertEqual(Summon.getQtSharedObjectFolder(), holding)

  def test_no_qt_found_without_qmake(self) -> None:
    """Without 'qmake6' and with no usual folder holding QtCore, it says
    where it looked, or that no usual folder is there."""
    empty = os.path.join(self.folder, 'empty')
    os.makedirs(empty)
    for folders, said in (((empty,), empty), ((), 'none is there')):
      with self.subTest(folders=folders):
        with mock.patch.object(
            Summon, '__qt_shared_object_folder__', None), \
            mock.patch.object(
                Summon, '_run', side_effect=FileNotFoundError), \
            mock.patch.object(
                Linux, 'getUsualQtFolders', return_value=folders):
          with self.assertRaises(FileNotFoundError) as caught:
            Summon.getQtSharedObjectFolder()
        self.assertIn("'libQt6Core.so.6'", str(caught.exception))
        self.assertIn(said, str(caught.exception))

  def test_programs_beside_the_shared_objects_without_qmake(self) -> None:
    """Without 'qmake6', Qt's programs are in 'bin' beside its 'lib'."""
    with mock.patch.object(Summon, '__qt_program_folder__', None), \
        mock.patch.object(Summon, '_run', side_effect=FileNotFoundError):
      self.assertEqual(
          Summon.getQtProgramFolder(), os.path.join(self.qt, 'bin'))

  def test_the_folder_of_the_modules(self) -> None:
    """The folder of what Qt knows of its parts is 'mkspecs/modules' of
    its host data, when it is there."""
    modules = os.path.join(self.qt, 'mkspecs', 'modules')
    os.makedirs(modules)
    with mock.patch.object(Summon, '__qt_module_folder__', None), \
        mock.patch.object(Summon, '_run', return_value=self.qt + '\n'):
      self.assertEqual(Summon.getQtModuleFolder(), modules)

  def test_a_missing_folder_of_the_modules(self) -> None:
    """A Qt with no such folder is refused, naming it."""
    with mock.patch.object(Summon, '__qt_module_folder__', None), \
        mock.patch.object(Summon, '_run', return_value=self.qt):
      with self.assertRaises(FileNotFoundError) as caught:
        Summon.getQtModuleFolder()
    self.assertIn(os.path.join(self.qt, 'mkspecs', 'modules'),
                  str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT IS TOLD  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_nothing_told_is_refused_when_asked(self) -> None:
    """The ritual files and the target file must be told before asked."""
    build = Summon()
    for ask in (build.getRitualFiles, build.getTargetFile):
      with self.subTest(ask=ask):
        with self.assertRaises(MissingVariable):
          ask()

  def test_the_ritual_files(self) -> None:
    """Each file is taken as its full path, in order."""
    first = self._write('QtCutieRituals/a.cpp', _ONE)
    second = self._write('QtCutieRituals/b.cpp', _ONE)
    build = Summon()
    relative = os.path.relpath(second)
    build.setRitualFiles(first, relative)
    self.assertEqual(build.getRitualFiles(), (first, second))

  def test_the_ritual_files_refused(self) -> None:
    """None at all, one that is no 'str', and one not there, are
    refused."""
    build = Summon()
    with self.assertRaises(ValueError):
      build.setRitualFiles()
    with self.assertRaises(TypeException):
      build.setRitualFiles(self._write('a.cpp', _ONE), 7)
    with self.assertRaises(FileNotFoundError) as caught:
      build.setRitualFiles('/no/such/ritual.cpp')
    self.assertIn("'/no/such/ritual.cpp'", str(caught.exception))

  def test_the_target_file(self) -> None:
    """The target file is taken as its full path, in a folder that is
    there; one that is no 'str', or in no folder, is refused."""
    build = Summon()
    target = os.path.join(self.folder, 'libcutienator_QtCutie.so')
    build.setTargetFile(target)
    self.assertEqual(build.getTargetFile(), target)
    with self.assertRaises(TypeException):
      build.setTargetFile(b'/x.so')
    with self.assertRaises(FileNotFoundError):
      build.setTargetFile('/no/such/folder/libcutie.so')

  def test_the_shared_objects_of_qt(self) -> None:
    """Each shared object is taken as its full path; none told is none;
    one that is no 'str', or not there, is refused."""
    build = Summon()
    self.assertEqual(build.getQtSharedObjects(), ())
    core = self._write('qt/lib/libQt6Core.so.6', '')
    build.setQtSharedObjects(core)
    self.assertEqual(build.getQtSharedObjects(), (core,))
    with self.assertRaises(TypeException):
      build.setQtSharedObjects(3)
    with self.assertRaises(FileNotFoundError):
      build.setQtSharedObjects('/no/such/libQt6Core.so.6')

  def test_shared_objects_never_set_do_not_loop(self) -> None:
    """When setting them leaves none, the getter raises, not loops."""
    build = Summon()
    with mock.patch.object(Summon, 'setQtSharedObjects'):
      with self.assertRaises(RecursionError):
        build.getQtSharedObjects()

  def test_the_static_dependencies(self) -> None:
    """The words beside a static library of Qt, none to begin with; one
    that is no 'str' is refused."""
    build = Summon()
    self.assertEqual(build.getStaticDependencies(), ())
    build.setStaticDependencies('-lole32', '/qt/lib/Qt6Widgets.lib')
    self.assertEqual(build.getStaticDependencies(),
                     ('-lole32', '/qt/lib/Qt6Widgets.lib'))
    with self.assertRaises(TypeException):
      build.setStaticDependencies(None)

  def test_the_job_count(self) -> None:
    """As many jobs as processors, or as told; a count that is no
    'int', a 'bool', or below one, is refused."""
    build = Summon()
    self.assertEqual(build.getJobCount(), os.cpu_count() or 1)
    build.setJobCount(3)
    self.assertEqual(build.getJobCount(), 3)
    for count in ('3', 2.0, True):
      with self.subTest(count=count):
        with self.assertRaises(TypeException):
          build.setJobCount(count)
    with self.assertRaises(ValueError):
      build.setJobCount(0)

  def test_one_job_when_the_count_of_processors_is_unknown(self) -> None:
    """A machine that does not say how many processors it has gets one
    job, and one program at a time."""
    with mock.patch.object(os, 'cpu_count', return_value=None):
      self.assertEqual(Summon().getJobCount(), 1)

  def test_the_components(self) -> None:
    """The parts of Qt of the ritual files, none to begin with; one
    that is no 'str' is refused; telling them anew forgets the folders
    they gave."""
    build = Summon()
    self.assertEqual(build.getComponents(), ())
    build.__private_include_folders__ = ('/old',)
    build.setComponents('QtCore', 'QtGui')
    self.assertEqual(build.getComponents(), ('QtCore', 'QtGui'))
    self.assertIsNone(build.__private_include_folders__)
    with self.assertRaises(TypeException):
      build.setComponents(1)

  def test_str_says_what_is_missing_or_made(self) -> None:
    """'str' names the setters still to call, or what is made."""
    build = Summon()
    self.assertEqual(str(build), '<Summon still waiting for: '
                     'setRitualFiles, setTargetFile, setQtSharedObjects>')
    build = self._build(_ONE, _TWO)
    said = "<Summon of 2 ritual files into '%s'>" % build.getTargetFile()
    self.assertEqual(str(build), said)
    self.assertEqual(repr(build), said)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE FILES IT NAMES   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_files_of_a_build(self) -> None:
    """The object folder beside the target file, and the common header,
    its precompiled header, the told file and the left-out file named
    after the target file."""
    build = self._build(_ONE)
    demons = os.path.join(self.folder, 'demons')
    self.assertEqual(build.getObjectFolder(), demons)
    for getter, name in (
        ('getCommonHeaderFile', 'libcutienator_QtCutie.common.h'),
        ('getPrecompiledHeaderFile', 'libcutienator_QtCutie.common.pch'),
        ('getToldFile', 'libcutienator_QtCutie.told.txt'),
    ):
      with self.subTest(getter=getter):
        self.assertEqual(getattr(build, getter)(),
                         os.path.join(demons, name))
    self.assertEqual(build.getLeftOutFile(), os.path.join(
        self.folder, 'libcutienator_QtCutie.left_out.json'))
    self.assertEqual(Summon.getLeftOutFileOf('/a/libx.dll'),
                     '/a/libx.left_out.json')

  def test_the_object_file_of_a_ritual_file(self) -> None:
    """A ritual file of a part's folder has its object file in that
    part's folder of demons; any other, in the object folder itself."""
    build = self._build(_ONE)
    demons = os.path.join(self.folder, 'demons')
    for ritualFile, objectFile in (
        ('/r/QtCoreRituals/q_object.cpp',
         os.path.join(demons, 'QtCoreDemons', 'q_object.o')),
        ('/r/QtCoreRituals/q_mac__objc.mm',
         os.path.join(demons, 'QtCoreDemons', 'q_mac__objc.o')),
        ('/r/Rituals/q_object.cpp', os.path.join(demons, 'q_object.o')),
        ('/r/elsewhere/q_object.cpp', os.path.join(demons, 'q_object.o')),
    ):
      with self.subTest(ritualFile=ritualFile):
        self.assertEqual(build.getObjectFile(ritualFile), objectFile)

  def test_the_copy_of_a_ritual_file(self) -> None:
    """The copy without what is dropped lies beside its object file,
    with the ending of the ritual file."""
    build = self._build(_ONE)
    demons = os.path.join(self.folder, 'demons', 'QtCoreDemons')
    self.assertEqual(
        build.getExorcisedFile('/r/QtCoreRituals/q_object.cpp'),
        os.path.join(demons, 'q_object.exorcised.cpp'))
    self.assertEqual(
        build.getExorcisedFile('/r/QtCoreRituals/q_mac__objc.mm'),
        os.path.join(demons, 'q_mac__objc.exorcised.mm'))

  def test_the_name_of_a_ritual_file_in_the_record(self) -> None:
    """A ritual file is named in the record by its folder and its name."""
    self.assertEqual(
        Summon._getRecordKey('/a/b/QtCoreRituals/q_object.cpp'),
        'QtCoreRituals/q_object.cpp')
    self.assertEqual(
        Summon._getRecordKey('/a/b/QtCoreRituals/../QtCoreRituals/x.cpp'),
        'QtCoreRituals/x.cpp')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT READS OF THE RITUAL FILES  # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_common_header(self) -> None:
    """Every '#include' line of the ritual files outside an '#if', once,
    in the order first seen."""
    first = '\n'.join((
        '#include <QtCore/qglobal.h>',
        '  #  include <QtCore/qstring.h>',
        '#if QT_CONFIG(cutie)',
        '#include <QtCore/qcutie.h>',
        '#ifdef Q_OS_WIN',
        '#include <windows.h>',
        '#endif',
        '#include <QtCore/qcutie2.h>',
        '#endif',
        '#define X 1',
        '#include <QtCore/qlist.h>',
        'int x;',
    ))
    second = '#include <QtCore/qglobal.h>\n#include <QtGui/qcolor.h>\n'
    build = self._build(first, second)
    self.assertEqual(build.getCommonHeaderText(), ''.join((
        '#include <QtCore/qglobal.h>\n',
        '#include <QtCore/qlist.h>\n',
        '#include <QtGui/qcolor.h>\n',
    )))

  def test_the_standard_of_a_ritual_file(self) -> None:
    """C++17, unless the first lines of comment ask for C++20; a line
    of 'Summon' after them is not read."""
    build = Summon()
    for text, standard in (
        (_ONE, 'c++17'),
        ('//  Written by hand.\n//  Summon: -std=c++20\nint x;\n', 'c++20'),
        ('int x;\n//  Summon: -std=c++20\n', 'c++17'),
        ('//  only a comment\n', 'c++17'),
    ):
      with self.subTest(text=text):
        self.assertEqual(
            build.getRitualStandard(self._write('std.cpp', text)), standard)

  def test_another_standard_is_refused(self) -> None:
    """Asking for any other standard raises, naming the one allowed."""
    path = self._write('std.cpp', '//  Summon: -std=c++23\nint x;\n')
    with self.assertRaises(ValueError) as caught:
      Summon().getRitualStandard(path)
    self.assertIn("'-std=c++23'", str(caught.exception))
    self.assertIn("'-std=c++20'", str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE FOLDERS OF THE PRIVATE HEADERS   # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_private_folders_of_the_parts_then_the_others(self) -> None:
    """The folders of the parts told that are there, then those of every
    other part of Qt, then the folder of the system's specs."""
    include = os.path.join(self.qt, 'include')
    for part in ('QtCore', 'QtGui', 'QtXml'):
      os.makedirs(os.path.join(include, part, '6.12.0', part, 'private'))
    os.makedirs(os.path.join(include, 'QtCutie'))
    os.makedirs(os.path.join(include, 'other'))
    build = self._build(_ONE)
    build.setComponents('QtGui', 'QtCore', 'QtGui')
    answers = {'QT_HOST_DATA': '/qt/host\n', 'QMAKE_SPEC': 'linux-g++\n'}
    with mock.patch.object(Summon, '_run', side_effect=(
        lambda *command: answers[command[2]])):
      folders = build.getPrivateIncludeFolders()

    def four(part: str) -> List[str]:
      top = os.path.join(include, part)
      return [top, os.path.join(top, '6.12.0'),
              os.path.join(top, '6.12.0', part),
              os.path.join(top, '6.12.0', part, 'private')]

    self.assertEqual(folders, (
        *four('QtGui'), *four('QtCore'), os.path.join(include, 'QtCutie'),
        *four('QtXml'), os.path.join('/qt/host', 'mkspecs', 'linux-g++')))
    with mock.patch.object(Summon, '_run') as run:
      self.assertIs(build.getPrivateIncludeFolders(), folders)
    run.assert_not_called()

  def test_no_private_folders_without_parts_that_have_them(self) -> None:
    """No part told, or none of them with folders: no folders, and
    'qmake6' is not asked."""
    build = self._build(_ONE)
    for components in ((), ('QtMissing',)):
      with self.subTest(components=components):
        build.setComponents(*components)
        with mock.patch.object(Summon, '_run') as run:
          self.assertEqual(build.getPrivateIncludeFolders(), ())
        run.assert_not_called()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IS STALE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_everything_is_stale_until_told(self) -> None:
    """With no told file, or one saying another build, every ritual file
    is compiled."""
    build = self._build(_ONE, _TWO)
    self.assertEqual(build.getStaleRitualFiles(), build.getRitualFiles())
    os.makedirs(build.getObjectFolder())
    with open(build.getToldFile(), 'w') as file:
      file.write('Qt 6.11.0\nsomething else\n')
    self.assertEqual(build.getStaleRitualFiles(), build.getRitualFiles())

  def test_what_is_stale_once_told(self) -> None:
    """Once told as now, a ritual file with no object file, or newer than
    it, is stale, and one older is not."""
    build = self._build(_ONE, _TWO, _ONE)
    os.makedirs(build.getObjectFolder())
    with open(build.getToldFile(), 'w') as file:
      file.write(build.getToldText())
    first, second, third = build.getRitualFiles()
    for ritualFile in (first, second):
      objectFile = build.getObjectFile(ritualFile)
      os.makedirs(os.path.dirname(objectFile), exist_ok=True)
      open(objectFile, 'w').close()
    later = time.time() + 100
    os.utime(second, (later, later))
    self.assertEqual(build.getStaleRitualFiles(), (second, third))

  def test_what_the_told_file_says(self) -> None:
    """The told file holds the version of Qt and both commands."""
    build = self._build(_ONE)
    said = build.getToldText().split('\n')
    self.assertEqual(said[0], 'Qt 6.12.0')
    self.assertEqual(said[1], ' '.join(build.getPrecompileCommand()))
    self.assertIn('RITUAL_FILE', said[2])
    self.assertEqual(said[3], '')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE COMMANDS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_command_of_the_precompiled_header(self) -> None:
    """'clang++' makes the precompiled header of the common header, told
    as every ritual file is told."""
    build = self._build(_ONE)
    include = os.path.join(self.qt, 'include')
    self.assertEqual(build.getPrecompileCommand(), (
        'clang++', '-std=c++17', '-O2', '-fno-access-control',
        '-DQT_USE_QSTRINGBUILDER', '-fPIC', '-fvisibility=hidden',
        '-fvisibility-inlines-hidden', '-I%s' % include,
        '-fpch-instantiate-templates', '-x', 'c++-header',
        build.getCommonHeaderFile(), '-o',
        build.getPrecompiledHeaderFile()))

  def test_the_command_of_a_ritual_file(self) -> None:
    """A ritual file of C++17 is compiled with the precompiled header;
    one of C++20, one of Objective-C++, or any after the precompiled
    header was refused, without it."""
    build = self._build(_ONE)
    include = os.path.join(self.qt, 'include')
    plain = self._write('QtCutieRituals/q_plain.cpp', _ONE)
    newer = self._write('QtCutieRituals/q_newer.cpp',
                        '//  Summon: -std=c++20\n' + _ONE)
    apple = self._write('QtCutieRituals/q_apple__objc.mm', _ONE)
    pch = ('-include-pch', build.getPrecompiledHeaderFile())
    for ritualFile, standard, precompiled in (
        (plain, 'c++17', pch), (newer, 'c++20', ()), (apple, 'c++17', ())):
      with self.subTest(ritualFile=ritualFile):
        self.assertEqual(build.getCompileCommand(ritualFile), (
            'clang++', '-std=%s' % standard, '-O2', '-fno-access-control',
            '-DQT_USE_QSTRINGBUILDER', '-c', '-fPIC', '-fvisibility=hidden',
            '-fvisibility-inlines-hidden', '-I%s' % include, *precompiled,
            ritualFile, '-o', build.getObjectFile(ritualFile)))
    build.__without_precompiled__ = True
    self.assertNotIn('-include-pch', build.getCompileCommand(plain))

  def test_the_command_that_joins(self) -> None:
    """The object files of every ritual file are joined into the target
    file, with Qt's shared objects and the static dependencies."""
    build = self._build(_ONE, _TWO)
    build.setStaticDependencies('-lm')
    command = build.getLinkCommand()
    objects = [build.getObjectFile(f) for f in build.getRitualFiles()]
    self.assertEqual(command[:5], (
        'clang++', '-shared', '-fPIC', '-fvisibility=hidden',
        '-fvisibility-inlines-hidden'))
    self.assertEqual(command[5:9], Linux().getLinkerFlags(
        os.path.join(self.qt, 'lib')))
    self.assertEqual(command[9:], (
        *objects, '-o', build.getTargetFile(), *build.getQtSharedObjects(),
        '-lm'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RECORD   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_record_with_no_left_out_file(self) -> None:
    """With no left-out file the record says nothing was left out."""
    record = self._build(_ONE).getRecord()
    self.assertEqual(record['common header'], None)
    self.assertEqual(record['ritual files'], {})
    self.assertIn("What 'Summon' left out", record['about'][0])

  def test_the_record_is_written_and_read(self) -> None:
    """A record of something left out is written as JSON, and read back
    with the rituals it left out."""
    build = self._build(_ONE)
    record = build.getRecord()
    record['ritual files']['QtCutieRituals/q_cutie_0.cpp'] = dict(
        dropped=[], whole=None,
        leftOut={'ritual_cutie_one': ['int one()', 'refused']})
    build._writeRecord(record)
    self.assertEqual(build.getRecord(), record)
    self.assertEqual(build.getLeftOut(),
                     {'ritual_cutie_one': ('int one()', 'refused')})
    self.assertEqual(
        Summon.readLeftOut(build.getLeftOutFile()), build.getLeftOut())

  def test_a_record_of_the_common_header_alone(self) -> None:
    """A record saying only that the common header was refused is
    written, and leaves out no ritual."""
    build = self._build(_ONE)
    record = build.getRecord()
    record['common header'] = 'refused'
    build._writeRecord(record)
    self.assertTrue(os.path.isfile(build.getLeftOutFile()))
    self.assertEqual(build.getLeftOut(), {})

  def test_a_record_of_nothing_left_out_removes_the_file(self) -> None:
    """A record of nothing removes an earlier left-out file, and is no
    trouble when there is none."""
    build = self._build(_ONE)
    record = build.getRecord()
    build._writeRecord(record)
    self.assertFalse(os.path.exists(build.getLeftOutFile()))
    with open(build.getLeftOutFile(), 'w') as file:
      file.write('{}')
    build._writeRecord(record)
    self.assertFalse(os.path.exists(build.getLeftOutFile()))

  def test_no_left_out_file_leaves_out_nothing(self) -> None:
    """A left-out file not there leaves out nothing and says no part
    went unbuilt."""
    self.assertEqual(Summon.readLeftOut('/no/such.left_out.json'), {})
    self.assertIsNone(Summon.readNotBuilt('/no/such.left_out.json'))

  def test_the_placeholder_of_a_part_not_built(self) -> None:
    """The placeholder says why the part was not built, beside what the
    left-out file held, and is read back."""
    build = self._build(_ONE)
    leftOut = build.getLeftOutFile()
    Summon.writeNotBuilt(leftOut, 'Qt has no QtCutie here')
    self.assertEqual(Summon.readNotBuilt(leftOut), 'Qt has no QtCutie here')
    record = build.getRecord()
    record['ritual files']['x'] = dict(leftOut={'ritual_a': ['a()', 'r']})
    build._writeRecord(record)
    Summon.writeNotBuilt(leftOut, 'the link failed')
    with open(leftOut, encoding='utf-8') as file:
      written = json.load(file)
    self.assertEqual(written['not built'], 'the link failed')
    self.assertEqual(written['ritual files']['x'],
                     dict(leftOut={'ritual_a': ['a()', 'r']}))
    self.assertIn('could not be built', written['about'][0])
    self.assertIsNone(Summon.readNotBuilt(self._write('x.json', '{}')))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  COMPILING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_precompiled_header_is_made_of_the_common_one(self) -> None:
    """The common header is written, then made into the precompiled one
    by its command."""
    build = self._build(_ONE)
    os.makedirs(build.getObjectFolder())
    with mock.patch.object(Summon, '_run') as run:
      build._precompile()
    run.assert_called_once_with(*build.getPrecompileCommand())
    with open(build.getCommonHeaderFile(), encoding='utf-8') as file:
      self.assertEqual(file.read(), '#include <QtCore/qglobal.h>\n')

  def test_a_refused_common_header_says_so(self) -> None:
    """When 'clang++' refuses the common header, it is said, with what
    'clang++' said."""
    build = self._build(_ONE)
    os.makedirs(build.getObjectFolder())
    with mock.patch.object(
        Summon, '_run', side_effect=RuntimeError('no qglobal.h')):
      with self.assertRaises(RuntimeError) as caught:
        build._precompile()
    self.assertIn('refused the common header', str(caught.exception))
    self.assertIn('no qglobal.h', str(caught.exception))

  def test_compiling_one_ritual_file(self) -> None:
    """One ritual file is compiled by its command, giving None, or what
    'clang++' said, the file named in front."""
    build = self._build(_ONE)
    ritualFile, = build.getRitualFiles()
    with mock.patch.object(Summon, '_run') as run:
      self.assertIsNone(build._compile(ritualFile))
    run.assert_called_once_with(*build.getCompileCommand(ritualFile))
    with mock.patch.object(Summon, '_run', side_effect=RuntimeError('no')):
      self.assertEqual(build._compile(ritualFile), '%s: no' % ritualFile)

  def test_compiling_the_copy(self) -> None:
    """The copy is compiled into the object file of its ritual file, with
    every error said, and its own folder looked in for quoted headers."""
    build = self._build(_ONE)
    ritualFile, = build.getRitualFiles()
    copyFile = build.getExorcisedFile(ritualFile)
    with mock.patch.object(Summon, '_run') as run:
      self.assertIsNone(build._compileCopy(ritualFile, copyFile))
    command = run.call_args[0]
    self.assertEqual(command[:6], (
        'clang++', '-ferror-limit=0', '-ftemplate-backtrace-limit=0',
        '-iquote', os.path.dirname(ritualFile), '-std=c++17'))
    self.assertEqual(command[-3:],
                     (copyFile, '-o', build.getObjectFile(ritualFile)))
    with mock.patch.object(Summon, '_run', side_effect=RuntimeError('no')):
      self.assertEqual(build._compileCopy(ritualFile, copyFile), 'no')

  def test_an_exorcist_of_a_ritual_file(self) -> None:
    """An Exorcist drops again what the record says of its file; a
    record of the file as it was before is forgotten."""
    build = self._build(_TWO)
    ritualFile, = build.getRitualFiles()
    key = Summon._getRecordKey(ritualFile)
    broken = ('ritual', 'ritual_cutie_broken', 9, 13)
    record = dict(ritual_files=None)
    record = {'ritual files': {key: dict(
        dropped=[[*broken, 'refused']], whole=None)}}
    self.assertEqual(build._createExorcist(ritualFile, record).getDropped(),
                     {broken: 'refused'})
    record = {'ritual files': {key: dict(
        dropped=[['ritual', 'ritual_gone', 1, 2, 'refused']])}}
    self.assertEqual(
        build._createExorcist(ritualFile, record).getDropped(), {})
    self.assertEqual(build._createExorcist(
        ritualFile, {'ritual files': {}}).getDropped(), {})

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FINDING BY TRIAL   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _trialBuild(self, refusedBy: Any) -> Any:
    """A build of '_TWO', and an Exorcist of it, whose copy 'clang++'
    refuses while 'refusedBy' says so of the text, with an error at no
    item."""
    build = self._build(_TWO)
    ritualFile, = build.getRitualFiles()
    os.makedirs(os.path.dirname(build.getObjectFile(ritualFile)))
    exorcist = build._createExorcist(ritualFile, {'ritual files': {}})

    def compileCopy(ritualFile: str, copyFile: str) -> Any:
      with open(copyFile, encoding='utf-8') as file:
        text = file.read()
      if refusedBy(text):
        return '%s:1:1: error: refused' % copyFile
      return None

    return build, ritualFile, exorcist, compileCopy

  def test_the_trial_finds_the_one_item(self) -> None:
    """Leaving out the rituals in halves finds the one whose leaving out
    clears the copy."""
    build, ritualFile, exorcist, compileCopy = self._trialBuild(
        lambda text: 'ritual_cutie_broken' in text)
    with mock.patch.object(build, '_compileCopy', side_effect=compileCopy):
      found = build._findByTrial(ritualFile, exorcist)
    self.assertEqual(found, ('ritual', 'ritual_cutie_broken', 9, 13))

  def test_the_trial_finds_the_first_of_two(self) -> None:
    """Of two rituals, the first whose leaving out clears it."""
    build, ritualFile, exorcist, compileCopy = self._trialBuild(
        lambda text: 'ritual_cutie_fine' in text)
    with mock.patch.object(build, '_compileCopy', side_effect=compileCopy):
      found = build._findByTrial(ritualFile, exorcist)
    self.assertEqual(found, ('ritual', 'ritual_cutie_fine', 3, 7))

  def test_the_trial_widens_to_the_includes(self) -> None:
    """When no ritual clears it, the trial widens to the other items."""
    lines = _TWO.replace('#include <QtCore/qglobal.h>\n',
                         '#if X\n#endif\n#include <QtCore/qbroken.h>\n')
    build = self._build(lines)
    ritualFile, = build.getRitualFiles()
    os.makedirs(os.path.dirname(build.getObjectFile(ritualFile)))
    exorcist = build._createExorcist(ritualFile, {'ritual files': {}})

    def compileCopy(ritualFile: str, copyFile: str) -> Any:
      with open(copyFile, encoding='utf-8') as file:
        text = file.read()
      return 'q.cpp:1:1: error: x' if 'qbroken.h' in text else None

    with mock.patch.object(build, '_compileCopy', side_effect=compileCopy):
      found = build._findByTrial(ritualFile, exorcist)
    self.assertEqual(found, ('include', '<QtCore/qbroken.h>', 3, 3))

  def test_the_trial_finds_nothing(self) -> None:
    """When leaving out every item does not clear it, it finds nothing."""
    build, ritualFile, exorcist, compileCopy = self._trialBuild(
        lambda text: True)
    with mock.patch.object(build, '_compileCopy', side_effect=compileCopy):
      self.assertIsNone(build._findByTrial(ritualFile, exorcist))

  def test_the_trial_of_a_file_with_nothing_to_leave_out(self) -> None:
    """A file with nothing to leave out finds nothing, compiling nothing."""
    build = self._build('#include <QtCore/qglobal.h>\nint x;\n')
    ritualFile, = build.getRitualFiles()
    exorcist = build._createExorcist(ritualFile, {'ritual files': {}})
    with mock.patch.object(build, '_compileCopy') as compileCopy:
      self.assertIsNone(build._findByTrial(ritualFile, exorcist))
    compileCopy.assert_not_called()

  def test_a_trial_cleared_by_what_the_compiler_blames(self) -> None:
    """A copy still refused, but only at the items left out, clears."""
    build, ritualFile, exorcist, compileCopy = self._trialBuild(
        lambda text: False)

    def blamedOnly(ritualFile: str, copyFile: str) -> Any:
      return '%s:11:3: error: in the broken one' % copyFile

    with mock.patch.object(build, '_compileCopy', side_effect=blamedOnly):
      found = build._findByTrial(ritualFile, exorcist)
    self.assertEqual(found, ('ritual', 'ritual_cutie_fine', 3, 7))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  EXORCISING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _exorciseBuild(self) -> Any:
    """A build of '_TWO' and an Exorcist of it, its folders made."""
    build = self._build(_TWO)
    ritualFile, = build.getRitualFiles()
    os.makedirs(os.path.dirname(build.getObjectFile(ritualFile)))
    return build, ritualFile, build._createExorcist(
        ritualFile, {'ritual files': {}})

  def test_exorcising_drops_what_is_blamed(self) -> None:
    """What the errors blame is dropped, and the copy compiled again."""
    build, ritualFile, exorcist = self._exorciseBuild()
    said = '%s:12:3: error: broken' % ritualFile
    with mock.patch.object(build, '_compileCopy', return_value=None) as cc:
      build._exorcise(ritualFile, exorcist, said, ritualFile)
    cc.assert_called_once()
    self.assertEqual([*exorcist.getLeftOut()], ['ritual_cutie_broken'])
    with open(build.getExorcisedFile(ritualFile), encoding='utf-8') as file:
      self.assertNotIn('ritual_cutie_broken', file.read())

  def test_exorcising_with_nothing_said_compiles_the_copy(self) -> None:
    """With nothing said yet, the copy is compiled as it is."""
    build, ritualFile, exorcist = self._exorciseBuild()
    with mock.patch.object(build, '_compileCopy', return_value=None):
      build._exorcise(ritualFile, exorcist, None, ritualFile)
    self.assertEqual(exorcist.getDropped(), {})

  def test_exorcising_by_trial(self) -> None:
    """An error the compiler blames on no item is found by trial, and
    the item dropped with what the compiler said."""
    build, ritualFile, exorcist = self._exorciseBuild()
    found = ('ritual', 'ritual_cutie_fine', 3, 7)
    said = '%s:1:1: error: at no item' % ritualFile
    with mock.patch.object(build, '_findByTrial', return_value=found), \
        mock.patch.object(build, '_compileCopy', return_value=None):
      build._exorcise(ritualFile, exorcist, said, ritualFile)
    reason = exorcist.getDropped()[found]
    self.assertIn('as compiling the file without it showed', reason)
    self.assertIn('error: at no item', reason)

  def test_exorcising_drops_the_whole_when_trial_finds_none(self) -> None:
    """When the trial finds nothing the whole file is dropped, and its
    empty copy compiled."""
    build, ritualFile, exorcist = self._exorciseBuild()
    said = '%s:1:1: error: at no item' % ritualFile
    with mock.patch.object(build, '_findByTrial', return_value=None), \
        mock.patch.object(build, '_compileCopy', return_value=None):
      build._exorcise(ritualFile, exorcist, said, ritualFile)
    self.assertIn('no ritual of it holds alone', exorcist.getWholeReason())
    self.assertIn('error: at no item', exorcist.getWholeReason())

  def test_exorcising_a_message_with_no_error(self) -> None:
    """What 'clang++' said with no error in it is quoted at its end."""
    build, ritualFile, exorcist = self._exorciseBuild()
    with mock.patch.object(build, '_findByTrial', return_value=None), \
        mock.patch.object(build, '_compileCopy', return_value=None):
      build._exorcise(ritualFile, exorcist, ' clang crashed ', ritualFile)
    self.assertTrue(exorcist.getWholeReason().endswith('clang crashed'))

  def test_exorcising_too_many_rounds(self) -> None:
    """A copy still refused after every round is dropped whole."""
    build, ritualFile, exorcist = self._exorciseBuild()
    rounds = []

    def refused(ritualFile: str, copyFile: str) -> Any:
      rounds.append(copyFile)
      if exorcist.getWholeReason() is not None:
        return None
      return '%s:12:3: error: again' % copyFile

    with mock.patch.object(Summon, '__exorcism_rounds__', 2), \
        mock.patch.object(Exorcist, 'drop'), \
        mock.patch.object(build, '_compileCopy', side_effect=refused):
      build._exorcise(ritualFile, exorcist, None, ritualFile)
    self.assertIn('after 2 rounds', exorcist.getWholeReason())
    self.assertEqual(len(rounds), 4)

  def test_an_empty_copy_refused(self) -> None:
    """When even the empty copy is refused, it raises, naming both
    files and what was said."""
    build, ritualFile, exorcist = self._exorciseBuild()
    exorcist.dropWhole('all of it')
    with mock.patch.object(build, '_compileCopy',
                           return_value='broken compiler'):
      with self.assertRaises(RuntimeError) as caught:
        build._exorcise(ritualFile, exorcist, None, ritualFile)
    said = str(caught.exception)
    self.assertIn('refused the empty copy', said)
    self.assertIn(build.getExorcisedFile(ritualFile), said)
    self.assertIn('broken compiler', said)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  JOINING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _linkBuild(self) -> Any:
    """A build of '_ONE' and '_TWO', its folders made."""
    build = self._build(_ONE, _TWO)
    for ritualFile in build.getRitualFiles():
      os.makedirs(os.path.dirname(build.getObjectFile(ritualFile)),
                  exist_ok=True)
    return build

  def test_joining_at_once(self) -> None:
    """A link that works at once is all."""
    build = self._linkBuild()
    with mock.patch.object(Summon, '_run') as run:
      build._link({}, {'ritual files': {}})
    run.assert_called_once_with(*build.getLinkCommand())

  def test_joining_again_without_what_the_linker_names(self) -> None:
    """What the linker names is dropped from its file, whose copy is
    compiled without the precompiled header, and it is joined again."""
    build = self._linkBuild()
    first, second = build.getRitualFiles()
    refusal = '\n'.join((
        "/usr/bin/ld: q_cutie_1.o: in function `ritual_cutie_broken':",
        "q.cpp:(.text+0x1): undefined reference to `cutie_gone()'",
    ))
    links = [RuntimeError(refusal), None]
    exorcists = dict()  # type: Dict[str, Exorcist]
    with mock.patch.object(Summon, '_run', side_effect=links), \
        mock.patch.object(build, '_exorcise') as exorcise:
      build._link(exorcists, {'ritual files': {}})
    self.assertEqual([*exorcists], [second])
    self.assertEqual([*exorcists[second].getLeftOut()],
                     ['ritual_cutie_broken'])
    exorcise.assert_called_once_with(
        second, exorcists[second], None, second)
    self.assertIs(build.__without_precompiled__, True)

  def test_joining_drops_a_file_the_linker_names_alone(self) -> None:
    """A file named for what none of its items holds is dropped whole;
    an Exorcist given is the one used."""
    build = self._linkBuild()
    first, second = build.getRitualFiles()
    given = build._createExorcist(first, {'ritual files': {}})
    refusal = "/usr/bin/ld: q_cutie_0.o:(.data+0x0): undefined reference " \
              "to `vtable for QGone'"
    with mock.patch.object(Summon, '_run', side_effect=[
        RuntimeError(refusal), None]), \
        mock.patch.object(build, '_exorcise'):
      build._link({first: given}, {'ritual files': {}})
    self.assertIn("it needs 'vtable for QGone'", given.getWholeReason())

  def test_joining_refused_with_no_ritual_file_named(self) -> None:
    """A link refused for what no object file of the ritual files holds
    raises, with what the linker said."""
    build = self._linkBuild()
    with mock.patch.object(
        Summon, '_run', side_effect=RuntimeError('no such Qt')):
      with self.assertRaises(RuntimeError) as caught:
        build._link({}, {'ritual files': {}})
    said = str(caught.exception)
    self.assertIn('named no object file of the ritual files', said)
    self.assertIn('no such Qt', said)

  def test_joining_refused_after_every_round(self) -> None:
    """A link still refused after every round raises."""
    build = self._linkBuild()
    refusal = RuntimeError(
        "/usr/bin/ld: q_cutie_0.o:(.data+0x0): undefined reference to `x'")
    with mock.patch.object(Summon, '__link_rounds__', 1), \
        mock.patch.object(Summon, '_run', side_effect=refusal), \
        mock.patch.object(build, '_exorcise'):
      with self.assertRaises(RuntimeError) as caught:
        build._link({}, {'ritual files': {}})
    self.assertIn('still refused after 1 rounds', str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  RUNNING A BUILD  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_two_ritual_files_of_one_name_are_refused(self) -> None:
    """Two ritual files that would make one object file are refused."""
    first = self._write('QtCutieRituals/q_same.cpp', _ONE)
    second = self._write('other/QtCutieRituals/q_same.cpp', _ONE)
    build = self._build(_ONE)
    build.setRitualFiles(first, second)
    with self.assertRaises(ValueError) as caught:
      build.run()
    self.assertIn('q_same.o', str(caught.exception))

  def test_a_run_compiles_what_is_stale_and_joins(self) -> None:
    """A run makes the folders, compiles every stale file with the
    precompiled header made and removed, writes the told file, joins,
    and writes no left-out file when nothing was left out."""
    build = self._build(_ONE, _TWO)
    compiled = []

    def run(*command: str) -> str:
      if '-o' in command:
        made = command[command.index('-o') + 1]
        open(made, 'w').close()
        compiled.append(os.path.basename(made))
      return ''

    with mock.patch.object(Summon, '_run', side_effect=run):
      self.assertEqual(build.run(), build.getTargetFile())
    self.assertEqual(compiled[0], 'libcutienator_QtCutie.common.pch')
    self.assertEqual(sorted(compiled[1:3]), ['q_cutie_0.o', 'q_cutie_1.o'])
    self.assertEqual(compiled[3], 'libcutienator_QtCutie.so')
    self.assertFalse(os.path.exists(build.getPrecompiledHeaderFile()))
    with open(build.getToldFile()) as file:
      self.assertEqual(file.read(), build.getToldText())
    self.assertFalse(os.path.exists(build.getLeftOutFile()))
    self.assertIs(build.__without_precompiled__, False)

  def test_a_run_after_another_build_starts_over(self) -> None:
    """A told file of another build is removed before anything is
    compiled, the record of that build forgotten, and the told file
    written anew once all is compiled."""
    build = self._build(_ONE)
    os.makedirs(build.getObjectFolder())
    with open(build.getToldFile(), 'w') as file:
      file.write('Qt 6.11.0\n')
    record = build.getRecord()
    record['ritual files']['QtCutieRituals/old.cpp'] = dict(
        leftOut={'ritual_old': ['old()', 'refused']})
    record['common header'] = 'refused once'
    build._writeRecord(record)
    seen = []

    def run(*command: str) -> str:
      seen.append(os.path.exists(build.getToldFile()))
      return ''

    with mock.patch.object(Summon, '_run', side_effect=run):
      build.run()
    self.assertEqual(seen, [False, False, True])
    with open(build.getToldFile()) as file:
      self.assertEqual(file.read(), build.getToldText())
    self.assertFalse(os.path.exists(build.getLeftOutFile()))

  def test_a_run_with_nothing_stale_only_joins(self) -> None:
    """With nothing stale a run compiles nothing and joins; the record
    of an earlier build stays, its placeholder of not built gone."""
    build = self._build(_ONE)
    ritualFile, = build.getRitualFiles()
    objectFile = build.getObjectFile(ritualFile)
    os.makedirs(os.path.dirname(objectFile))
    open(objectFile, 'w').close()
    with open(build.getToldFile(), 'w') as file:
      file.write(build.getToldText())
    record = build.getRecord()
    record['ritual files']['QtCutieRituals/old.cpp'] = dict(
        leftOut={'ritual_old': ['old()', 'refused']})
    record['not built'] = 'the link failed'
    build._writeRecord(record)
    with mock.patch.object(Summon, '_run') as run:
      build.run()
    run.assert_called_once_with(*build.getLinkCommand())
    self.assertEqual(build.getLeftOut(),
                     {'ritual_old': ('old()', 'refused')})
    self.assertIsNone(Summon.readNotBuilt(build.getLeftOutFile()))

  def test_a_run_whose_common_header_is_refused(self) -> None:
    """When the common header is refused, every file is compiled without
    it, and the record says what was refused."""
    build = self._build(_ONE)
    commands = []

    def run(*command: str) -> str:
      if '-x' in command:
        raise RuntimeError('no qglobal.h')
      commands.append(command)
      return ''

    with mock.patch.object(Summon, '_run', side_effect=run):
      build.run()
    self.assertNotIn('-include-pch', commands[0])
    self.assertIn('no qglobal.h', build.getRecord()['common header'])

  @staticmethod
  def _refusesBroken(ritualFile: str, copyFile: str) -> Any:
    """A stand-in for '_compileCopy' refusing the copy while it still
    holds the broken ritual, at its line."""
    with open(copyFile, encoding='utf-8') as file:
      if 'ritual_cutie_broken' in file.read():
        return '%s:12:3: error: broken' % copyFile
    return None

  def test_a_run_exorcising_a_refused_file(self) -> None:
    """A ritual file 'clang++' refuses is exorcised, and what was left
    out of it written to the left-out file; the record of a file not
    stale stays."""
    build = self._build(_TWO)
    ritualFile, = build.getRitualFiles()

    def run(*command: str) -> str:
      if '-c' in command and command[command.index('-c') + 1:] and (
          ritualFile in command):
        raise RuntimeError('%s:12:3: error: broken' % ritualFile)
      return ''

    with mock.patch.object(Summon, '_run', side_effect=run), \
        mock.patch.object(
            build, '_compileCopy', side_effect=self._refusesBroken):
      build.run()
    self.assertEqual([*build.getLeftOut()], ['ritual_cutie_broken'])

  def test_a_run_that_cannot_join_still_writes_its_record(self) -> None:
    """When the link fails for good, the record of what was left out is
    written all the same, and the build raises."""
    build = self._build(_TWO)
    ritualFile, = build.getRitualFiles()

    def run(*command: str) -> str:
      if '-shared' in command:
        raise RuntimeError('no Qt at all')
      if '-c' in command and ritualFile in command:
        raise RuntimeError('%s:12:3: error: broken' % ritualFile)
      return ''

    with mock.patch.object(Summon, '_run', side_effect=run), \
        mock.patch.object(
            build, '_compileCopy', side_effect=self._refusesBroken):
      with self.assertRaises(RuntimeError):
        build.run()
    self.assertEqual([*build.getLeftOut()], ['ritual_cutie_broken'])
    self.assertIs(build.__without_precompiled__, False)
