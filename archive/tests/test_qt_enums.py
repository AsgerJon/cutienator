"""
TestQtEnums tests the enums of Qt that the dev tooling wrote into the
package: those of the namespace 'Qt' and those of the classes it has.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.cute import CuteNum, CuteFlags
from cutienator.QtCore import Qt, QEvent, QMetaObject, QSize, QThread
from cutienator.QtGui import QPainter
from cutienator.QtWidgets import QMessageBox
from cutienator.occult import Rituals


class TestQtEnums(BaseTest):
  """
  Tests that the enums are where Qt has them, hold the numbers Qt gives,
  and go into real functions of Qt. The numbers themselves are verified
  against the compiler by the dev tooling when the files are written.
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_namespace_holds_its_enums(self) -> None:
    """'Qt' has one name for each of its 95 enums, each of a cute kind."""
    held = [v for v in vars(Qt).values() if isinstance(v, type)]
    kinds = (CuteNum, CuteFlags)
    enums = {v for v in held if issubclass(v, kinds)}
    self.assertEqual(len(enums), 95)
    self.assertEqual(sum(1 for e in enums if issubclass(e, CuteFlags)), 24)

  def test_an_enum_of_the_namespace(self) -> None:
    """A plain enum holds its names with their numbers."""
    mode = Qt.AspectRatioMode
    self.assertTrue(issubclass(mode, CuteNum))
    names = [member.name for member in mode]
    expected = [
      'IgnoreAspectRatio',
      'KeepAspectRatio',
      'KeepAspectRatioByExpanding',
    ]
    self.assertEqual(names, expected)
    self.assertEqual(mode.KeepAspectRatio.value, 1)

  def test_a_flags_enum_of_the_namespace(self) -> None:
    """A flags enum combines, and both names of Qt hold one class."""
    flag = Qt.AlignmentFlag
    self.assertTrue(issubclass(flag, CuteFlags))
    self.assertIs(Qt.Alignment, flag)
    both = flag.AlignLeft | flag.AlignTop
    self.assertEqual(both.value, 0x21)
    self.assertIs(flag.AlignLeading, flag.AlignLeft)
    self.assertIs(flag.AlignCenter, flag.AlignVCenter | flag.AlignHCenter)
    self.assertEqual(flag.AlignHorizontal_Mask.value, 0x1f)

  def test_flags_without_a_sign(self) -> None:
    """A flags enum that needs the last bit is kept without a sign."""
    modifier = Qt.KeyboardModifier
    self.assertEqual(modifier.KeyboardModifierMask.value, 0xfe000000)
    self.assertIs(modifier.NULL, modifier.NoModifier)
    self.assertEqual((~modifier.ShiftModifier).value, 0xfdffffff)

  def test_flags_with_a_number_below_zero(self) -> None:
    """A number below 0 is kept as Qt gives it."""
    self.assertEqual(QMessageBox.StandardButton.ButtonMask.value, -769)

  def test_names_that_differ_by_case_alone(self) -> None:
    """'Qt::Key' has both of each pair."""
    key = Qt.Key
    self.assertEqual(key.Key_Dead_a.value, 0x01001280)
    self.assertEqual(key.Key_Dead_A.value, 0x01001281)
    self.assertEqual(key.Key_Escape.value, 0x01000000)

  def test_the_word_of_c_for_none(self) -> None:
    """Qt's 'QEvent::None' is 'QEvent.Type.NULL'."""
    self.assertEqual(QEvent.Type.NULL.value, 0)
    self.assertEqual(QEvent.Type.Timer.value, 1)
    self.assertEqual(QEvent.Type.User.value, 1000)

  def test_an_event_type_of_your_own(self) -> None:
    """A number above 'User' is a member without a name."""
    custom = QEvent.Type(QEvent.Type.User + 1)
    self.assertIsInstance(custom, QEvent.Type)
    self.assertEqual(custom.value, 1001)
    self.assertIs(QEvent.Type(1001), custom)

  def test_the_enums_of_the_classes(self) -> None:
    """Each class holds the enums Qt writes inside it."""
    self.assertTrue(issubclass(QThread.Priority, CuteNum))
    self.assertTrue(issubclass(QThread.QualityOfService, CuteNum))
    self.assertTrue(issubclass(QMetaObject.Call, CuteNum))
    self.assertTrue(issubclass(QPainter.CompositionMode, CuteNum))
    self.assertTrue(issubclass(QMessageBox.Icon, CuteNum))
    self.assertTrue(issubclass(QMessageBox.ButtonRole, CuteNum))
    self.assertIs(QPainter.RenderHints, QPainter.RenderHint)
    self.assertIs(QPainter.PixmapFragmentHints, QPainter.PixmapFragmentHint)
    self.assertIs(QMessageBox.StandardButtons, QMessageBox.StandardButton)
    self.assertIs(QMessageBox.Options, QMessageBox.Option)
    self.assertEqual(QPainter.RenderHint.Antialiasing.value, 1)
    self.assertEqual(QMessageBox.StandardButton.Yes.value, 0x4000)

  def test_a_member_into_a_real_function_of_qt(self) -> None:
    """'QSize.scaled' takes a member of 'Qt.AspectRatioMode'."""
    size = QSize(4, 2)
    scaled = size.scaled(10, 10, Qt.AspectRatioMode.KeepAspectRatio)
    self.assertEqual((scaled.width(), scaled.height()), (10, 5))
    scaled = size.scaled(10, 10, Qt.AspectRatioMode.IgnoreAspectRatio)
    self.assertEqual((scaled.width(), scaled.height()), (10, 10))

  def test_a_member_into_and_out_of_an_event(self) -> None:
    """An event made with a member gives back that member."""
    event = QEvent(QEvent.Type.Timer)
    self.assertIs(event.type(), QEvent.Type.Timer)
    self.assertTrue(event.type() == 1)
