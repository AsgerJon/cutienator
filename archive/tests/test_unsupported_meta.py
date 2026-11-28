"""
TestUnsupportedMeta tests the class that stands in a cute class for a
class of Qt that has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.cute import UnsupportedMeta


class QStandIn(metaclass=UnsupportedMeta):
  """
  Qt's class 'QStandIn' of QtMadeUp: the dev tooling cannot write its
  ritual file yet, for what no code taken from Qt's source is to blame.
  """

  __qt_class__ = 'QStandIn'


class QHeir(QStandIn):
  """Stands in for a class of a program built on the stand-in."""


class TestUnsupportedMeta(BaseTest):
  """
  Tests 'UnsupportedMeta': calling the class, or reading an attribute
  it lacks, raises 'NotImplementedError' with its docstring, and what
  it has reads as any class's.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_making_an_object_raises(self) -> None:
    """The message names the class, the class of Qt and why."""
    with self.assertRaises(NotImplementedError) as context:
      QStandIn(1, two=2)
    said = str(context.exception)
    self.assertIn("'QStandIn' cannot be called", said)
    self.assertIn('has no cute class yet', said)
    self.assertIn("Qt's class 'QStandIn' of QtMadeUp", said)

  def test_a_class_built_on_it_raises_too(self) -> None:
    """A class of a program built on it cannot be made either."""
    self.assertIsInstance(QHeir, UnsupportedMeta)
    with self.assertRaises(NotImplementedError) as context:
      QHeir()
    self.assertIn("'QHeir' cannot be called", str(context.exception))

  def test_reading_an_attribute_it_lacks_raises(self) -> None:
    """The message names the attribute as well."""
    with self.assertRaises(NotImplementedError) as context:
      _ = QStandIn.parent
    said = str(context.exception)
    self.assertIn("'QStandIn' has no attribute 'parent'", said)
    self.assertIn('has no cute class yet', said)

  def test_a_name_with_underscores_around_it_is_lacking(self) -> None:
    """'hasattr' asks for such names and lets only 'AttributeError'
    pass, so a tool asking finds the name missing."""
    self.assertFalse(hasattr(QStandIn, '__wrapped__'))
    with self.assertRaises(AttributeError):
      _ = QStandIn.__signature_of_nothing__

  def test_what_the_class_has_is_there(self) -> None:
    """Its docstring, its names and its metaclass read as any class's,
    and nothing is an object of it."""
    self.assertIn("Qt's class 'QStandIn'", QStandIn.__doc__)
    self.assertEqual(QStandIn.__qt_class__, 'QStandIn')
    self.assertEqual(QStandIn.__qualname__, 'QStandIn')
    self.assertIsInstance(QStandIn, UnsupportedMeta)
    self.assertNotIsInstance(object(), QStandIn)
