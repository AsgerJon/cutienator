"""
TestCuteWait tests 'WAIT', which stands in a class body for a class that
is made later.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from unittest import mock

from worktoy.mcls import BaseObject
from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import MetaCute, WAIT


class TestCuteWait(BaseTest):
  """
  Tests 'WAIT' on its own: how one is made, what it says of itself,
  what it tells the metaclass of the class holding it, and a read while
  it waits. What happens to the signatures naming it is tested in
  'TestCuteMetaCute'.

  What to know before adding a test
  ---------------------------------

  - Each test has a fresh record of the classes 'MetaCute' made and of
    the fields waiting, in 'setUp'.
  """

  def setUp(self) -> None:
    """A fresh record of the classes made and of the fields waiting."""
    super().setUp()
    for name in ('__made_classes__', '__waiting_fields__'):
      patcher = mock.patch.object(MetaCute, name, dict())
      patcher.start()
      self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING ONE   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_brackets_make_a_wait(self) -> None:
    """'WAIT[...]' gives a new 'WAIT' knowing the name it was given."""
    wait = WAIT['QLater']
    self.assertIsInstance(wait, WAIT)
    self.assertEqual(wait.getWaitingName(), 'QLater')
    self.assertIsNot(wait, WAIT['QLater'])

  def test_brackets_take_a_dotted_name_and_a_part(self) -> None:
    """A class of a namespace goes by its dotted name, and one two parts
    have by its part as well."""
    for right in ('Ns.Later', 'QtCharts:QBarSeries', 'QtCharts:Ns.Later'):
      with self.subTest(right=right):
        self.assertEqual(WAIT[right].getWaitingName(), right)

  def test_brackets_refuse_what_is_no_text(self) -> None:
    """Anything but text between the brackets is refused."""
    for wrong in (7, None, BaseObject, ('QLater',)):
      with self.subTest(wrong=repr(wrong)):
        with self.assertRaises(TypeException):
          _ = WAIT[wrong]

  def test_brackets_refuse_what_no_class_is_called(self) -> None:
    """Text no class could be named is refused, quoting it."""
    for wrong in ('', '2x', 'two words', 'dotted..name', 'Late!',
                  ':Late', 'Part:', 'a:b:C', 'Qt Charts:Late'):
      with self.subTest(wrong=wrong):
        with self.assertRaises(ValueError) as caught:
          _ = WAIT[wrong]
        self.assertIn("received '%s'" % wrong, str(caught.exception))

  def test_made_without_brackets_it_has_no_name(self) -> None:
    """A 'WAIT' made otherwise has no name to give."""
    with self.assertRaises(MissingVariable):
      WAIT().getWaitingName()

  def test_text_shows_it_as_written(self) -> None:
    """Its text is what was written to make it."""
    self.assertEqual(str(WAIT['QLater']), "WAIT['QLater']")
    self.assertEqual(repr(WAIT['Ns.Later']), "WAIT['Ns.Later']")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  IN A CLASS BODY  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_it_tells_the_metaclass_it_waits(self) -> None:
    """In the body of a cute class it is noted as waiting, until the late
    class is made, which then takes its place."""
    wait = WAIT['QLater']

    class QWaiter(metaclass=MetaCute):
      Later = wait

    self.assertEqual(MetaCute.getStillWaiting(), ('QLater',))
    self.assertIs(QWaiter.Later, wait)

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(MetaCute.getStillWaiting(), ())
    self.assertIs(QWaiter.Later, QLater)

  def test_a_read_through_an_object_while_it_waits(self) -> None:
    """Read through an object, a field still waiting raises."""

    class QWaiter(metaclass=MetaCute):
      Later = WAIT['QLater']

    with self.assertRaises(MissingVariable):
      QWaiter().Later

  def test_it_belongs_in_a_cute_class(self) -> None:
    """In the body of a class no 'MetaCute' made it is refused, naming
    the class, the name and the metaclass."""
    with self.assertRaises((TypeError, RuntimeError)) as caught:

      class Plain(BaseObject):
        Later = WAIT['QLater']

    said = str(caught.exception)
    if not isinstance(caught.exception, TypeError):
      said = str(caught.exception.__cause__)
    self.assertIn("WAIT['QLater'] is bound at 'Plain.Later'", said)
    self.assertIn("'BaseMeta'", said)
