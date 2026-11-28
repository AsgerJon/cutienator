"""
TestWAIT tests 'WAIT', which stands in a class body for a class that is
made later.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls import BaseObject
from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.waitaminute.desc import ReadOnlyError, ProtectedError
from worktoy.work_test import BaseTest

from cutienator.cute import MetaCute, UnsupportedMeta, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestWAIT(BaseTest):
  """
  Tests 'WAIT' on its own: how one is made, what it says of itself,
  what it tells the metaclass, and what reading, writing and deleting
  its name gives. What happens to the signatures that name it is tested
  in 'TestMetaCute'.

  What to know before adding a test
  ---------------------------------

  'MetaCute' knows a class by its name alone, for the whole program. A
  test that puts a 'WAIT' in a cute class body uses a name for the late
  class that no other test uses, in this file or another, and makes the
  late class before it ends. A 'WAIT' that is put in no class body is
  noted nowhere and needs neither.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING ONE   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_brackets_make_a_wait(self) -> None:
    """'WAIT[...]' gives a new WAIT that knows the name it was given."""
    wait = WAIT['BracketLate']
    self.assertIsInstance(wait, WAIT)
    self.assertEqual(wait.getWaitingName(), 'BracketLate')
    self.assertIsNot(wait, WAIT['BracketLate'])

  def test_brackets_refuse_what_is_no_text(self) -> None:
    """'WAIT[...]' refuses anything but text between its brackets."""
    for wrong in (7, None, BaseObject, ('BracketLate',)):
      with self.subTest(wrong=repr(wrong)):
        with self.assertRaises(TypeException):
          _ = WAIT[wrong]

  def test_brackets_refuse_what_no_class_is_called(self) -> None:
    """'WAIT[...]' refuses text that no class could have as its name."""
    for wrong in ('', '2x', 'two words', 'dotted..name', 'Late!',
                  ':Late', 'Part:', 'a:b:C', 'Qt Charts:Late'):
      with self.subTest(wrong=wrong):
        with self.assertRaises(ValueError):
          _ = WAIT[wrong]

  def test_brackets_take_a_dotted_name_and_a_part(self) -> None:
    """A class of a namespace goes by its dotted name, and one two
    parts of Qt have by its part as well."""
    for right in ('Ns.Late', 'QtCharts:Late', 'QtCharts:Ns.Late'):
      with self.subTest(right=right):
        self.assertEqual(WAIT[right].getWaitingName(), right)

  def test_made_around_the_brackets_has_no_name(self) -> None:
    """A WAIT made without the brackets has no name to give."""
    with self.assertRaises(MissingVariable):
      WAIT().getWaitingName()

  def test_text_shows_it_as_written(self) -> None:
    """The text of a WAIT is what was written to make it."""
    wait = WAIT['TextLate']
    self.assertEqual(str(wait), "WAIT['TextLate']")
    self.assertEqual(repr(wait), "WAIT['TextLate']")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TELLING THE METACLASS  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_tells_the_metaclass_as_its_class_is_made(self) -> None:
    """A WAIT in a cute body is noted by 'MetaCute' with class and name."""

    class TellEarly(BaseObject, metaclass=MetaCute):
      TellLate = WAIT['TellLate']

    wait = TellEarly.TellLate
    self.assertIs(wait.getFieldOwner(), TellEarly)
    self.assertEqual(wait.getFieldName(), 'TellLate')
    self.assertIn('TellLate', MetaCute.getStillWaiting())

    class TellLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertNotIn('TellLate', MetaCute.getStillWaiting())

  def test_a_class_of_two_parts_is_told_by_its_part(self) -> None:
    """A cute class whose body says its part is what a WAIT with that
    part waits for, and not a WAIT of the name alone."""

    class PartEarly(BaseObject, metaclass=MetaCute):
      ChartsLate = WAIT['QtMadeUpCharts:PartLate']
      GraphsLate = WAIT['QtMadeUpGraphs:PartLate']

    still = MetaCute.getStillWaiting()
    self.assertIn('QtMadeUpCharts:PartLate', still)
    self.assertIn('QtMadeUpGraphs:PartLate', still)

    class ChartsPartLate(BaseObject, metaclass=MetaCute):
      __qt_class__ = 'PartLate'
      __qt_part__ = 'QtMadeUpCharts'

    still = MetaCute.getStillWaiting()
    self.assertNotIn('QtMadeUpCharts:PartLate', still)
    self.assertIn('QtMadeUpGraphs:PartLate', still)
    self.assertIs(PartEarly.ChartsLate, ChartsPartLate)

    class GraphsPartLate(BaseObject, metaclass=MetaCute):
      __qt_class__ = 'PartLate'
      __qt_part__ = 'QtMadeUpGraphs'

    self.assertNotIn('QtMadeUpGraphs:PartLate', MetaCute.getStillWaiting())
    self.assertIs(PartEarly.GraphsLate, GraphsPartLate)
    self.assertIs(PartEarly.ChartsLate, ChartsPartLate)

  def test_a_class_without_cute_class_is_waited_for_by_its_stand_in(
      self) -> None:
    """A class 'UnsupportedMeta' makes, standing in for a class of Qt
    that has no cute class yet, settles the WAIT for that class as a
    cute class would: the waiting class holds the stand-in, and making
    one raises, saying why."""

    class StandInEarly(BaseObject, metaclass=MetaCute):
      Missing = WAIT['StandInLate']

    self.assertIn('StandInLate', MetaCute.getStillWaiting())

    class StandInLate(metaclass=UnsupportedMeta):
      """Qt's class 'StandInLate' of QtMadeUp: no ritual file yet."""
      __qt_class__ = 'StandInLate'

    self.assertNotIn('StandInLate', MetaCute.getStillWaiting())
    self.assertIs(StandInEarly.Missing, StandInLate)
    with self.assertRaises(NotImplementedError) as context:
      StandInEarly.Missing()
    self.assertIn('no ritual file yet', str(context.exception))

  def test_refuses_an_owner_that_is_not_cute(self) -> None:
    """'hookSetName' refuses a class whose metaclass notices nothing."""
    wait = WAIT['StrayLate']
    for owner in (BaseObject, int):
      with self.subTest(owner=owner.__name__):
        with self.assertRaises(TypeError):
          wait.hookSetName(owner, 'StrayLate')
    self.assertNotIn('StrayLate', MetaCute.getStillWaiting())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  READING, WRITING, DELETING   # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_class_read_gives_the_wait_itself(self) -> None:
    """Read through the waiting class, the name gives the WAIT."""

    class ReadEarly(BaseObject, metaclass=MetaCute):
      ReadLate = WAIT['ReadLate']

    self.assertIs(ReadEarly.ReadLate, ReadEarly.__dict__['ReadLate'])
    self.assertIsInstance(ReadEarly.ReadLate, WAIT)

    class ReadLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertIs(ReadEarly.ReadLate, ReadLate)

  def test_object_read_refuses_until_the_class_is_made(self) -> None:
    """Through an object the name is missing until the class is made."""

    class ObjectEarly(BaseObject, metaclass=MetaCute):
      ObjectLate = WAIT['ObjectLate']

    early = ObjectEarly()
    with self.assertRaises(MissingVariable):
      _ = early.ObjectLate
    self.assertFalse(hasattr(early, 'ObjectLate'))

    class ObjectLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertTrue(hasattr(early, 'ObjectLate'))
    self.assertIs(early.ObjectLate, ObjectLate)

  def test_hook_runs_before_the_refusal(self) -> None:
    """A read through an object runs 'hookPreGet', then refuses."""
    seen = []

    class Watched(WAIT):

      def hookPreGet(self, instance: Any, **kwargs) -> None:
        seen.append((instance, self.instance, self.owner))

    class WatchEarly(BaseObject, metaclass=MetaCute):
      WatchLate = Watched['WatchLate']

    early = WatchEarly()
    with self.assertRaises(MissingVariable):
      _ = early.WatchLate
    self.assertEqual(len(seen), 1)
    for seenObject in seen[0][:2]:
      self.assertIs(seenObject, early)
    self.assertIs(seen[0][2], WatchEarly)

    class WatchLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertIs(early.WatchLate, WatchLate)
    self.assertEqual(len(seen), 1)

  def test_cannot_be_replaced_through_an_object(self) -> None:
    """An object can neither write nor delete the name of a WAIT."""

    class FixedEarly(BaseObject, metaclass=MetaCute):
      FixedLate = WAIT['FixedLate']

    early = FixedEarly()
    with self.subTest(attempt='write'):
      with self.assertRaises(ReadOnlyError):
        early.FixedLate = 7
    with self.subTest(attempt='delete'):
      with self.assertRaises(ProtectedError):
        del early.FixedLate
    self.assertIsInstance(FixedEarly.FixedLate, WAIT)

    class FixedLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertIs(FixedEarly.FixedLate, FixedLate)
