"""
TestOccultSummonBuild tests 'Summon' building for real: ritual files
compiled by 'clang++' against the Qt 'qmake6' names, and joined into a
shared object Python opens, with what the compiler or the linker refuses
left out.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import os
import shutil
import tempfile
import time
import unittest
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.occult import Summon, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple

#  Ritual files made up for the builds, each of QtCore.
_GOOD = (
  '#include <QtCore/qglobal.h>\n'
  '\n'
  '//  int good()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_good() {\n'
  '  return QT_VERSION_MAJOR;\n'
  '}\n'
)
_COMPILER_REFUSES = (
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
  '  return cutie_no_such_name;\n'
  '}\n'
)
_LINKER_REFUSES = (
  '#include <QtCore/qglobal.h>\n'
  'int cutie_never_defined();\n'
  '\n'
  '//  int kept()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_kept() {\n'
  '  return 2;\n'
  '}\n'
  '\n'
  '//  int needs()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_needs() {\n'
  '  return cutie_never_defined();\n'
  '}\n'
)
_INCLUDE_REFUSED = (
  '#include <QtCore/qglobal.h>\n'
  '#include <QtCore/qcutie_no_such_header.h>\n'
  '\n'
  '//  int spared()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_spared() {\n'
  '  return 4;\n'
  '}\n'
)
#  The header that is not there is named above the first '#if', where
#  a header every ritual may need is named, so it is left out with none.
_REFUSED_WHOLE = (
  '#include <QtCore/qglobal.h>\n'
  '#include <QtCore/qcutie_no_such_header.h>\n'
  '#if 1\n'
  '#endif\n'
  '\n'
  '//  int lost()\n'
  'extern "C" Q_DECL_EXPORT\n'
  'int ritual_cutie_lost() {\n'
  '  return 3;\n'
  '}\n'
)


#  The tests marked with '_compiles' start 'clang++' for real. They run
#  where 'CUTIENATOR_TEST_COMPILES' is '1': on gcloud, and in a release
#  run on one machine of each system. Every other machine skips them,
#  so it compiles nothing.
_COMPILES = os.environ.get('CUTIENATOR_TEST_COMPILES', '') == '1'
_compiles = unittest.skipUnless(
    _COMPILES, "starts clang++: runs where CUTIENATOR_TEST_COMPILES=1")


@_compiles
class TestOccultSummonBuild(BaseTest):
  """
  Tests whole builds by 'Summon' on the machine the tests run on.

  What to know before adding a test
  ---------------------------------

  - These tests need 'clang++' and a Qt 6 with 'qmake6' on 'PATH', as
    the release workflows give every machine; they compile for real,
    a second or two a file. The rules apart from a real build are in
    'TestOccultSummon'.
  - Each test builds in a temporary folder of its own, into
    'libcutienator_QtCutie' with the ending of the system, and opens
    what it built with 'ctypes'; each ritual has a name no other test
    and no part of Qt has.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _build(self, *texts: str) -> Summon:
    """A build of ritual files of these texts, in a part's folder of a
    temporary folder, against this machine's QtCore."""
    folder = tempfile.mkdtemp()
    self.addCleanup(shutil.rmtree, folder)
    rituals = os.path.join(folder, 'QtCutieRituals')
    os.makedirs(rituals)
    files = []
    for number, text in enumerate(texts):
      path = os.path.join(rituals, 'q_cutie_%d.cpp' % number)
      with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
      files.append(path)
    system = System.getHere()
    core = os.path.join(
        Summon.getQtSharedObjectFolder(), system.getQtFileName('QtCore'))
    build = Summon()
    build.setRitualFiles(*files)
    build.setTargetFile(os.path.join(folder, 'libcutienator_QtCutie.so'))
    build.setQtSharedObjects(core)
    return build

  @staticmethod
  def _offers(build: Summon, *names: str) -> Tuple[bool, ...]:
    """Says, for each name, whether the target file offers it."""
    opened = ctypes.CDLL(build.getTargetFile())
    return (*(hasattr(opened, name) for name in names),)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BUILDS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_part_built_whole(self) -> None:
    """Every ritual is built and runs; nothing is left out, the told file
    is written and the precompiled header is gone."""
    build = self._build(_GOOD)
    self.assertEqual(build.run(), build.getTargetFile())
    opened = ctypes.CDLL(build.getTargetFile())
    self.assertEqual(opened.ritual_cutie_good(), 6)
    self.assertFalse(os.path.exists(build.getLeftOutFile()))
    self.assertEqual(build.getLeftOut(), {})
    self.assertFalse(os.path.exists(build.getPrecompiledHeaderFile()))
    with open(build.getToldFile()) as file:
      self.assertEqual(file.read(), build.getToldText())

  def test_a_ritual_the_compiler_refuses(self) -> None:
    """A ritual 'clang++' refuses is left out, with what it said; the
    other ritual of its file is built and runs."""
    build = self._build(_GOOD, _COMPILER_REFUSES)
    build.run()
    self.assertEqual(self._offers(
        build, 'ritual_cutie_good', 'ritual_cutie_fine',
        'ritual_cutie_broken'), (True, True, False))
    function, reason = build.getLeftOut()['ritual_cutie_broken']
    self.assertEqual(function, 'int broken()')
    self.assertIn('the compiler refused it', reason)
    self.assertIn('cutie_no_such_name', reason)
    self.assertEqual([*build.getLeftOut()], ['ritual_cutie_broken'])
    self.assertEqual(ctypes.CDLL(build.getTargetFile()).ritual_cutie_fine(),
                     1)

  def test_a_ritual_the_linker_refuses(self) -> None:
    """A ritual needing what no library offers is left out, naming it;
    the other ritual of its file is built and runs."""
    build = self._build(_GOOD, _LINKER_REFUSES)
    build.run()
    self.assertEqual(self._offers(
        build, 'ritual_cutie_kept', 'ritual_cutie_needs'), (True, False))
    function, reason = build.getLeftOut()['ritual_cutie_needs']
    self.assertEqual(function, 'int needs()')
    self.assertIn('the linker refused it', reason)
    self.assertIn('cutie_never_defined', reason)
    self.assertEqual(ctypes.CDLL(build.getTargetFile()).ritual_cutie_kept(),
                     2)

  def test_an_include_the_compiler_refuses(self) -> None:
    """A header that is not there, named by a line of its own, is left
    out alone, and the ritual not needing it is built; the common header
    naming it is refused, and every file is compiled without it."""
    build = self._build(_GOOD, _INCLUDE_REFUSED)
    build.run()
    self.assertEqual(self._offers(
        build, 'ritual_cutie_good', 'ritual_cutie_spared'), (True, True))
    self.assertEqual(build.getLeftOut(), {})
    record = build.getRecord()
    self.assertIn('refused the common header', record['common header'])
    entry = record['ritual files']['QtCutieRituals/q_cutie_1.cpp']
    (kind, name, first, last, reason), = entry['dropped']
    self.assertEqual((kind, name, first, last), (
        'include', '<QtCore/qcutie_no_such_header.h>', 2, 2))
    self.assertIn('qcutie_no_such_header.h', reason)
    self.assertIsNone(entry['whole'])

  def test_a_ritual_file_refused_whole(self) -> None:
    """A file refused for what none of its items can be left out for
    is left out whole, its rituals with it; the other files are built."""
    build = self._build(_GOOD, _REFUSED_WHOLE)
    build.run()
    self.assertEqual(self._offers(
        build, 'ritual_cutie_good', 'ritual_cutie_lost'), (True, False))
    function, reason = build.getLeftOut()['ritual_cutie_lost']
    self.assertEqual(function, 'int lost()')
    self.assertIn('no ritual of it holds alone', reason)
    self.assertIn('qcutie_no_such_header.h', reason)
    record = build.getRecord()
    entry = record['ritual files']['QtCutieRituals/q_cutie_1.cpp']
    self.assertIsNotNone(entry['whole'])

  def test_a_second_build_compiles_only_what_changed(self) -> None:
    """Built once, a second build compiles nothing and joins again; a
    file changed since is compiled alone, and what was left out of the
    others stays left out."""
    build = self._build(_GOOD, _COMPILER_REFUSES)
    build.run()
    with mock.patch.object(build, '_compile', wraps=build._compile) as made:
      build.run()
    made.assert_not_called()
    self.assertEqual([*build.getLeftOut()], ['ritual_cutie_broken'])
    first, second = build.getRitualFiles()
    later = time.time() + 100
    os.utime(first, (later, later))
    with mock.patch.object(build, '_compile', wraps=build._compile) as made:
      build.run()
    made.assert_called_once_with(first)
    self.assertEqual([*build.getLeftOut()], ['ritual_cutie_broken'])
    self.assertEqual(self._offers(build, 'ritual_cutie_good'), (True,))
