"""
TestTrialTrial tests 'Trial', one test written once as steps, and
'qObjectTrials', the trials written for QObject.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.trial import Trial, qObjectTrials


class TestTrialTrial(BaseTest):
  """
  Tests 'Trial': its name, the steps it is written, what it refuses
  where a step is written, and what it works out from its steps; and
  the trials of QObject.

  What to know before adding a test
  ---------------------------------

  - A trial runs nothing, so nothing here needs Qt or a compiler.
  """

  @staticmethod
  def _trial() -> Trial:
    """A trial with a name and two objects made."""
    trial = Trial()
    trial.setName('two objects')
    trial.make('mother', 'QObject')
    trial.make('child', 'QObject')
    return trial

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE NAME   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_name(self) -> None:
    """Asked for before it is set, it raises; set again, it is
    replaced."""
    trial = Trial()
    with self.assertRaises(MissingVariable):
      trial.getName()
    trial.setName('first')
    trial.setName('QObject: parent')
    self.assertEqual(trial.getName(), 'QObject: parent')

  def test_what_no_name_is(self) -> None:
    """A name is text with a letter or a digit."""
    with self.assertRaises(TypeException):
      Trial().setName(7)
    with self.assertRaises(ValueError) as caught:
      Trial().setName(': -')
    self.assertIn("received ': -'", str(caught.exception))

  def test_its_text(self) -> None:
    """Its name, once it has one, and the count of its steps."""
    trial = Trial()
    self.assertEqual(str(trial), '<Trial with no name yet, of 0 steps>')
    trial.setName('named')
    trial.make('one', 'QObject')
    self.assertEqual(str(trial), "<Trial 'named' of 1 steps>")
    self.assertEqual(repr(trial), str(trial))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE STEPS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_steps_in_the_order_written(self) -> None:
    """Each kind of step, as it is kept."""
    trial = self._trial()
    self.assertEqual(Trial().getSteps(), ())
    trial.call('child', 'setParent', 'mother')
    trial.call('child', 'setParent', None)
    trial.call('child', 'deleteLater')
    trial.expectSame('child', 'parent', 'mother')
    trial.expectNothing('mother', 'parent')
    self.assertEqual(trial.getSteps(), (
        ('make', 'mother', 'QObject', ()),
        ('make', 'child', 'QObject', ()),
        ('call', 'child', 'setParent', ('mother',)),
        ('call', 'child', 'setParent', (None,)),
        ('call', 'child', 'deleteLater', ()),
        ('same', 'child', 'parent', ('mother',)),
        ('nothing', 'mother', 'parent', ()),
    ))

  def test_the_classes_and_objects(self) -> None:
    """Each class made, once, in order of first use; the class of each
    object made; an object never made is refused."""
    trial = self._trial()
    trial.make('timer', 'QTimer')
    trial.make('other', 'QObject')
    self.assertEqual(trial.getClassNames(), ('QObject', 'QTimer'))
    self.assertEqual(trial.getClassOf('timer'), 'QTimer')
    for asking in (trial, Trial()):
      with self.subTest(asking=asking):
        with self.assertRaises(LookupError) as caught:
          asking.getClassOf('nobody')
        self.assertIn("named 'nobody'", str(caught.exception))

  def test_an_object_made_twice(self) -> None:
    """An object name is made once."""
    trial = self._trial()
    with self.assertRaises(ValueError) as caught:
      trial.make('child', 'QTimer')
    self.assertIn("named 'child' was made", str(caught.exception))

  def test_what_no_name_of_both_languages_is(self) -> None:
    """A name that is no text, no plain name, or a word one of the two
    languages keeps, is refused where it is written."""
    trial = self._trial()
    with self.assertRaises(TypeException):
      trial.make(7, 'QObject')
    for word in ('class', 'lambda', 'new', '2nd', 'blå', 'a-b'):
      with self.subTest(word=word):
        with self.assertRaises(ValueError) as caught:
          trial.make(word, 'QObject')
        self.assertIn("Received '%s' for 'objectName'" % word,
                      str(caught.exception))
    with self.assertRaises(ValueError):
      trial.make('fine', 'delete')

  def test_steps_naming_an_object_never_made(self) -> None:
    """A call, or an expectation, on or with an object no step made is
    refused; so is a method name of no language."""
    trial = self._trial()
    for write in (
        lambda: trial.call('nobody', 'parent'),
        lambda: trial.call('child', 'setParent', 'nobody'),
        lambda: trial.expectSame('nobody', 'parent', 'mother'),
        lambda: trial.expectSame('child', 'parent', 'nobody'),
        lambda: trial.expectNothing('nobody', 'parent'),
    ):
      with self.subTest(write=write):
        with self.assertRaises(LookupError):
          write()
    for write in (
        lambda: trial.call('child', 'for'),
        lambda: trial.expectSame('child', 'if', 'mother'),
        lambda: trial.expectNothing('child', 'while'),
    ):
      with self.subTest(write=write):
        with self.assertRaises(ValueError):
          write()
    self.assertEqual(len(trial.getSteps()), 2)

  def test_the_label_of_an_expectation(self) -> None:
    """The words both halves print before 'true' or 'false'."""
    self.assertEqual(Trial.getLabel('child', 'parent', 'mother'),
                     'child.parent() is mother')
    self.assertEqual(Trial.getLabel('child', 'parent', None),
                     'child.parent() is nothing')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE TRIALS OF QOBJECT  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_trials_of_qobject(self) -> None:
    """New trials each time, named, of QObject alone."""
    first, = qObjectTrials()
    again, = qObjectTrials()
    self.assertIsNot(first, again)
    self.assertEqual(first.getName(), 'QObject: parent and setParent')
    self.assertEqual(first.getClassNames(), ('QObject',))
    self.assertEqual(len(first.getSteps()), 8)
    first.make('extra', 'QObject')
    self.assertEqual(len(again.getSteps()), 8)
