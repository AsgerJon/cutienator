"""
TestPrivateAndProtected tests that a function C++ marks 'private' or
'protected' is called like any other. C++ means by those words that
only the class itself, or a class built on it, may call the function;
cutienator takes every function Qt has.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.QtCore import QObject, QModelIndex
from cutienator.QtGui import QStandardItemModel
from cutienator.occult import Rituals


class TestPrivateAndProtected(BaseTest):
  """None of these needs an application."""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.summon()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_protected_function_is_called_from_outside(self) -> None:
    """Qt's 'QObject::sender()' and 'QObject::senderSignalIndex()' are
    protected. Called where no signal is being answered, they give no
    object and -1, as Qt says they do."""
    thing = QObject()
    self.assertIsNone(thing.sender())
    self.assertEqual(thing.senderSignalIndex(), -1)

  def test_a_protected_function_that_changes_something(self) -> None:
    """Qt's 'QAbstractItemModel::beginResetModel()' and its
    'endResetModel()' are protected, and so is 'createIndex'."""
    model = QStandardItemModel(2, 3)
    model.beginResetModel()
    model.endResetModel()
    self.assertEqual(model.rowCount(), 2)
    made = model.createIndex(1, 2, 0)
    self.assertIsInstance(made, QModelIndex)
    self.assertEqual((made.row(), made.column()), (1, 2))
    self.assertTrue(made.isValid())

  def test_the_compiler_is_told_not_to_mind(self) -> None:
    """The ritual files are compiled with '-fno-access-control', and
    the sigil files list rituals of protected functions."""
    names = Rituals.getRitualNames()
    self.assertIn('ritual_ZNK7QObject6senderEv', names)
    self.assertIn('ritual_ZN18QAbstractItemModel15beginResetModelEv', names)
