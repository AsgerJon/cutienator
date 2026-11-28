"""
TestOccultSharedObject tests 'SharedObject', which reads the list of
names a shared object offers.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import SharedObject, Symbol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, List


#  A small library of C++ for the test of a real file: a function and a
#  number of C, a function of C++, and a constructor, which C++ stores
#  twice under one readable name.
_SOURCE = """
extern "C" int cutie_alpha() { return 1; }
extern "C" { int cutie_data = 7; }
namespace cutie {
  struct Box { Box(); int value; };
  Box::Box() : value(3) {}
  int twice(int x) { return 2 * x; }
}
"""


class TestOccultSharedObject(BaseTest):
  """
  Tests 'SharedObject': how a line of 'nm' is taken apart, how the
  entries of a file are made, found and listed, and each refusal.

  What to know before adding a test
  ---------------------------------

  - Most tests hand 'SharedObject' made-up output of 'nm' and 'c++filt',
    through '_fakeRun', so each shape of output can be tried; the file
    named must still be there, so it is an empty temporary file.
  - One library of C++ is compiled for the whole class with 'clang++'
    ('setUpClass'), and read for real with the 'nm' and 'c++filt' of the
    machine, as the tooling reads Qt's shared objects.
  """

  __library_folder__ = None  # type: Any
  __library_path__ = None  # type: Any

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SET UP   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Compiles the small library once for every test of the class."""
    super().setUpClass()
    cls.__library_folder__ = tempfile.TemporaryDirectory()
    folder = cls.__library_folder__.name
    source = os.path.join(folder, 'cutie.cpp')
    with open(source, 'w', encoding='utf-8') as file:
      file.write(_SOURCE)
    library = os.path.join(folder, 'libcutie.so')
    subprocess.run(
        ('clang++', '-shared', '-fPIC', '-o', library, source), check=True)
    cls.__library_path__ = library

  @classmethod
  def tearDownClass(cls) -> None:
    """Removes the folder of the small library."""
    cls.__library_folder__.cleanup()
    super().tearDownClass()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _fakeRun(nmLines: List[str], filtLines: List[str]) -> Callable:
    """A stand-in for '_run' giving 'nmLines' for 'nm' and 'filtLines'
    for 'c++filt', each line ended."""

    def fake(*command: str, **kwargs: Any) -> str:
      lines = nmLines if command[0] == 'nm' else filtLines
      return ''.join('%s\n' % line for line in lines)

    return fake

  def _emptyFile(self) -> str:
    """Gives the path of an empty file, removed when the test ends."""
    folder = tempfile.mkdtemp()
    self.addCleanup(shutil.rmtree, folder)
    path = os.path.join(folder, 'libfake.so')
    open(path, 'w').close()
    return path

  def _fakeObject(self) -> SharedObject:
    """A shared object of four made-up entries: a function, two entries
    of one constructor, and data."""
    nm = [
        '0000000000001000 T _ZN6QTimer5startEv@@Qt_6',
        '0000000000002000 T _ZN6QTimerC1Ev@@Qt_6',
        '0000000000002000 T _ZN6QTimerC2Ev@@Qt_6',
        '0000000000003000 D qt_version_tag@Qt_6.12',
    ]
    filt = [
        'QTimer::start()', 'QTimer::QTimer()', 'QTimer::QTimer()',
        'qt_version_tag',
    ]
    with mock.patch.object(
        SharedObject, '_run', side_effect=self._fakeRun(nm, filt)):
      return SharedObject(self._emptyFile())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  RUNNING A PROGRAM  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_program_gives_what_it_printed(self) -> None:
    """What the program prints comes back, and 'feed' is what it reads."""
    self.assertEqual(SharedObject._run('echo', 'cute'), 'cute\n')
    self.assertEqual(SharedObject._run('cat', feed='fed\n'), 'fed\n')

  def test_a_program_not_installed_is_named(self) -> None:
    """A program that is not installed raises, naming it."""
    with self.assertRaises(FileNotFoundError) as caught:
      SharedObject._run('no-such-program-of-cutienator')
    self.assertIn("'no-such-program-of-cutienator'", str(caught.exception))

  def test_a_program_that_fails_says_why(self) -> None:
    """A program ending with an error raises with what it said."""
    with self.assertRaises(RuntimeError) as caught:
      SharedObject._run('sh', '-c', 'echo broken >&2; exit 3')
    self.assertIn("'sh' failed: broken", str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A LINE OF NM   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_line_with_its_default_version(self) -> None:
    """'@@' marks the default version, which is kept without the '@'s."""
    self.assertEqual(
        SharedObject._parseLine(
            '0000000000208140 T _ZN6QTimer5startEv@@Qt_6'),
        (0x208140, 'T', '_ZN6QTimer5startEv', 'Qt_6'))

  def test_a_line_with_another_version(self) -> None:
    """One '@' marks another version, kept without the '@'."""
    self.assertEqual(
        SharedObject._parseLine('00000000000000ff D qt_tag@Qt_5'),
        (0xff, 'D', 'qt_tag', 'Qt_5'))

  def test_a_line_without_version(self) -> None:
    """A name with no version has the version ''."""
    self.assertEqual(
        SharedObject._parseLine('0000000000000010 T cutie_alpha'),
        (0x10, 'T', 'cutie_alpha', ''))

  def test_a_line_of_another_shape_is_refused(self) -> None:
    """A line of two fields, or of four, raises, quoting it."""
    for line in ('U _ZN6QTimer5startEv', '10 T name extra', ''):
      with self.subTest(line=line):
        with self.assertRaises(ValueError) as caught:
          SharedObject._parseLine(line)
        self.assertIn("'%s'" % line, str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING ONE   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_missing_file_is_refused(self) -> None:
    """A path where no file is raises, naming it, before any program."""
    with mock.patch.object(SharedObject, '_run') as run:
      with self.assertRaises(FileNotFoundError) as caught:
        SharedObject('/no/such/libcutie.so')
    run.assert_not_called()
    self.assertIn("'/no/such/libcutie.so'", str(caught.exception))

  def test_the_entries_in_the_order_nm_gave(self) -> None:
    """Each line becomes a symbol of its five values, in order."""
    shared = self._fakeObject()
    self.assertEqual(len(shared), 4)
    self.assertEqual([*shared], [
        Symbol('_ZN6QTimer5startEv', 'QTimer::start()', 'T', 0x1000,
               'Qt_6'),
        Symbol('_ZN6QTimerC1Ev', 'QTimer::QTimer()', 'T', 0x2000, 'Qt_6'),
        Symbol('_ZN6QTimerC2Ev', 'QTimer::QTimer()', 'T', 0x2000, 'Qt_6'),
        Symbol('qt_version_tag', 'qt_version_tag', 'D', 0x3000,
               'Qt_6.12'),
    ])

  def test_nm_and_cppfilt_are_asked_once(self) -> None:
    """'nm' lists the names offered, and 'c++filt' reads all of them at
    once, one on each line."""
    path = self._emptyFile()
    run = mock.Mock(side_effect=self._fakeRun(
        ['10 T _ZN6QTimer5startEv'], ['QTimer::start()']))
    with mock.patch.object(SharedObject, '_run', run):
      SharedObject(path)
    self.assertEqual(run.call_args_list, [
        mock.call('nm', '-D', '--defined-only', path),
        mock.call('c++filt', feed='_ZN6QTimer5startEv\n'),
    ])

  def test_a_path_object_is_taken(self) -> None:
    """A 'pathlib.Path' is taken, and kept as text."""
    path = self._emptyFile()
    with mock.patch.object(SharedObject, '_run', side_effect=self._fakeRun(
        ['10 T cutie_alpha'], ['cutie_alpha'])):
      shared = SharedObject(pathlib.Path(path))
    self.assertEqual(shared.path, path)
    self.assertIsInstance(shared.path, str)

  def test_a_file_offering_nothing(self) -> None:
    """A file 'nm' lists nothing of has no entries."""
    with mock.patch.object(
        SharedObject, '_run', side_effect=self._fakeRun([], [])):
      shared = SharedObject(self._emptyFile())
    self.assertEqual(len(shared), 0)
    self.assertEqual([*shared], [])

  def test_cppfilt_giving_another_count_is_refused(self) -> None:
    """'c++filt' giving back fewer names than it got raises, counting
    both."""
    with mock.patch.object(SharedObject, '_run', side_effect=self._fakeRun(
        ['10 T _ZN6QTimer5startEv', '20 T cutie_alpha'],
        ['QTimer::start()'])):
      with self.assertRaises(ValueError) as caught:
        SharedObject(self._emptyFile())
    self.assertIn('received 2 names', str(caught.exception))
    self.assertIn('gave back 1', str(caught.exception))

  def test_a_cpp_name_cppfilt_cannot_read_is_refused(self) -> None:
    """A name of C++ that 'c++filt' gives back unchanged raises."""
    with mock.patch.object(SharedObject, '_run', side_effect=self._fakeRun(
        ['10 T _ZN6QTimer5startEv'], ['_ZN6QTimer5startEv'])):
      with self.assertRaises(ValueError) as caught:
        SharedObject(self._emptyFile())
    self.assertIn("'_ZN6QTimer5startEv'", str(caught.exception))

  def test_a_name_of_c_reads_as_itself(self) -> None:
    """A name that is no C++ name reads the same, and is taken."""
    with mock.patch.object(SharedObject, '_run', side_effect=self._fakeRun(
        ['10 T cutie_alpha'], ['cutie_alpha'])):
      shared = SharedObject(self._emptyFile())
    self.assertEqual(shared['cutie_alpha'].mangled, 'cutie_alpha')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FINDING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_name_offered_is_in_it(self) -> None:
    """'in' says whether an entry has that readable name."""
    shared = self._fakeObject()
    self.assertIn('QTimer::start()', shared)
    self.assertIn('QTimer::QTimer()', shared)
    self.assertNotIn('QTimer::stop()', shared)
    self.assertNotIn('_ZN6QTimer5startEv', shared)

  def test_the_one_entry_of_a_name(self) -> None:
    """A name of one entry gives that entry."""
    shared = self._fakeObject()
    self.assertEqual(
        shared['QTimer::start()'].mangled, '_ZN6QTimer5startEv')

  def test_a_name_not_offered_is_refused(self) -> None:
    """A name of no entry raises, naming the file and the name."""
    shared = self._fakeObject()
    with self.assertRaises(LookupError) as caught:
      _ = shared['QTimer::stop()']
    self.assertIn("'QTimer::stop()'", str(caught.exception))
    self.assertIn(shared.path, str(caught.exception))

  def test_a_name_of_several_entries_is_refused(self) -> None:
    """A name of two entries raises, listing both stored spellings."""
    shared = self._fakeObject()
    with self.assertRaises(LookupError) as caught:
      _ = shared['QTimer::QTimer()']
    said = str(caught.exception)
    self.assertIn('2 entries', said)
    self.assertIn('_ZN6QTimerC1Ev, _ZN6QTimerC2Ev', said)
    self.assertIn("'named'", said)

  def test_named_gives_every_entry_of_a_name(self) -> None:
    """'named' gives all entries of a name, or none."""
    shared = self._fakeObject()
    self.assertEqual(
        [s.mangled for s in shared.named('QTimer::QTimer()')],
        ['_ZN6QTimerC1Ev', '_ZN6QTimerC2Ev'])
    self.assertEqual(shared.named('QTimer::stop()'), ())

  def test_search_gives_every_entry_containing_text(self) -> None:
    """'search' gives each entry whose readable name holds the text."""
    shared = self._fakeObject()
    self.assertEqual(
        [s.mangled for s in shared.search('QTimer::')],
        ['_ZN6QTimer5startEv', '_ZN6QTimerC1Ev', '_ZN6QTimerC2Ev'])
    self.assertEqual(shared.search('nothing like it'), ())

  def test_functions_leave_out_the_data(self) -> None:
    """'functions' gives the entries of code alone."""
    shared = self._fakeObject()
    self.assertEqual(
        [s.mangled for s in shared.functions()],
        ['_ZN6QTimer5startEv', '_ZN6QTimerC1Ev', '_ZN6QTimerC2Ev'])

  def test_str_and_repr(self) -> None:
    """'str' and 'repr' name the class, the file and the count."""
    shared = self._fakeObject()
    said = "<SharedObject '%s' offering 4 names>" % shared.path
    self.assertEqual(str(shared), said)
    self.assertEqual(repr(shared), said)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A REAL FILE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_real_library(self) -> None:
    """The small library, read with the machine's 'nm' and 'c++filt':
    its functions of C and of C++, its number, and its constructor
    stored twice."""
    shared = SharedObject(self.__library_path__)
    alpha = shared['cutie_alpha']
    self.assertTrue(alpha.isFunction())
    self.assertEqual(alpha.mangled, 'cutie_alpha')
    self.assertFalse(shared['cutie_data'].isFunction())
    twice = shared['cutie::twice(int)']
    self.assertEqual(twice.mangled, '_ZN5cutie5twiceEi')
    self.assertTrue(twice.isFunction())
    made = shared.named('cutie::Box::Box()')
    self.assertEqual(
        sorted(s.mangled for s in made),
        ['_ZN5cutie3BoxC1Ev', '_ZN5cutie3BoxC2Ev'])

  def test_a_file_that_is_no_shared_object(self) -> None:
    """'nm' refuses a file that is no shared object, and so does
    'SharedObject', with what 'nm' said."""
    path = self._emptyFile()
    with open(path, 'w', encoding='utf-8') as file:
      file.write('no shared object\n')
    with self.assertRaises(RuntimeError) as caught:
      SharedObject(path)
    self.assertIn("'nm' failed", str(caught.exception))
