"""
TestRituals tests the rows of 'Rituals' and how text crosses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import contextlib
import json
import os
import re
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Iterator, List, Set


class TestRituals(BaseTest):
  """
  Tests what 'Rituals' reads from the rows files, and that a 'str'
  crosses to Qt and back as text. The rituals are called for real;
  'setUpClass' builds the shared object of rituals when a ritual file
  is newer than it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.summon()

  @contextlib.contextmanager
  def _madeUpRows(self, parts: Dict[str, Dict[str, Any]]) -> Iterator:
    """
    Has 'Rituals' read rows files made up for one test, while the test
    runs inside: under each part of Qt, a ritual file for each entry,
    with a rows file holding what the entry says, or none at all for an
    entry that is None. What 'Rituals' read before is put back
    afterwards.
    """
    names = ('__ritual_rows__', '__ritual_parts__', '__parts_first__')
    kept = {name: getattr(Rituals, name) for name in names}
    with tempfile.TemporaryDirectory() as folder:
      for partName, written in parts.items():
        partFolder = os.path.join(folder, '%sRituals' % partName)
        os.makedirs(partFolder)
        for stem, rows in written.items():
          open(os.path.join(partFolder, '%s.cpp' % stem), 'w').close()
          if rows is None:
            continue
          if 'rows' not in rows:
            rows = dict(about=[], rows=rows)
          path = os.path.join(partFolder, '%s.json' % stem)
          with open(path, 'w') as file:
            json.dump(rows, file)
      try:
        with mock.patch.object(Rituals, 'getRitualFolder', lambda: folder):
          Rituals._createRows()
          yield
      finally:
        for name, value in kept.items():
          setattr(Rituals, name, value)

  def _readRowsOf(self, parts: Dict[str, Dict[str, Any]]) -> None:
    """Has 'Rituals' read rows files made up for one test, as
    '_madeUpRows' does, and puts back what it read before."""
    with self._madeUpRows(parts):
      pass

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_every_ritual_file_has_its_rows_file(self) -> None:
    """Beside each ritual file lies the rows file of the same name."""
    ritualFiles, rowsFiles = Rituals.getRitualFiles(), Rituals.getRowsFiles()
    self.assertTrue(ritualFiles)
    self.assertEqual(len(ritualFiles), len(rowsFiles))
    for ritualFile, rowsFile in zip(ritualFiles, rowsFiles):
      with self.subTest(ritualFile=ritualFile):
        self.assertEqual(
            os.path.splitext(ritualFile)[0], os.path.splitext(rowsFile)[0])
        self.assertTrue(os.path.isfile(rowsFile))

  def test_a_row_says_what_comes_back_and_what_goes_in(self) -> None:
    """Rows of three rituals, read from the rows files."""
    rows = Rituals.getRows('QtCore')
    expected = dict(
        ritual_ZN7QObject12blockSignalsEb=('bool', 'address', 'bool'),
        ritual_ZNK7QObject10objectNameEv=('text', 'address'),
        ritual_ZN5QSizeD1Ev=('nothing', 'address'),
    )
    for name, row in expected.items():
      with self.subTest(name=name):
        self.assertEqual(rows[name], row)

  def test_every_ritual_named_once_and_in_known_words(self) -> None:
    """Each ritual of the ritual files of a part has one row of known
    words, and each is named once in all. A ritual may be written in
    two files of the part for two systems, as one of Objective-C++ for
    visionOS and one of C++ for the others; its row is one."""
    names = []  # type: List[str]
    written = re.compile(
        r'extern "C" Q_DECL_EXPORT\n[^\n]*?\b(ritual\w*)\(')
    for partName in Rituals.getRitualParts():
      rows = Rituals.getRows(partName)
      found = set()  # type: Set[str]
      for ritualFile in Rituals.getPartRitualFiles(partName):
        with open(ritualFile) as file:
          found.update(written.findall(file.read()))
      with self.subTest(partName=partName):
        self.assertEqual({*rows}, found)
      for name, row in rows.items():
        self.assertIn(partName, Rituals.getPartsOf(name))
        if name not in names:
          names.append(name)
        for word in row:
          self.assertIn(word, Rituals.__row_words__, name)
    self.assertEqual((*names,), Rituals.getRitualNames())

  def test_text_crosses_as_a_str_both_ways(self) -> None:
    """A 'str' handed to a ritual comes back the same, whatever it
    holds."""
    address = Rituals.call('ritual_ZN7QObjectC1EPS_', None)
    setName = 'ritual_ZN7QObject13setObjectNameE14QAnyStringView'
    samples = (
        'cutie', '', 'æøå ÆØÅ', 'smile \U0001F600', 'nul\x00inside',
        'lone \ud83d surrogate', 'x' * 100000,
    )
    for sample in samples:
      with self.subTest(sample=sample[:20]):
        self.assertIsNone(Rituals.call(setName, address, sample))
        back = Rituals.call('ritual_ZNK7QObject10objectNameEv', address)
        self.assertIs(type(back), str)
        self.assertEqual(back, sample)

  def test_every_qstring_made_for_a_call_is_removed(self) -> None:
    """One QString is made for text going in and one comes back with
    text; both are removed before the call returns."""
    made, dropped = [], []  # type: List[int], List[int]
    realMake, realRead = Rituals._makeText, Rituals._readText
    realDrop = Rituals._dropText

    def making(text: Any) -> int:
      made.append(realMake(text))
      return made[-1]

    def reading(address: int) -> str:
      made.append(address)
      return realRead(address)

    def dropping(address: int) -> None:
      dropped.append(address)
      realDrop(address)

    address = Rituals.call('ritual_ZN7QObjectC1EPS_', None)
    setName = 'ritual_ZN7QObject13setObjectNameE14QAnyStringView'
    with mock.patch.object(Rituals, '_makeText', making):
      with mock.patch.object(Rituals, '_readText', reading):
        with mock.patch.object(Rituals, '_dropText', dropping):
          Rituals.call(setName, address, 'cutie')
          self.assertEqual(len(made), 1)
          self.assertEqual(dropped, made)
          Rituals.call('ritual_ZNK7QObject10objectNameEv', address)
          self.assertEqual(len(made), 2)
          self.assertEqual(dropped, made)
          with self.assertRaises(TypeException):
            Rituals.call(setName, address, 5)
          self.assertEqual(dropped, made)

  def test_what_is_no_str_is_refused_as_text(self) -> None:
    """Bytes, a number and None are no text for a QString."""
    address = Rituals.call('ritual_ZN7QObjectC1EPS_', None)
    setName = 'ritual_ZN7QObject13setObjectNameE14QAnyStringView'
    Rituals.call(setName, address, 'kept')
    for wrong in (b'bytes', 5, None):
      with self.subTest(wrong=wrong):
        with self.assertRaises(TypeException):
          Rituals.call(setName, address, wrong)
    back = Rituals.call('ritual_ZNK7QObject10objectNameEv', address)
    self.assertEqual(back, 'kept')

  def test_a_ritual_no_rows_file_lists_is_refused(self) -> None:
    """'call' names the ritual it does not know."""
    with self.assertRaises(LookupError) as caught:
      Rituals.call('ritual_of_nothing')
    self.assertIn('ritual_of_nothing', str(caught.exception))

  def test_a_ritual_file_without_rows_file_is_refused(self) -> None:
    """A ritual file alone says nothing of what its rituals take."""
    with self.assertRaises(FileNotFoundError) as caught:
      self._readRowsOf(dict(QtCore=dict(alone=None)))
    self.assertIn('alone.json', str(caught.exception))

  def test_a_word_that_is_no_word_of_a_row_is_refused(self) -> None:
    """A row may hold the words 'Rituals' knows, and no other."""
    with self.assertRaises(ValueError) as caught:
      odd = dict(odd=dict(ritual_odd=['nothing', 'pointer']))
      self._readRowsOf(dict(QtCore=odd))
    self.assertIn('pointer', str(caught.exception))

  def test_a_ritual_listed_twice_is_refused(self) -> None:
    """Two rows files of one part naming one ritual leave it open which
    one holds."""
    rows = dict(ritual_twice=['nothing'])
    with self.assertRaises(ValueError) as caught:
      self._readRowsOf(dict(QtCore=dict(first=rows, second=rows)))
    self.assertIn('ritual_twice', str(caught.exception))

  def test_two_parts_may_list_one_ritual(self) -> None:
    """A ritual of a class two parts each have, as 'QBarSeries' of
    QtCharts and of QtGraphs, is listed by both, each with its row;
    'call' refuses it, as it cannot tell which part it is for."""
    shared = 'ritual_ZNK10QBarSeries5countEv'
    charts = dict(q_bar_series={shared: ['int', 'address']})
    graphs = dict(q_bar_series={shared: ['long long', 'address']})
    with self._madeUpRows(dict(QtCharts=charts, QtGraphs=graphs)):
      self.assertEqual(Rituals.getPartsOf(shared), ('QtCharts', 'QtGraphs'))
      self.assertEqual(
          Rituals.getRows('QtCharts')[shared], ('int', 'address'))
      self.assertEqual(
          Rituals.getRows('QtGraphs')[shared], ('long long', 'address'))
      self.assertEqual(Rituals.getRitualNames(), (shared,))
      with self.assertRaises(LookupError) as caught:
        Rituals.call(shared, None)
      self.assertIn('callFrom', str(caught.exception))
      self.assertEqual(Rituals._findPart(shared, 'QtGraphs'), 'QtGraphs')
      self.assertEqual(Rituals._findPart(shared, 'QtCharts'), 'QtCharts')

  def test_a_missing_ritual_raises_not_implemented(self) -> None:
    """A ritual 'summon' left out raises 'NotImplementedError' naming
    the function it calls and what the compiler said; one Qt's own
    '#if' compiled out raises it too."""
    rows = dict(q_made_up=dict(ritual_gone=['nothing'],
                               ritual_hidden=['nothing']))
    reason = 'the compiler refused it on this machine: x.cpp:3:1: oops'
    leftOut = dict(ritual_gone=('void QMadeUp::gone()', reason))
    missing = frozenset(('ritual_gone', 'ritual_hidden'))
    with self._madeUpRows(dict(QtCore=rows)), mock.patch.dict(
        Rituals.__opened_targets__, dict(QtCore=object())), mock.patch.dict(
        Rituals.__missing_rituals__, dict(QtCore=missing)), mock.patch.dict(
        Rituals.__left_out_rituals__, dict(QtCore=leftOut)):
      with self.assertRaises(NotImplementedError) as caught:
        Rituals.call('ritual_gone')
      self.assertIn('void QMadeUp::gone()', str(caught.exception))
      self.assertIn('x.cpp:3:1: oops', str(caught.exception))
      with self.assertRaises(NotImplementedError) as caught:
        Rituals.call('ritual_hidden')
      self.assertIn("'#if'", str(caught.exception))

  def test_what_summon_left_out_is_read_beside_the_target(self) -> None:
    """The left-out file beside the target file of a part says which
    rituals were left out; no file, none."""
    with tempfile.TemporaryDirectory() as folder:
      target = os.path.join(folder, 'libcutienator_QtCore.so')
      with mock.patch.object(Rituals, 'getTargetFile', lambda p: target):
        self.assertEqual(Rituals.getLeftOut('QtCore'), {})
        record = {'ritual files': {'QtCoreRituals/q_made_up.cpp': dict(
            dropped=[], whole=None, leftOut=dict(
                ritual_gone=['void QMadeUp::gone()', 'why']))}}
        leftOutFile = os.path.join(
            folder, 'libcutienator_QtCore.left_out.json')
        with open(leftOutFile, 'w') as file:
          json.dump(record, file)
        self.assertEqual(Rituals.getLeftOut('QtCore'), dict(
            ritual_gone=('void QMadeUp::gone()', 'why')))

  def test_the_parts_a_part_sees_first(self) -> None:
    """What the rows files of a part say under 'parts first' comes
    first in the order the part sees the parts in, after the part
    itself; a part whose rows files say nothing sees itself first and
    then the installed parts, in alphabetical order."""
    first = ['QtGraphsWidgets', 'QtGraphs', 'QtWidgets', 'QtGui']
    rows = {'parts first': first, 'about': [], 'rows': dict(ritual_a=[
        'nothing'])}
    plain = dict(q_plain=dict(ritual_b=['nothing']))
    made = dict(QtGraphsWidgets=dict(one=rows), QtCore=plain)
    with self._madeUpRows(made):
      self.assertEqual(Rituals.getPartsFirst('QtGraphsWidgets'), (*first,))
      self.assertEqual(Rituals.getPartsFirst('QtCore'), ())
      order = Rituals.getPartOrder('QtGraphsWidgets')
      self.assertEqual(order[:4], (*first,))
      self.assertEqual(Rituals.getPartOrder('QtCore')[0], 'QtCore')
      self.assertEqual(
          Rituals.getPartComponents('QtGraphsWidgets')[:4], (*first,))
      seen = Rituals.getPartComponents('QtCore')
      needs = Rituals.getQtDependencies('QtCore')
      self.assertEqual(seen[:1 + len(needs)], ('QtCore', *needs))
      rest = seen[1 + len(needs):]
      self.assertEqual(rest, (*sorted(rest),))
      self.assertNotIn('QtCore', seen[1:])

  def test_qt_module_files_are_read(self) -> None:
    """Qt's files describing its parts give, for each part, the parts
    it needs, nearest first, its private side and what it was built with
    counted, itself and names no file describes left out."""
    files = {
      'qt_lib_core.pri': 'QT.core.name = QtCore\nQT.core.depends =\n',
      'qt_lib_core_private.pri': (
          'QT.core_private.name = QtCore\n'
          'QT.core_private.depends = core\n'),
      'qt_lib_gui.pri': 'QT.gui.name = QtGui\nQT.gui.depends = core\n',
      'qt_lib_utils_private.pri': (
          'QT.utils_private.name = QtUtils\n'
          'QT.utils_private.depends = core_private gui_private utils\n'),
      'qt_lib_utils.pri': (
          'QT.utils.name = QtUtils\nQT.utils.depends = \n'
          'QT.utils.run_depends = gone_private gui\n'),
      'qt_lib_helpers.pri': (
          'QT.helpers.name = QtHelpers\nQT.helpers.depends =\n'
          'QT.helpers.run_depends = utils\n'),
      'qt_lib_gui_private.pri': (
          'QT.gui_private.name = QtGui\n'
          'QT.gui_private.depends = core_private gui\n'),
    }
    with tempfile.TemporaryDirectory() as folder:
      for name, text in files.items():
        with open(os.path.join(folder, name), 'w') as file:
          file.write(text)
      with open(os.path.join(folder, 'not_a_part.txt'), 'w') as file:
        file.write('QT.other.name = QtOther\n')
      found = Rituals.readQtModules(folder)
    self.assertEqual(found['QtCore'], ())
    self.assertEqual(found['QtGui'], ('QtCore',))
    self.assertEqual(found['QtUtils'], ('QtGui', 'QtCore'))
    self.assertEqual(found['QtHelpers'], ('QtUtils', 'QtGui', 'QtCore'))
    self.assertNotIn('QtOther', found)

  def test_a_part_looks_first_in_the_parts_it_needs(self) -> None:
    """A part looks in the headers of the parts Qt says it needs before
    those of any other part: QtWidgets in QtGui's and QtCore's before
    those of a part it does not need, whatever the alphabet says."""
    if 'QtWidgets' not in Rituals.getRitualParts():
      self.skipTest('no ritual files of QtWidgets')
    needs = Rituals.getQtDependencies('QtWidgets')
    self.assertIn('QtCore', needs)
    self.assertIn('QtGui', needs)
    seen = Rituals.getPartComponents('QtWidgets')
    self.assertEqual(seen[:1 + len(needs)], ('QtWidgets', *needs))
    self.assertEqual(len(seen), len(set(seen)))

  def test_the_parts_first_of_one_part_must_agree(self) -> None:
    """The ritual files of a part are made with one order of the parts:
    rows files of it saying two orders are refused."""
    one = {'parts first': ['QtGraphs', 'QtGui'], 'about': [],
           'rows': dict(ritual_one=['nothing'])}
    two = {'parts first': ['QtGraphs', 'QtQuick'], 'about': [],
           'rows': dict(ritual_two=['nothing'])}
    with self.assertRaises(ValueError) as caught:
      self._readRowsOf(dict(QtGraphs=dict(one=one, two=two)))
    self.assertIn('parts first', str(caught.exception))

  def test_rows_made_up_for_a_test_leave_the_real_ones(self) -> None:
    """The helper of these tests puts the rows of 'Rituals' back."""
    before = Rituals.getRows('QtCore')
    fine = dict(fine=dict(ritual_fine=['nothing', 'int']))
    self._readRowsOf(dict(QtCore=fine))
    self.assertIs(Rituals.getRows('QtCore'), before)

  def test_a_part_with_no_ritual_folder_is_refused(self) -> None:
    """'getRows' names the part it has no ritual files of."""
    with self.assertRaises(LookupError) as caught:
      Rituals.getRows('QtOfNothing')
    self.assertIn('QtOfNothing', str(caught.exception))

  def test_the_target_file_of_a_part(self) -> None:
    """Each part has its own, beside the ritual folder."""
    here = os.path.dirname(Rituals.getRitualFolder())
    self.assertEqual(
        Rituals.getTargetFile('QtCore'),
        os.path.join(here, 'libcutienator_QtCore.so'))
    self.assertEqual(
        Rituals.getTargetFiles(),
        (*(Rituals.getTargetFile(p) for p in Rituals.getBuiltParts()),))
    with self.assertRaises(TypeException):
      Rituals.getTargetFile(None)

  def test_text_needs_the_rituals_of_qstring(self) -> None:
    """With a row taking text and no ritual of QString listed for
    QtCore, nothing is opened."""
    takes = dict(q_takes=dict(ritual_takes_text=['nothing', 'text']))
    with self._madeUpRows(dict(QtCore=takes)):
      with self.assertRaises(LookupError) as caught:
        Rituals._createOpened('QtCore')
    self.assertIn('QString', str(caught.exception))
