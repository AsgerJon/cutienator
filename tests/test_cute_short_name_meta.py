"""
TestCuteShortNameMeta tests 'ShortNameMeta', which gives the names of an
enum of Qt to the class that holds the enum.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteNum, ShortNameMeta


class TestCuteShortNameMeta(BaseTest):
  """
  Tests 'ShortNameMeta' through the enums and flags built on it: the
  names of an enum C++ does not keep inside it are bound on the class
  holding it, and a scoped enum keeps its own.
  """

  def test_an_unscoped_enum_gives_its_names_to_its_holder(self) -> None:
    """Each name of an enum is bound on the class whose body holds it."""

    class QHolder:

      class Direction(CuteNum):
        Forward = Kee[int](0)
        Backward = Kee[int](1)

      class Option(CuteFlags):
        Wide = 0x1
        Tall = 0x2

    self.assertIs(QHolder.Forward, QHolder.Direction.Forward)
    self.assertIs(QHolder.Backward, QHolder.Direction.Backward)
    self.assertIs(QHolder.Wide, QHolder.Option.Wide)
    self.assertIs(QHolder.Tall, QHolder.Option.Tall)

  def test_a_scoped_enum_keeps_its_names(self) -> None:
    """A scoped enum binds nothing on its holder."""

    class QHolder:

      class Direction(CuteNum, scoped=True):
        Forward = Kee[int](0)

      class Option(CuteFlags, scoped=True):
        Wide = 0x1

    self.assertIs(QHolder.Direction.isScoped(), True)
    self.assertFalse(hasattr(QHolder, 'Forward'))
    self.assertFalse(hasattr(QHolder, 'Wide'))

  def test_an_enum_is_unscoped_until_said(self) -> None:
    """An enum not saying 'scoped' is not scoped."""

    class Direction(CuteNum):
      Forward = Kee[int](0)

    self.assertIs(Direction.isScoped(), False)

  def test_scoped_must_be_a_bool(self) -> None:
    """'scoped' that is no 'bool' is refused when the names are bound."""
    with self.assertRaises((TypeException, RuntimeError)) as caught:

      class QHolder:

        class Direction(CuteNum, scoped='yes'):
          Forward = Kee[int](0)

    self.assertIn('scoped', str(caught.exception))

  def test_a_name_held_by_the_same_thing_is_fine(self) -> None:
    """A name the holder holds already, with that very member, is kept."""

    class Direction(CuteNum):
      Forward = Kee[int](0)

    class QHolder:
      Forward = Direction.Forward
      Kind = Direction

    self.assertIs(QHolder.Forward, Direction.Forward)

  def test_a_name_held_by_something_else_is_refused(self) -> None:
    """A name the holder holds with something else raises, naming the
    holder, the enum and the name."""
    with self.assertRaises((TypeError, RuntimeError)) as caught:

      class QHolder:
        Forward = 'something else'

        class Direction(CuteNum):
          Forward = Kee[int](0)

    said = str(caught.exception)
    for word in ("'QHolder'", "'Direction'", "'Forward'"):
      with self.subTest(word=word):
        self.assertIn(word, said)

  def test_the_names_are_asked_of_a_subclass(self) -> None:
    """'ShortNameMeta' itself has no names to give."""
    with self.assertRaises(NotImplementedError):
      ShortNameMeta.getShortNames(object)
