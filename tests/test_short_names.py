"""
TestShortNames tests that the names of an enum of Qt are names of the
class holding the enum as well, where C++ has them there.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteNum, CuteFlags
from cutienator.QtCore import Qt, QEvent
from cutienator.QtWidgets import QMessageBox


class Shape(CuteNum):
  """Stands in for an enum C++ does not scope."""

  Round = Kee[int](0)
  Square = Kee[int](1)


class Mood(CuteNum, scoped=True):
  """Stands in for an 'enum class' of C++."""

  Calm = Kee[int](0)
  Loud = Kee[int](1)


class Edge(CuteFlags):
  """Stands in for a flags enum that names no zero."""

  Top = 0x1
  Left = 0x2
  Corner = Top | Left


class Option(CuteFlags):
  """Stands in for a flags enum that names its zero, as Qt's 'None'."""

  NULL = 0x0
  Bold = 0x1


class Holder:
  """Holds the enums as a class of Qt holds its own."""

  Shape = Shape
  Mood = Mood
  Edge = Edge
  Edges = Edge
  Option = Option


class Heir(Holder):
  """Built on the class that holds the enums."""


class TestShortNames(BaseTest):
  """
  Tests 'ShortNameMeta': an enum class bound in the body of another
  class gives that class its names, unless C++ scopes the enum.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_names_of_an_enum_are_names_of_its_holder(self) -> None:
    """Each name gives the very member the enum has there."""
    self.assertIs(Holder.Round, Shape.Round)
    self.assertIs(Holder.Square, Shape.Square)

  def test_the_names_of_flags_are_names_of_their_holder(self) -> None:
    """Each name gives the very value the flags class has there."""
    self.assertIs(Holder.Top, Edge.Top)
    self.assertIs(Holder.Corner, Edge.Top | Edge.Left)
    self.assertIs(Holder.Bold, Option.Bold)

  def test_a_scoped_enum_keeps_its_names(self) -> None:
    """The names of an 'enum class' stay inside the enum."""
    self.assertTrue(Mood.isScoped())
    self.assertFalse(Shape.isScoped())
    self.assertFalse(hasattr(Holder, 'Calm'))
    self.assertFalse(hasattr(Holder, 'Loud'))
    self.assertIs(Holder.Mood.Calm, Mood.Calm)

  def test_null_is_a_name_of_the_holder_only_where_named(self) -> None:
    """'NULL' comes from the flags class that names its zero."""
    self.assertIs(Holder.NULL, Option.NULL)
    self.assertIsNot(Holder.NULL, Edge.NULL)

  def test_a_class_built_on_the_holder_has_the_names(self) -> None:
    """So has an object of either."""
    self.assertIs(Heir.Round, Shape.Round)
    self.assertIs(Heir().Top, Edge.Top)
    self.assertIs(Holder().Square, Shape.Square)

  def test_something_else_at_a_name_is_refused(self) -> None:
    """A holder with another thing at a name of its enum is not made.
    Before Python 3.12 the refusal comes inside a 'RuntimeError'."""
    with self.assertRaises((TypeError, RuntimeError)) as context:
      class Clash:
        Shape = Shape
        Round = 'something else'
    raised = context.exception
    if isinstance(raised, RuntimeError):
      raised = raised.__cause__
    self.assertIsInstance(raised, TypeError)
    self.assertIn('Round', str(raised))

  def test_scoped_takes_a_bool_only(self) -> None:
    """Anything but True or False for 'scoped' is refused."""

    class Odd(CuteNum, scoped='yes'):
      One = Kee[int](1)

    with self.assertRaises(TypeException):
      Odd.isScoped()

  def test_the_names_of_qt(self) -> None:
    """The enums of Qt give their names to the classes Qt writes them
    in, and to the namespace 'Qt'."""
    self.assertIs(Qt.AlignLeft, Qt.AlignmentFlag.AlignLeft)
    self.assertIs(Qt.KeepAspectRatio, Qt.AspectRatioMode.KeepAspectRatio)
    self.assertIs(Qt.Key_Escape, Qt.Key.Key_Escape)
    self.assertIs(QEvent.Timer, QEvent.Type.Timer)
    self.assertIs(QEvent.NULL, QEvent.Type.NULL)
    self.assertIs(QMessageBox.Yes, QMessageBox.StandardButton.Yes)
    self.assertIs(Qt.AlignLeft | Qt.AlignTop, Qt.Alignment(0x21))
    self.assertIs(QEvent(QEvent.Timer).type(), QEvent.Timer)

  def test_the_scoped_enums_of_qt_keep_their_names(self) -> None:
    """'Qt::TimerId' is an 'enum class', so 'Qt.Invalid' is no name."""
    self.assertTrue(Qt.TimerId.isScoped())
    self.assertFalse(hasattr(Qt, 'Invalid'))
    self.assertFalse(hasattr(Qt, 'Granted'))
