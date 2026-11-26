"""
TestUnsupportedMeta tests the class that stands in a cute class at the
name of a function of Qt that has no cute function yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import inspect

from worktoy.dispatch import overload
from worktoy.work_test import BaseTest

from cutienator.cute import CuteMixin, MetaCute, UnsupportedMeta


class QStandIn(CuteMixin, metaclass=MetaCute):
  """Stands in for a cute class with one function and one name of Qt
  that has none."""

  __qt_class__ = 'QStandIn'

  @overload(int)
  def doubled(self, number: int) -> int:
    """Stands in for a cute function."""
    return 2 * number

  class nativeEvent(metaclass=UnsupportedMeta):
    """
    Qt's 'bool QStandIn::nativeEvent(const QByteArray &eventType, void
    *message, qintptr *result)': names 'void', which has no cute class
    yet.
    """


class QHeir(QStandIn):
  """Stands in for a cute class built on the one above."""

  __qt_class__ = 'QHeir'


class TestUnsupportedMeta(BaseTest):
  """
  Tests 'UnsupportedMeta': calling the class, or reading an attribute
  it lacks, raises 'NotImplementedError' with its docstring, and the
  cute class around it works as before.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_calling_through_the_class_raises(self) -> None:
    """The message names the class, the function of Qt and why."""
    with self.assertRaises(NotImplementedError) as context:
      QStandIn.nativeEvent(b'xcb', None, None)
    said = str(context.exception)
    self.assertIn("'QStandIn.nativeEvent' cannot be called", said)
    self.assertIn("names 'void', which has no cute class yet.", said)

  def test_calling_through_an_object_raises(self) -> None:
    """A class is no descriptor: an object hands it on as it is."""
    standIn = QStandIn.__new__(QStandIn)
    self.assertIs(standIn.nativeEvent, QStandIn.nativeEvent)
    with self.assertRaises(NotImplementedError):
      standIn.nativeEvent()

  def test_a_class_built_on_it_has_it(self) -> None:
    """So has an object of that class."""
    self.assertIs(QHeir.nativeEvent, QStandIn.nativeEvent)
    with self.assertRaises(NotImplementedError):
      QHeir.__new__(QHeir).nativeEvent()

  def test_reading_an_attribute_it_lacks_raises(self) -> None:
    """The message names the attribute as well."""
    with self.assertRaises(NotImplementedError) as context:
      _ = QStandIn.nativeEvent.result
    said = str(context.exception)
    self.assertIn("'QStandIn.nativeEvent' has no attribute 'result'", said)

  def test_a_name_with_underscores_around_it_is_lacking(self) -> None:
    """'hasattr' asks for such names and lets only 'AttributeError'
    pass, so a tool asking finds the name missing."""
    self.assertFalse(hasattr(QStandIn.nativeEvent, '__wrapped__'))
    with self.assertRaises(AttributeError):
      _ = QStandIn.nativeEvent.__signature_of_nothing__

  def test_what_the_class_has_is_there(self) -> None:
    """Its docstring, its name and its metaclass read as any class's."""
    self.assertIn('QStandIn::nativeEvent', QStandIn.nativeEvent.__doc__)
    self.assertEqual(
        QStandIn.nativeEvent.__qualname__, 'QStandIn.nativeEvent')
    self.assertIsInstance(QStandIn.nativeEvent, UnsupportedMeta)

  def test_the_cute_class_works_as_before(self) -> None:
    """Its functions are called, and its members can be walked."""
    self.assertEqual(QStandIn.__new__(QStandIn).doubled(21), 42)
    names = [name for name, _ in inspect.getmembers(QStandIn)]
    self.assertIn('nativeEvent', names)
