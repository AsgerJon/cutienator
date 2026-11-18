"""
TestRituals tests the rows of 'Rituals' and how text crosses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import tempfile
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List


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
      Rituals.build()

  def _readRowsOf(self, written: Dict[str, Any]) -> None:
    """
    Has 'Rituals' read rows files made up for one test: one for each
    entry of 'written', holding what the entry says, or none at all for
    an entry that is None. The rows it had are put back afterwards.
    """
    kept = Rituals.__ritual_rows__
    with tempfile.TemporaryDirectory() as folder:
      ritualFiles = []
      for stem, rows in written.items():
        ritualFiles.append(os.path.join(folder, '%s.cpp' % stem))
        if rows is None:
          continue
        with open(os.path.join(folder, '%s.json' % stem), 'w') as file:
          json.dump(dict(about=[], rows=rows), file)
      rowsFiles = [path[:-4] + '.json' for path in ritualFiles]
      try:
        with mock.patch.object(Rituals, 'getRitualFiles',
                               lambda: (*ritualFiles,)):
          with mock.patch.object(Rituals, 'getRowsFiles',
                                 lambda: (*rowsFiles,)):
            Rituals._createRows()
      finally:
        Rituals.__ritual_rows__ = kept

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
        self.assertEqual(ritualFile[:-4], rowsFile[:-5])
        self.assertTrue(os.path.isfile(rowsFile))

  def test_a_row_says_what_comes_back_and_what_goes_in(self) -> None:
    """Rows of three rituals, read from the rows files."""
    rows = Rituals.getRows()
    expected = dict(
        ritual_ZN7QObject12blockSignalsEb=('bool', 'address', 'bool'),
        ritual_ZNK7QObject10objectNameEv=('text', 'address'),
        ritual_ZN5QSizeD1Ev=('nothing', 'address'),
    )
    for name, row in expected.items():
      with self.subTest(name=name):
        self.assertEqual(rows[name], row)

  def test_every_ritual_named_once_and_in_known_words(self) -> None:
    """Each ritual of the ritual files has one row of known words."""
    rows = Rituals.getRows()
    self.assertEqual((*rows,), Rituals.getRitualNames())
    count = 0
    for ritualFile in Rituals.getRitualFiles():
      with open(ritualFile) as file:
        count += file.read().count('extern "C" Q_DECL_EXPORT')
    self.assertEqual(len(rows), count)
    for name, row in rows.items():
      for word in row:
        self.assertIn(word, Rituals.__row_words__, name)

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
      self._readRowsOf(dict(alone=None))
    self.assertIn('alone.json', str(caught.exception))

  def test_a_word_that_is_no_word_of_a_row_is_refused(self) -> None:
    """A row may hold the words 'Rituals' knows, and no other."""
    with self.assertRaises(ValueError) as caught:
      self._readRowsOf(dict(odd=dict(ritual_odd=['nothing', 'pointer'])))
    self.assertIn('pointer', str(caught.exception))

  def test_a_ritual_listed_twice_is_refused(self) -> None:
    """Two rows files naming one ritual leave it open which one holds."""
    rows = dict(ritual_twice=['nothing'])
    with self.assertRaises(ValueError) as caught:
      self._readRowsOf(dict(first=rows, second=rows))
    self.assertIn('ritual_twice', str(caught.exception))

  def test_rows_made_up_for_a_test_leave_the_real_ones(self) -> None:
    """The helper of these tests puts the rows of 'Rituals' back."""
    before = Rituals.getRows()
    self._readRowsOf(dict(fine=dict(ritual_fine=['nothing', 'int'])))
    self.assertIs(Rituals.getRows(), before)

  def test_text_needs_the_rituals_of_qstring(self) -> None:
    """With a row taking text and no ritual of QString listed, nothing
    is opened."""
    rows = dict(ritual_takes_text=('nothing', 'text'))
    with mock.patch.object(Rituals, 'getRows', lambda **kwargs: rows):
      with self.assertRaises(LookupError) as caught:
        Rituals._createOpened()
    self.assertIn('QString', str(caught.exception))
