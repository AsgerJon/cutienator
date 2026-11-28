"""
TestOccultMain tests 'python -m cutienator.occult', which prints what a
shared object offers.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import contextlib
import io
import os
import runpy
import subprocess
import sys
import tempfile
import unittest
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import __main__ as occultMain

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Tuple

#  A small library of C++: a function and a number of C, and two
#  functions of C++.
_SOURCE = """
extern "C" int cutie_alpha() { return 1; }
extern "C" { int cutie_data = 7; }
namespace cutie {
  int twice(int x) { return 2 * x; }
  int thrice(int x) { return 3 * x; }
}
"""


#  The tests marked with '_compiles' start 'clang++' for real. They run
#  where 'CUTIENATOR_TEST_COMPILES' is '1': on gcloud, and in a release
#  run on one machine of each system. Every other machine skips them,
#  so it compiles nothing.
_COMPILES = os.environ.get('CUTIENATOR_TEST_COMPILES', '') == '1'
_compiles = unittest.skipUnless(
    _COMPILES, "starts clang++: runs where CUTIENATOR_TEST_COMPILES=1")


@_compiles
class TestOccultMain(BaseTest):
  """
  Tests the program of the package 'occult': what it prints of a
  shared object, and how it refuses the wrong number of arguments.

  What to know before adding a test
  ---------------------------------

  - A small library of C++ is compiled for the class with 'clang++', as
    'TestOccultSharedObject' does, and read with the machine's 'nm' and
    'c++filt'.
  - 'main' is called with what the command line would hand it, and what
    it prints is caught; one test runs the package as a program, as
    'python -m' does, to see its exit code.
  """

  __library_folder__ = None  # type: Any
  __library_path__ = None  # type: Any

  @classmethod
  def setUpClass(cls) -> None:
    """Compiles the small library once for the class."""
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

  @staticmethod
  def _main(*args: str) -> Tuple[int, str, str]:
    """Runs 'main' with the arguments, and gives its exit code and what
    it printed and what it printed as errors."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
      code = occultMain.main(*args)
    return code, out.getvalue(), err.getvalue()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_how_many_names_a_file_offers(self) -> None:
    """With the file alone, it says how many names and functions."""
    code, said, errors = self._main(self.__library_path__)
    self.assertEqual(code, 0)
    self.assertEqual(errors, '')
    self.assertIn("'%s' offers " % self.__library_path__, said)
    self.assertRegex(said, r'offers \d+ names, \d+ of them functions\.\n$')

  def test_the_functions_containing_a_text(self) -> None:
    """With a text, each function whose readable name holds it, and its
    stored name, after a tab; data holding the text is left out."""
    code, said, errors = self._main(self.__library_path__, 'cutie')
    self.assertEqual(code, 0)
    lines = sorted(said.splitlines())
    self.assertEqual(lines, [
        'cutie::thrice(int)\t_ZN5cutie6thriceEi',
        'cutie::twice(int)\t_ZN5cutie5twiceEi',
        'cutie_alpha\tcutie_alpha',
    ])

  def test_the_wrong_number_of_arguments(self) -> None:
    """No argument, or three, prints how to use it, and gives 2."""
    for args in ((), ('a', 'b', 'c')):
      with self.subTest(args=args):
        code, said, errors = self._main(*args)
        self.assertEqual(code, 2)
        self.assertEqual(said, '')
        self.assertIn('python -m cutienator.occult FILE', errors)

  def test_run_as_a_program(self) -> None:
    """Run as 'python -m cutienator.occult', it ends with the code of
    'main'."""
    argv = ['cutienator.occult', self.__library_path__]
    with mock.patch.object(sys, 'argv', argv), \
        mock.patch.dict(sys.modules), \
        contextlib.redirect_stdout(io.StringIO()):
      #  The program runs as a fresh module, as 'python -m' runs it, not
      #  as the one this test imported.
      sys.modules.pop('cutienator.occult.__main__', None)
      with self.assertRaises(SystemExit) as caught:
        runpy.run_module('cutienator.occult', run_name='__main__')
    self.assertEqual(caught.exception.code, 0)
