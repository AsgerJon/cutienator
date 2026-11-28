"""
TestOccultRituals tests the rules of 'Rituals', which opens cutienator's
own shared objects and runs their rituals, against ritual files and a Qt
made up for each test.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import json
import os
import shutil
import subprocess
import tempfile
import time
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator.occult import Linux, MacOS, Rituals, Summon, System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Sequence

#  What 'Rituals' keeps on the class, each put back to nothing for a test.
_KEPT = dict(
  __ritual_sigils__=None, __ritual_parts__=None, __parts_first__=None,
  __qt_dependencies__=None, __kept_exception__=None, __kept_given__=None,
)
_FRESH = (
  '__opened_targets__', '__missing_rituals__', '__left_out_rituals__',
  '__seen_parts__',
)
#  The four rituals text crosses by, and the one that stops the loop.
_TEXT = (
  'ritual_ZN7QStringC1EPK5QCharx', 'ritual_ZNK7QString4sizeEv',
  'ritual_ZNK7QString9constDataEv', 'ritual_ZN7QStringD1Ev',
)
_STOP = 'ritual_ZN16QCoreApplication4exitEi'
#  A small library of rituals, compiled by the tests that open one.
_LIBRARY = """
extern "C" int ritual_cutie_plus(int x) { return x + 1; }
extern "C" double ritual_cutie_half(double x) { return x / 2; }
"""


class TestOccultRituals(BaseTest):
  """
  Tests each rule of 'Rituals' on a package and a Qt made up for the
  test.

  What to know before adding a test
  ---------------------------------

  - 'setUp' makes, in a temporary folder, a folder of ritual files that
    'getRitualFolder' gives, and a Qt that the answers of 'qmake6' in
    'Summon' name; 'System' is 'Linux'. Everything 'Rituals' keeps on
    the class starts empty, and is put back when the test ends, so the
    real package is not touched. '_ritual' writes a ritual file and its
    sigil file; '_qt' gives the made-up Qt a part.
  - A test that opens a target file compiles '_LIBRARY' with 'clang++'
    ('_compile'); Qt's own files are empty there, so opening them is
    replaced.
  - The real package, its target files and Qt are tested by
    'TestOccultRitualsReal'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SET UP   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setUp(self) -> None:
    """A made-up package and Qt, and nothing kept."""
    super().setUp()
    self.root = tempfile.mkdtemp()
    self.addCleanup(shutil.rmtree, self.root)
    self.rituals = os.path.join(self.root, 'occult', 'rituals')
    os.makedirs(self.rituals)
    self.lib = os.path.join(self.root, 'qt', 'lib')
    self.include = os.path.join(self.root, 'qt', 'include')
    self.modules = os.path.join(self.root, 'qt', 'modules')
    for folder in (self.lib, self.include, self.modules):
      os.makedirs(folder)
    patches = [
      mock.patch.object(Rituals, 'getRitualFolder',
                        return_value=self.rituals),
      mock.patch.object(Summon, '__qt_shared_object_folder__', self.lib),
      mock.patch.object(Summon, '__qt_header_folder__', self.include),
      mock.patch.object(Summon, '__qt_module_folder__', self.modules),
      mock.patch.object(System, '__system_here__', Linux()),
      *(mock.patch.object(Rituals, name, value)
        for name, value in _KEPT.items()),
      *(mock.patch.object(Rituals, name, dict()) for name in _FRESH),
      mock.patch.object(Rituals, '__start_texts__', []),
    ]
    for patcher in patches:
      patcher.start()
      self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _ritual(
      self,
      part: str,
      stem: str,
      sigils: Dict[str, Sequence[str]],
      first: Optional[Sequence[str]] = None,
      ending: str = '.cpp',
  ) -> str:
    """Writes a ritual file of a part and its sigil file, and gives the
    path of the ritual file."""
    folder = os.path.join(self.rituals, '%sRituals' % part)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, stem + ending)
    with open(path, 'w', encoding='utf-8') as file:
      file.write('//  made up\n')
    written = dict(about=[], sigils={k: [*v] for k, v in sigils.items()})
    if first is not None:
      written['parts first'] = [*first]
    with open(os.path.join(folder, stem + '.json'), 'w') as file:
      json.dump(written, file)
    return path

  def _qt(self, part: str, kind: str = 'shared') -> None:
    """Gives the made-up Qt a part: its shared object, its static library
    with a '.prl' file saying so, or its headers alone."""
    linux = Linux()
    if kind == 'shared':
      open(os.path.join(self.lib, linux.getQtFileName(part)), 'w').close()
    elif kind == 'static':
      open(os.path.join(
          self.lib, linux.getQtStaticFileName(part)), 'w').close()
      with open(os.path.join(self.lib, linux.getQtPrlFileName(part)),
                'w') as file:
        file.write('QMAKE_PRL_CONFIG = static\n'
                   'QMAKE_PRL_LIBS = -lole32 -framework Metal -lm\n')
    os.makedirs(os.path.join(self.include, part), exist_ok=True)

  def _compile(self, part: str) -> str:
    """Compiles '_LIBRARY' into the target file of a part."""
    source = os.path.join(self.root, 'library.cpp')
    with open(source, 'w') as file:
      file.write(_LIBRARY)
    target = Rituals.getTargetFile(part)
    subprocess.run(
        ('clang++', '-shared', '-fPIC', '-o', target, source), check=True)
    return target

  def _openable(self) -> None:
    """Has the opening of Qt's files do nothing, as they are empty."""
    patcher = mock.patch.object(Linux, 'prepareOpening')
    patcher.start()
    self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  FOLDERS AND FILES  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_folder_of_a_part(self) -> None:
    """The ritual files of a part lie in a folder named after it."""
    self.assertEqual(Rituals.getPartFolder('QtCore'),
                     os.path.join(self.rituals, 'QtCoreRituals'))

  def test_the_ritual_files(self) -> None:
    """Every '.cpp' and '.mm' in a folder of rituals, in order; other
    files, and files of other folders, are passed by."""
    b = self._ritual('QtCore', 'q_b', {})
    a = self._ritual('QtCore', 'q_a', {})
    mm = self._ritual('QtCore', 'q_m__objc', {}, ending='.mm')
    g = self._ritual('QtGui', 'q_g', {})
    os.makedirs(os.path.join(self.rituals, 'Other'))
    open(os.path.join(self.rituals, 'Other', 'x.cpp'), 'w').close()
    open(os.path.join(self.rituals, 'QtCoreRituals', 'x.txt'), 'w').close()
    self.assertEqual(Rituals.getRitualFiles(), tuple(sorted((a, b, mm, g))))
    self.assertEqual(Rituals.getPartRitualFiles('QtCore'), (a, b, mm))
    self.assertEqual(Rituals.getPartRitualFiles('QtMissing'), ())

  def test_objective_c_is_compiled_on_macos_alone(self) -> None:
    """The '.mm' files are compiled where Objective-C++ is built."""
    cpp = self._ritual('QtCore', 'q_a', {})
    mm = self._ritual('QtCore', 'q_m__objc', {}, ending='.mm')
    self.assertEqual(Rituals.getPartCompiledFiles('QtCore'), (cpp,))
    with mock.patch.object(System, '__system_here__', MacOS()):
      self.assertEqual(Rituals.getPartCompiledFiles('QtCore'), (cpp, mm))

  def test_the_part_of_a_ritual_file(self) -> None:
    """The part of a ritual file is the name of its folder."""
    self.assertEqual(Rituals._getPartOf('/r/QtGuiRituals/q_a.cpp'), 'QtGui')

  def test_the_target_file_of_a_part(self) -> None:
    """The target file lies beside the folder of rituals; a part that is
    no 'str' is refused."""
    self.assertEqual(Rituals.getTargetFile('QtCore'), os.path.join(
        self.root, 'occult', 'libcutienator_QtCore.so'))
    with self.assertRaises(TypeException):
      Rituals.getTargetFile(None)

  def test_the_parts_of_the_rituals(self) -> None:
    """A part is each folder 'Qt*Rituals'; a file of that name is no
    part."""
    self._ritual('QtGui', 'q_a', {})
    self._ritual('QtCore', 'q_a', {})
    open(os.path.join(self.rituals, 'QtFakeRituals'), 'w').close()
    self.assertEqual(Rituals.getRitualParts(), ('QtCore', 'QtGui'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE PARTS QT HAS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _parts(self) -> None:
    """Five parts with ritual files: a shared one, a static one, one of
    headers alone, one with neither, and one more shared."""
    for part in ('QtCore', 'QtAx', 'QtHeads', 'QtGone', 'QtGui'):
      self._ritual(part, 'q_a', {})
    self._qt('QtCore')
    self._qt('QtAx', 'static')
    self._qt('QtHeads', 'headers')
    self._qt('QtGui')

  def test_the_parts_installed(self) -> None:
    """A part is installed when its shared object, its static library or
    its headers are there; the built parts are those of them, and their
    ritual files and target files."""
    self._parts()
    installed = ('QtAx', 'QtCore', 'QtGui', 'QtHeads')
    self.assertEqual(Rituals.getInstalledParts(), installed)
    self.assertEqual(Rituals.getBuiltParts(), installed)
    self.assertEqual(
        [Rituals._getPartOf(f) for f in Rituals.getBuiltRitualFiles()],
        [*installed])
    self.assertEqual(Rituals.getTargetFiles(), tuple(
        Rituals.getTargetFile(part) for part in installed))

  def test_the_parts_installed_without_headers(self) -> None:
    """When Qt's header folder cannot be asked for, only parts with a
    file are installed."""
    self._parts()
    with mock.patch.object(Summon, '__qt_header_folder__', None), \
        mock.patch.object(Summon, '_run', side_effect=FileNotFoundError):
      self.assertEqual(
          Rituals.getInstalledParts(), ('QtAx', 'QtCore', 'QtGui'))

  def test_the_files_of_qt(self) -> None:
    """The file of a part is its shared object, else its static library,
    else none; the shared objects are those of the parts that have one."""
    self._parts()
    self.assertEqual(Rituals._findQtFile('QtCore'),
                     os.path.join(self.lib, 'libQt6Core.so.6'))
    self.assertEqual(Rituals._findQtFile('QtAx'),
                     os.path.join(self.lib, 'libQt6Ax.a'))
    self.assertIsNone(Rituals._findQtFile('QtHeads'))
    self.assertEqual(Rituals.getQtSharedObjects(), (
        os.path.join(self.lib, 'libQt6Ax.a'),
        os.path.join(self.lib, 'libQt6Core.so.6'),
        os.path.join(self.lib, 'libQt6Gui.so.6')))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE ORDER OF THE PARTS   # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_reading_the_modules_of_qt(self) -> None:
    """Each part needs the parts its modules and their private modules
    need, nearest first, without itself; a module with no name is
    passed through, and lines of another shape passed by."""
    with open(os.path.join(self.modules, 'qt_lib_alpha.pri'), 'w') as f:
      f.write('\n'.join((
          'QT.alpha.VERSION = 6.12.0',
          'QT.alpha.name = QtAlpha',
          'QT.alpha.depends = core gamma',
          'QT.alpha_private.name = QtAlpha',
          'QT.alpha_private.run_depends = beta alpha',
          'QT_MODULES += alpha',
          'QT.alpha.x.y = z',
          'QX.alpha.name = Nothing',
      )))
    with open(os.path.join(self.modules, 'qt_lib_core.pri'), 'w') as f:
      f.write('QT.core.name = QtCore\n')
    with open(os.path.join(self.modules, 'qt_lib_gamma.pri'), 'w') as f:
      f.write('QT.gamma.name = QtGamma\nQT.gamma.depends = core\n')
    with open(os.path.join(self.modules, 'beta.txt'), 'w') as f:
      f.write('QT.beta.name = QtBeta\n')
    self.assertEqual(Rituals.readQtModules(self.modules), dict(
        QtAlpha=('QtCore', 'QtGamma'), QtCore=(), QtGamma=('QtCore',)))

  def test_the_dependencies_are_read_once(self) -> None:
    """The modules are read at the first question, and kept."""
    with open(os.path.join(self.modules, 'qt_lib_gui.pri'), 'w') as f:
      f.write('QT.gui.name = QtGui\nQT.gui.depends = core\n'
              'QT.core.name = QtCore\n')
    self.assertEqual(Rituals.getQtDependencies('QtGui'), ('QtCore',))
    with mock.patch.object(Rituals, 'readQtModules') as read:
      self.assertEqual(Rituals.getQtDependencies('QtMissing'), ())
    read.assert_not_called()

  def _ordered(self) -> None:
    """A part QtAlpha that sees QtBeta and QtEps first and needs QtGamma
    by Qt's modules; QtDelta and QtEps are static, QtZeta has headers
    alone."""
    self._ritual('QtAlpha', 'q_a', {}, first=('QtBeta', 'QtEps'))
    for part in ('QtBeta', 'QtGamma', 'QtDelta', 'QtEps', 'QtZeta'):
      self._ritual(part, 'q_a', {})
    for part in ('QtAlpha', 'QtBeta', 'QtGamma'):
      self._qt(part)
    self._qt('QtDelta', 'static')
    self._qt('QtEps', 'static')
    self._qt('QtZeta', 'headers')
    with open(os.path.join(self.modules, 'qt_lib_alpha.pri'), 'w') as f:
      f.write('QT.alpha.name = QtAlpha\nQT.alpha.depends = gamma\n'
              'QT.gamma.name = QtGamma\n')

  def test_the_order_a_part_sees_the_parts_in(self) -> None:
    """Itself, the parts its sigil files name first, then every other
    part installed."""
    self._ordered()
    self.assertEqual(Rituals.getPartsFirst('QtAlpha'), ('QtBeta', 'QtEps'))
    self.assertEqual(Rituals.getPartOrder('QtAlpha'), (
        'QtAlpha', 'QtBeta', 'QtEps', 'QtDelta', 'QtGamma', 'QtZeta'))

  def test_the_parts_a_target_file_is_joined_to(self) -> None:
    """Every part in its order with a file, but a static library it
    does not need."""
    self._ordered()
    self.assertEqual(Rituals.getJoinedParts('QtAlpha'),
                     ('QtAlpha', 'QtBeta', 'QtEps', 'QtGamma'))
    self.assertEqual(Rituals.getPartSharedObjects('QtAlpha'), (
        os.path.join(self.lib, 'libQt6Alpha.so.6'),
        os.path.join(self.lib, 'libQt6Beta.so.6'),
        os.path.join(self.lib, 'libQt6Eps.a'),
        os.path.join(self.lib, 'libQt6Gamma.so.6')))

  def test_what_a_static_library_needs_beside_it(self) -> None:
    """The words of each static library joined, each once, but each
    '-framework' with the framework after it."""
    self._ordered()
    with open(os.path.join(self.lib, 'libQt6Beta.prl'), 'w') as file:
      file.write('QMAKE_PRL_CONFIG = static\n'
                 'QMAKE_PRL_LIBS = -lm -framework Metal -framework Foo\n')
    self.assertEqual(Rituals.getPartStaticDependencies('QtAlpha'), (
        '-lm', '-framework', 'Metal', '-framework', 'Foo', '-lole32',
        '-framework', 'Metal'))

  def test_the_parts_a_build_looks_in(self) -> None:
    """Itself, the parts it sees first, the parts it needs, then every
    part of Qt's header folder."""
    self._ordered()
    os.makedirs(os.path.join(self.include, 'QtOnlyHeaders'))
    self.assertEqual(Rituals.getPartComponents('QtAlpha'), (
        'QtAlpha', 'QtBeta', 'QtEps', 'QtGamma', 'QtDelta', 'QtOnlyHeaders',
        'QtZeta'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE SIGILS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_sigils_of_a_part(self) -> None:
    """Each ritual's sigil as a 'tuple', by part; the sigil file of each
    ritual file beside it."""
    a = self._ritual('QtCore', 'q_a', dict(ritual_a=['int', 'address']))
    self._ritual('QtCore', 'q_b', dict(ritual_b=['nothing']))
    self.assertEqual(Rituals.getSigils('QtCore'), dict(
        ritual_a=('int', 'address'), ritual_b=('nothing',)))
    self.assertEqual(Rituals.getSigilFiles()[0],
                     os.path.splitext(a)[0] + '.json')

  def test_a_ritual_two_parts_list(self) -> None:
    """A ritual two parts list is of both; one listed by none is of no
    part; every name is given once."""
    self._ritual('QtCharts', 'q_bar', dict(ritual_bar=['nothing']))
    self._ritual('QtGraphs', 'q_bar', dict(ritual_bar=['nothing'],
                                           ritual_own=['int']))
    self.assertEqual(Rituals.getPartsOf('ritual_bar'),
                     ('QtCharts', 'QtGraphs'))
    self.assertEqual(Rituals.getPartsOf('ritual_gone'), ())
    self.assertEqual(sorted(Rituals.getRitualNames()),
                     ['ritual_bar', 'ritual_own'])

  def test_the_names_and_parts_read_when_first_asked(self) -> None:
    """Asking for the parts of a ritual or every name reads the sigil
    files first, once."""
    self._ritual('QtCore', 'q_a', dict(ritual_a=['nothing']))
    self.assertEqual(Rituals.getRitualNames(), ('ritual_a',))
    with mock.patch.object(Rituals, '__ritual_parts__', None):
      self.assertEqual(Rituals.getPartsOf('ritual_a'), ('QtCore',))

  def test_a_part_with_no_folder(self) -> None:
    """Asking for the sigils of a part with no folder raises."""
    self._ritual('QtCore', 'q_a', {})
    with self.assertRaises(LookupError) as caught:
      Rituals.getSigils('QtMissing')
    self.assertIn("'QtMissing'", str(caught.exception))

  def test_sigils_never_read_do_not_loop(self) -> None:
    """When reading leaves no sigils, asking raises, not loops."""
    with mock.patch.object(Rituals, '_createSigils'):
      with self.assertRaises(RecursionError):
        Rituals.getSigils('QtCore')

  def test_a_ritual_file_without_sigil_file(self) -> None:
    """A ritual file alone says nothing of its rituals, and is refused."""
    path = self._ritual('QtCore', 'q_alone', {})
    os.remove(os.path.splitext(path)[0] + '.json')
    with self.assertRaises(FileNotFoundError) as caught:
      Rituals.getSigils('QtCore')
    self.assertIn('q_alone.json', str(caught.exception))

  def test_a_word_of_no_sigil(self) -> None:
    """A sigil may hold the words 'Rituals' knows, and no other."""
    self._ritual('QtCore', 'q_a', dict(ritual_a=['int', 'pointer']))
    with self.assertRaises(ValueError) as caught:
      Rituals.getSigils('QtCore')
    self.assertIn("'pointer'", str(caught.exception))

  def test_a_ritual_listed_twice_in_a_part(self) -> None:
    """Two sigil files of one part listing one ritual are refused."""
    self._ritual('QtCore', 'q_a', dict(ritual_twice=['nothing']))
    self._ritual('QtCore', 'q_b', dict(ritual_twice=['nothing']))
    with self.assertRaises(ValueError) as caught:
      Rituals.getSigils('QtCore')
    self.assertIn("'ritual_twice'", str(caught.exception))

  def test_two_orders_of_one_part(self) -> None:
    """Sigil files of one part saying two orders of the parts are
    refused; one saying nothing sees no part first."""
    self._ritual('QtGraphs', 'q_a', {}, first=('QtGui',))
    self._ritual('QtGraphs', 'q_b', {}, first=('QtQuick',))
    with self.assertRaises(ValueError) as caught:
      Rituals.getSigils('QtGraphs')
    self.assertIn("'parts first'", str(caught.exception))

  def test_a_part_that_says_nothing_first(self) -> None:
    """A part whose sigil files name no part first sees none, and an
    empty folder of rituals sees none either."""
    self._ritual('QtCore', 'q_a', {})
    os.makedirs(os.path.join(self.rituals, 'QtEmptyRituals'))
    self.assertEqual(Rituals.getPartsFirst('QtCore'), ())
    self.assertEqual(Rituals.getPartsFirst('QtEmpty'), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STALE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_stale_until_every_target_file_is_newer(self) -> None:
    """Stale while a built part has no target file, or one older than a
    ritual file it compiles; else not; nothing built is not stale."""
    self.assertIs(Rituals.isStale(), False)
    ritual = self._ritual('QtCore', 'q_a', {})
    self._qt('QtCore')
    self.assertIs(Rituals.isStale(), True)
    target = Rituals.getTargetFile('QtCore')
    open(target, 'w').close()
    earlier = time.time() - 100
    os.utime(ritual, (earlier, earlier))
    self.assertIs(Rituals.isStale(), False)
    later = time.time() + 100
    os.utime(ritual, (later, later))
    self.assertIs(Rituals.isStale(), True)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPENING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _opened(self) -> None:
    """A part QtCute whose target file offers two of its three rituals,
    and a QtCore with the rituals of text and the loop."""
    self._ritual('QtCute', 'q_a', dict(
        ritual_cutie_plus=['int', 'int'],
        ritual_cutie_half=['double', 'double'],
        ritual_cutie_gone=['nothing']))
    self._ritual('QtCore', 'q_string', {
        name: ['nothing'] for name in (*_TEXT, _STOP)})
    self._qt('QtCute')
    self._qt('QtCore')
    self._compile('QtCute')
    self._openable()

  def test_opening_a_target_file(self) -> None:
    """Each ritual offered is readied by its sigil; one not offered is
    missing; the Qt files of the part are opened first, once."""
    self._opened()
    opened = Rituals.getOpened('QtCute')
    self.assertIs(Rituals.getOpened('QtCute'), opened)
    self.assertEqual(opened.ritual_cutie_plus.restype, ctypes.c_int)
    self.assertEqual(opened.ritual_cutie_half.argtypes, [ctypes.c_double])
    self.assertEqual(Rituals.getMissing('QtCute'),
                     frozenset({'ritual_cutie_gone'}))
    Linux.prepareOpening.assert_called_once_with(
        os.path.join(self.lib, 'libQt6Cute.so.6'))

  def test_the_missing_of_a_part_not_installed(self) -> None:
    """Every ritual of a part not installed is missing, and nothing is
    opened."""
    self._ritual('QtFar', 'q_a', dict(ritual_far=['nothing']))
    self.assertEqual(Rituals.getMissing('QtFar'), frozenset({'ritual_far'}))
    self.assertEqual(Rituals.__opened_targets__, {})

  def test_opening_a_part_not_installed(self) -> None:
    """A part this Qt lacks has nothing to open."""
    self._ritual('QtFar', 'q_a', dict(ritual_far=['nothing']))
    with self.assertRaises(LookupError) as caught:
      Rituals.getOpened('QtFar')
    self.assertIn('QtFar is not installed', str(caught.exception))

  def test_opening_a_part_not_built(self) -> None:
    """A part installed whose target file is not there says to summon."""
    self._ritual('QtCute', 'q_a', dict(ritual_a=['nothing']))
    self._qt('QtCute')
    with self.assertRaises(FileNotFoundError) as caught:
      Rituals.getOpened('QtCute')
    self.assertIn('Rituals.summon()', str(caught.exception))

  def test_opening_that_leaves_nothing_does_not_loop(self) -> None:
    """When opening leaves nothing open, asking raises, not loops."""
    with mock.patch.object(Rituals, '_createOpened'):
      with self.assertRaises(RecursionError):
        Rituals.getOpened('QtCore')

  def test_text_needs_the_rituals_of_qstring(self) -> None:
    """A part with rituals of text needs QtCore to list the four rituals
    text crosses by; one with no text needs nothing."""
    self._ritual('QtCute', 'q_a', dict(ritual_t=['text', 'address']))
    self._ritual('QtPlain', 'q_a', dict(ritual_p=['int']))
    self._ritual('QtCore', 'q_string', {_TEXT[0]: ['address']})
    Rituals._checkTextRituals('QtPlain')
    with self.assertRaises(LookupError) as caught:
      Rituals._checkTextRituals('QtCute')
    self.assertIn("'%s'" % _TEXT[1], str(caught.exception))

  def test_qtcore_must_offer_the_rituals_of_text(self) -> None:
    """A target file of QtCore not offering a ritual of text is refused
    when opened."""
    self._ritual('QtCore', 'q_string', {
        name: ['nothing'] for name in (*_TEXT, 'ritual_cutie_plus')})
    self._qt('QtCore')
    self._compile('QtCore')
    self._openable()
    with self.assertRaises(LookupError) as caught:
      Rituals.getOpened('QtCore')
    self.assertIn("'%s'" % _TEXT[0], str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CALLING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_calling_a_ritual(self) -> None:
    """A ritual runs, by its name alone or from its part."""
    self._opened()
    self.assertEqual(Rituals.call('ritual_cutie_plus', 41), 42)
    self.assertEqual(
        Rituals.callFrom('QtCute', 'ritual_cutie_half', 5.0), 2.5)

  def test_a_ritual_compiled_out_here(self) -> None:
    """A ritual the target file does not offer, with no reason left
    out, stands under Qt's own '#if' and raises when called."""
    self._opened()
    with self.assertRaises(NotImplementedError) as caught:
      Rituals.call('ritual_cutie_gone')
    self.assertIn("Qt's own '#if' lines", str(caught.exception))

  def test_a_ritual_left_out_here(self) -> None:
    """A ritual 'summon' left out raises with the function and why."""
    self._opened()
    leftOut = Summon.getLeftOutFileOf(Rituals.getTargetFile('QtCute'))
    with open(leftOut, 'w') as file:
      json.dump({'ritual files': {'QtCuteRituals/q_a.cpp': dict(leftOut={
          'ritual_cutie_gone': ['void gone()', 'the linker refused it']})}},
          file)
    with self.assertRaises(NotImplementedError) as caught:
      Rituals.call('ritual_cutie_gone')
    said = str(caught.exception)
    self.assertIn("'void gone()' cannot be called", said)
    self.assertIn('the linker refused it', said)
    self.assertEqual(Rituals.getLeftOut('QtCute'), {
        'ritual_cutie_gone': ('void gone()', 'the linker refused it')})

  def test_a_ritual_of_a_part_not_installed(self) -> None:
    """A ritual of a part this Qt lacks raises when called."""
    self._ritual('QtFar', 'q_a', dict(ritual_far=['nothing']))
    with self.assertRaises(NotImplementedError) as caught:
      Rituals.call('ritual_far')
    self.assertIn('QtFar, which is not installed', str(caught.exception))

  def test_a_ritual_of_a_part_not_built(self) -> None:
    """A ritual of a part whose target file is not there raises when
    called, with the reason its placeholder gives, or saying to
    summon."""
    self._ritual('QtCute', 'q_a', dict(ritual_a=['nothing']))
    self._qt('QtCute')
    with self.assertRaises(NotImplementedError) as caught:
      Rituals.call('ritual_a')
    self.assertIn('has not been summoned here', str(caught.exception))
    Summon.writeNotBuilt(
        Summon.getLeftOutFileOf(Rituals.getTargetFile('QtCute')),
        'Qt has no QtCuteCore here')
    with self.assertRaises(NotImplementedError) as caught:
      Rituals.call('ritual_a')
    self.assertIn('Qt has no QtCuteCore here', str(caught.exception))

  def test_a_ritual_raises_what_was_kept(self) -> None:
    """An exception kept while a ritual ran is raised once it is back."""
    self._opened()
    problem = KeyError('kept')
    Rituals.__kept_exception__ = problem
    with self.assertRaises(KeyError) as caught:
      Rituals.call('ritual_cutie_plus', 1)
    self.assertIs(caught.exception, problem)
    self.assertIs(Rituals.hasKeptException(), False)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHICH PART RUNS A RITUAL   # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _shared(self) -> None:
    """A ritual of QtCharts and of QtGraphs, QtGraphsWidgets seeing
    QtGraphs first, QtDataVis seeing neither."""
    for part in ('QtCharts', 'QtGraphs'):
      self._ritual(part, 'q_bar', dict(ritual_bar=['nothing']))
    self._ritual('QtGraphsWidgets', 'q_w', {}, first=('QtGraphs',))
    self._ritual('QtDataVis', 'q_d', {})
    self._ritual('QtCore', 'q_one', dict(ritual_one=['nothing']))
    for part in ('QtCharts', 'QtGraphs', 'QtGraphsWidgets', 'QtCore'):
      self._qt(part)

  def test_a_ritual_of_one_part(self) -> None:
    """A ritual one part lists is of that part, from anywhere."""
    self._shared()
    self.assertEqual(Rituals._findPart('ritual_one', None), 'QtCore')
    self.assertEqual(Rituals._findPart('ritual_one', 'QtGraphs'), 'QtCore')

  def test_a_ritual_of_no_part(self) -> None:
    """A ritual no part lists is a gap: NotImplementedError, naming it,
    from anywhere."""
    self._shared()
    for seenFrom in (None, 'QtGraphs'):
      with self.subTest(seenFrom=seenFrom):
        with self.assertRaises(NotImplementedError) as caught:
          Rituals._findPart('ritual_gone', seenFrom)
        said = str(caught.exception)
        self.assertIn("'ritual_gone'", said)
        self.assertIn('ships no ritual of that name', said)

  def test_a_ritual_of_two_parts_seen_from_one(self) -> None:
    """A ritual two parts list is of the first of them its part sees,
    found once and kept."""
    self._shared()
    self.assertEqual(
        Rituals._findPart('ritual_bar', 'QtGraphsWidgets'), 'QtGraphs')
    self.assertEqual(Rituals._findPart('ritual_bar', 'QtCharts'),
                     'QtCharts')
    with mock.patch.object(Rituals, 'getPartOrder') as order:
      self.assertEqual(
          Rituals._findPart('ritual_bar', 'QtGraphsWidgets'), 'QtGraphs')
    order.assert_not_called()

  def test_a_ritual_of_two_parts_neither_installed(self) -> None:
    """Seen from a part that sees neither part installed, it is refused."""
    self._shared()
    with mock.patch.object(Rituals, 'getPartOrder',
                           return_value=('QtDataVis',)):
      with self.assertRaises(LookupError) as caught:
        Rituals._findPart('ritual_bar', 'QtDataVis')
    self.assertIn('none is installed here', str(caught.exception))

  def test_a_ritual_of_two_parts_seen_from_none(self) -> None:
    """Called by its name alone, a ritual two parts list is refused,
    naming both and 'callFrom'."""
    self._shared()
    with self.assertRaises(LookupError) as caught:
      Rituals.call('ritual_bar')
    said = str(caught.exception)
    self.assertIn('QtCharts and QtGraphs', said)
    self.assertIn("'callFrom'", said)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _textual(self) -> Any:
    """Replaces making, reading and dropping a text, and gives the three
    stand-ins: each text made is a number, read back as 'read N'."""
    made = mock.patch.object(
        Rituals, '_makeText', side_effect=lambda text: 1000 + len(text))
    read = mock.patch.object(
        Rituals, '_readText', side_effect=lambda address: 'read %d' % (
            address,))
    drop = mock.patch.object(Rituals, '_dropText')
    stand = (made.start(), read.start(), drop.start())
    self.addCleanup(mock.patch.stopall)
    return stand

  def test_a_ritual_taking_text(self) -> None:
    """Each 'str' where the sigil says text is made a text, passed, and
    dropped after; the other arguments pass as they are."""
    made, read, drop = self._textual()
    ritual = mock.Mock(return_value=7)
    back = Rituals._callWithText(
        ritual, ('int', 'address', 'text', 'int'), (5, 'cute', 9, 'extra'))
    self.assertEqual(back, 7)
    ritual.assert_called_once_with(5, 1004, 9, 'extra')
    drop.assert_called_once_with(1004)
    read.assert_not_called()

  def test_a_ritual_giving_text(self) -> None:
    """A text given back is read as a 'str', and dropped."""
    made, read, drop = self._textual()
    ritual = mock.Mock(return_value=2000)
    back = Rituals._callWithText(ritual, ('text', 'address'), (5,))
    self.assertEqual(back, 'read 2000')
    drop.assert_called_once_with(2000)

  def test_the_texts_made_are_dropped_when_it_raises(self) -> None:
    """When the ritual raises, every text made is dropped all the same."""
    made, read, drop = self._textual()
    ritual = mock.Mock(side_effect=RuntimeError('broke'))
    with self.assertRaises(RuntimeError):
      Rituals._callWithText(ritual, ('nothing', 'text', 'text'), ('a', 'bc'))
    self.assertEqual(drop.call_args_list, [mock.call(1001), mock.call(1002)])

  def test_a_text_must_be_a_str(self) -> None:
    """A text made of what is no 'str' is refused before anything runs."""
    with self.assertRaises(TypeException):
      Rituals._makeText(b'bytes')

  def test_the_texts_a_program_was_started_with(self) -> None:
    """The texts are kept as Qt takes them, a count and a list ending in
    nothing, and the two addresses given; what is no list of 'str' is
    refused."""
    count, texts = Rituals.keepStartTexts(['cutie', 'rätsel'])
    self.assertEqual(ctypes.c_int.from_address(count).value, 2)
    listed = (ctypes.c_char_p * 3).from_address(texts)
    self.assertEqual(
        [*listed], ['cutie'.encode(), 'rätsel'.encode(), None])
    self.assertEqual(len(Rituals.__start_texts__), 1)
    self.assertEqual(len(Rituals.keepStartTexts(('a',))), 2)
    with self.assertRaises(TypeException):
      Rituals.keepStartTexts('cutie')
    with self.assertRaises(TypeException):
      Rituals.keepStartTexts(['cutie', 3])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PYTHON CALLED BY QT  # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_python_function_c_can_call(self) -> None:
    """A Python function made into one of C takes the object, what the
    sigil says, and where to say it handled the call."""
    self._ritual('QtCore', 'q_app', {_STOP: ['nothing', 'int']})
    call = Rituals.createCall(
        'int', ('int', 'double'), lambda this, x, y, handled: x + int(y))
    self.assertIsInstance(call, ctypes._CFuncPtr)
    self.assertEqual(call(None, 40, 2.0, None), 42)

  def test_a_python_function_of_text_or_unknown_words(self) -> None:
    """Text, and words that are none of a sigil's, are refused."""
    self._ritual('QtCore', 'q_app', {_STOP: ['nothing', 'int']})
    for gives, takes in (('text', ()), ('int', ('text',)),
                         ('pointer', ()), ('int', ('vector',))):
      with self.subTest(gives=gives, takes=takes):
        with self.assertRaises(ValueError):
          Rituals.createCall(gives, takes, print)

  def test_a_python_function_needs_the_ritual_of_the_loop(self) -> None:
    """Without the ritual that stops Qt's loop, a Python function cannot
    be handed to Qt."""
    self._ritual('QtCore', 'q_other', dict(ritual_other=['nothing']))
    with self.assertRaises(LookupError) as caught:
      Rituals.createCall('int', (), print)
    self.assertIn("'%s'" % _STOP, str(caught.exception))

  def test_an_exception_raised_while_qt_called_python(self) -> None:
    """The first exception is kept and Qt's loop is told to stop; a
    later one is not kept; raising it gives it back once."""
    opened = mock.Mock()
    first, later = ValueError('first'), ValueError('later')
    with mock.patch.object(Rituals, 'getOpened', return_value=opened):
      self.assertIs(Rituals.hasKeptException(), False)
      Rituals.keepException(first)
      Rituals.keepException(later)
    getattr(opened, _STOP).assert_called_once_with(1)
    self.assertIs(Rituals.hasKeptException(), True)
    with self.assertRaises(ValueError) as caught:
      Rituals._raiseKept()
    self.assertIs(caught.exception, first)
    self.assertIs(Rituals.hasKeptException(), False)
    Rituals._raiseKept()

  def test_what_a_python_function_gave(self) -> None:
    """What a function called by Qt gave is kept."""
    given = object()
    Rituals.keepGiven(given)
    self.assertIs(Rituals.__kept_given__, given)

  def test_text_handed_to_and_from_python(self) -> None:
    """'takeText' and 'giveText' read and make a text of Qt."""
    with mock.patch.object(Rituals, '_readText', return_value='cute'), \
        mock.patch.object(Rituals, '_makeText', return_value=7) as make:
      self.assertEqual(Rituals.takeText(9), 'cute')
      self.assertEqual(Rituals.giveText('cute'), 7)
    make.assert_called_once_with('cute')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SUMMONING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_summon_of_a_part(self) -> None:
    """A part's build is told its ritual files, its target file, its
    files of Qt, what static libraries need and the parts it looks in."""
    self._ordered()
    build = Rituals.createPartSummon('QtAlpha')
    self.assertEqual(build.getRitualFiles(),
                     Rituals.getPartCompiledFiles('QtAlpha'))
    self.assertEqual(build.getTargetFile(), Rituals.getTargetFile('QtAlpha'))
    self.assertEqual(build.getQtSharedObjects(),
                     Rituals.getPartSharedObjects('QtAlpha'))
    self.assertEqual(build.getStaticDependencies(),
                     Rituals.getPartStaticDependencies('QtAlpha'))
    self.assertEqual(build.getComponents(),
                     Rituals.getPartComponents('QtAlpha'))

  def test_summoning_one_part(self) -> None:
    """A part built gives its target file; one its build refuses raises,
    naming the part."""
    build = mock.Mock()
    build.run.return_value = '/x/libcutienator_QtCute.so'
    with mock.patch.object(Rituals, 'createPartSummon', return_value=build):
      self.assertEqual(Rituals._summonPart('QtCute'),
                       '/x/libcutienator_QtCute.so')
      build.run.side_effect = RuntimeError('refused')
      with self.assertRaises(RuntimeError) as caught:
        Rituals._summonPart('QtCute')
    self.assertIn('The target file of QtCute was not built. refused',
                  str(caught.exception))

  def test_summoning_every_part(self) -> None:
    """Every built part is summoned; a part that cannot be built gets its
    placeholder, saying why, and nothing is raised; the target files
    built are given."""
    for part in ('QtGood', 'QtBroken', 'QtLacking'):
      self._ritual(part, 'q_a', {})
      self._qt(part)
    good = Rituals.getTargetFile('QtGood')

    def summonPart(part: str) -> str:
      if part == 'QtBroken':
        raise RuntimeError('The target file of QtBroken was not built.')
      if part == 'QtLacking':
        raise OSError('no libQt6Lacking.so.6')
      return good

    with mock.patch.object(Rituals, '_summonPart', side_effect=summonPart):
      self.assertEqual(Rituals.summon(), (good,))
    for part, said in (
        ('QtBroken', 'The target file of QtBroken was not built.'),
        ('QtLacking', 'OSError: no libQt6Lacking.so.6')):
      with self.subTest(part=part):
        self.assertEqual(Summon.readNotBuilt(Summon.getLeftOutFileOf(
            Rituals.getTargetFile(part))), said)

  def test_summoning_with_one_job(self) -> None:
    """A machine not saying how many processors it has summons one part
    at a time."""
    self._ritual('QtGood', 'q_a', {})
    self._qt('QtGood')
    with mock.patch.object(os, 'cpu_count', return_value=None), \
        mock.patch.object(Rituals, '_summonPart', return_value='/t.so'):
      self.assertEqual(Rituals.summon(), ('/t.so',))

  def test_summoning_nothing(self) -> None:
    """With no ritual file of a part Qt has, there is nothing to summon."""
    self._ritual('QtFar', 'q_a', {})
    with self.assertRaises(FileNotFoundError) as caught:
      Rituals.summon()
    self.assertIn(self.rituals, str(caught.exception))

  def test_summoning_after_a_ritual_ran(self) -> None:
    """Once a target file is open, nothing is summoned in this Python."""
    Rituals.__opened_targets__['QtCore'] = object()
    with self.assertRaises(RuntimeError) as caught:
      Rituals.summon()
    self.assertIn('already open', str(caught.exception))
