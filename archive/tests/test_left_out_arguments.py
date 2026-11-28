"""
TestLeftOutArguments tests the arguments Qt fills in when they are left
out, where Qt writes what it fills in as more than one plain value.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.QtCore import QDate, QDir, QMarginsF
from cutienator.QtGui import QColor, QPageLayout, QPageSize


class TestLeftOutArguments(BaseTest):
  """Tests left-out arguments on the class files the dev tooling wrote,
  against Qt itself. None of them needs an application."""

  def test_flags_joined(self) -> None:
    """Qt fills in 'SortFlags(Name | IgnoreCase)' for the sorting of a
    QDir made of a path and a name filter."""
    expected = QDir.SortFlag.Name | QDir.SortFlag.IgnoreCase
    self.assertEqual(QDir('/', '*').sorting(), expected)

  def test_flags_joined_given(self) -> None:
    """What is handed over still goes before what Qt fills in."""
    directory = QDir('/', '*', QDir.SortFlag.Size)
    self.assertEqual(directory.sorting(), QDir.SortFlag.Size)

  def test_number_worked_out(self) -> None:
    """Qt fills in 'USHRT_MAX', which it writes as a sum, for the alpha
    of 'QColor.fromRgba64': the color is opaque."""
    self.assertEqual(QColor.fromRgba64(1, 2, 3).alpha(), 255)
    self.assertEqual(QColor.fromRgba64(1, 2, 3, 0).alpha(), 0)

  def test_value_made_of_numbers(self) -> None:
    """Qt fills in 'QMarginsF(0, 0, 0, 0)' for the least margins of a
    QPageLayout."""
    pageSize = QPageSize(QPageSize.PageSizeId.A4)
    portrait = QPageLayout.Orientation.Portrait
    margins = QMarginsF(1, 2, 3, 4)
    layout = QPageLayout(pageSize, portrait, margins)
    least = layout.minimumMargins()
    found = (least.left(), least.top(), least.right(), least.bottom())
    self.assertEqual(found, (0.0, 0.0, 0.0, 0.0))
    self.assertEqual(layout.margins().top(), 2.0)

  def test_constant_of_another_class(self) -> None:
    """Qt fills in 'QLocale::DefaultTwoDigitBaseYear', which is 1900,
    for the base year of 'QDate.fromString'."""
    whole = QDate.fromString('2024-02-29', 'yyyy-MM-dd')
    found = (whole.year(), whole.month(), whole.day())
    self.assertEqual(found, (2024, 2, 29))
    self.assertEqual(QDate.fromString('24-02-29', 'yy-MM-dd').year(), 1924)
    later = QDate.fromString('24-02-29', 'yy-MM-dd', 2000)
    self.assertEqual(later.year(), 2024)
